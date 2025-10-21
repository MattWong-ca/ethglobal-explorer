import { createClient } from '@supabase/supabase-js';
import { NextResponse } from 'next/server';

// Rate limit configuration
const WINDOW_SIZE_IN_MINUTES = 15;
const MAX_REQUESTS_PER_WINDOW = 1000;

// Store IP addresses and their request counts
const ipRequests = new Map<string, { count: number, windowStart: number }>();

// Clean up old entries on each request (serverless-friendly)
function cleanupOldEntries() {
    const now = Date.now();
    for (const [ip, data] of ipRequests.entries()) {
        if (now - data.windowStart > WINDOW_SIZE_IN_MINUTES * 60 * 1000) {
            ipRequests.delete(ip);
        }
    }
}

// Validate environment variables
function validateEnvironment() {
    if (!process.env.SUPABASE_URL) {
        throw new Error('SUPABASE_URL environment variable is not set');
    }
    if (!process.env.SUPABASE_SERVICE_KEY) {
        throw new Error('SUPABASE_SERVICE_KEY environment variable is not set');
    }
}

const supabase = createClient(
    process.env.SUPABASE_URL!,
    process.env.SUPABASE_SERVICE_KEY!
);

export async function GET(request: Request) {
    try {
        // Validate environment variables
        validateEnvironment();
        
        // Clean up old rate limit entries
        cleanupOldEntries();
        
        const ip = request.headers.get('x-forwarded-for') ?? '127.0.0.1';
        const now = Date.now();
        
        // Get or create rate limit data for this IP
        let rateData = ipRequests.get(ip);
        if (!rateData || now - rateData.windowStart > WINDOW_SIZE_IN_MINUTES * 60 * 1000) {
            rateData = { count: 1, windowStart: now };
            ipRequests.set(ip, rateData);
        } else {
            // Increment count before checking limit
            rateData.count++;
            ipRequests.set(ip, rateData);
            
            // Check if rate limit exceeded
            if (rateData.count > MAX_REQUESTS_PER_WINDOW) {
                const resetTime = new Date(rateData.windowStart + WINDOW_SIZE_IN_MINUTES * 60 * 1000);
                return NextResponse.json(
                    { error: 'Too many requests' },
                    { 
                        status: 429,
                        headers: {
                            'X-RateLimit-Limit': MAX_REQUESTS_PER_WINDOW.toString(),
                            'X-RateLimit-Remaining': '0',
                            'X-RateLimit-Reset': resetTime.getTime().toString(),
                        }
                    }
                );
            }
        }

    const { searchParams } = new URL(request.url);
    const page = parseInt(searchParams.get('page') || '1');
    const searchTerm = searchParams.get('q') || '';
    const selectedEvent = searchParams.get('event') || '';
    const selectedPrize = searchParams.get('prize') || '';
    const selectedTag = searchParams.get('tag') || '';
    const itemsPerPage = 100;

    try {
        let query = supabase
            .from('projects')
            .select(`
        id,
        title,
        description,
        url,
        event,
        project_prizes(
          prizes(name, img_url)
        )
      `).order('id', { ascending: false });

        let countQuery = supabase
            .from('projects')
            .select('*', { count: 'exact', head: true });
        if (searchTerm) {
            query = query.or(`title.ilike.%${searchTerm}%`);
            countQuery = countQuery.or(`title.ilike.%${searchTerm}%`);
        }
        if (selectedEvent) {
            query = query.eq('event', selectedEvent);
            countQuery = countQuery.eq('event', selectedEvent);
        }
        if (selectedPrize) {
            const { data: projectIds } = await supabase
                .from('project_prizes')
                .select('project_id, prize:prize_id!inner(name)')
                .eq('prize.name', selectedPrize);
            if (projectIds) {
                const ids = projectIds.map(p => p.project_id);
                query = query.in('id', ids);
                countQuery = countQuery.in('id', ids);
            }
        }
        if (selectedTag) {
            query = query.or(`description.ilike.%${selectedTag}%`);
            countQuery = countQuery.or(`description.ilike.%${selectedTag}%`);
            // const tagTerms = selectedTags.split(',').map(tag => tag.trim());
            // const tagFilters = tagTerms.map(tag => `description.ilike.%${tag}%`);
            // query = query.or(tagFilters.join(','));
            // countQuery = countQuery.or(tagFilters.join(','));
        }

        const [{ count }, { data: fetchedData }] = await Promise.all([
            countQuery,
            query.range(
                (page - 1) * itemsPerPage,
                page * itemsPerPage - 1
            )
        ]);

        const transformedData = fetchedData?.map(project => ({
            ...project,
            project_prizes: project.project_prizes.map(pp => pp.prizes).flat()
        }));
        
        return NextResponse.json({
            data: transformedData,
            totalCount: count
        });
    } catch (error) {
        console.error('Error in projects API:', error);
        return NextResponse.json(
            { 
                error: 'Internal Server Error',
                message: error instanceof Error ? error.message : 'Unknown error'
            },
            { status: 500 }
        );
    }
    } catch (error) {
        console.error('Error in projects API:', error);
        return NextResponse.json(
            { 
                error: 'Internal Server Error',
                message: error instanceof Error ? error.message : 'Unknown error'
            },
            { status: 500 }
        );
    }
}