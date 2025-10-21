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
            rateData.count++;
            ipRequests.set(ip, rateData);
            
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
    const itemsPerPage = 100;

    try {
        let query = supabase
            .from('events')
            .select(`
                id,
                name
            `);

        let countQuery = supabase
            .from('events')
            .select('*', { count: 'exact', head: true });

        if (searchTerm) {
            query = query.or(`name.ilike.%${searchTerm}%`);
            countQuery = countQuery.or(`name.ilike.%${searchTerm}%`);
        }

        const [{ count }, { data: fetchedData }] = await Promise.all([
            countQuery,
            query.range(
                (page - 1) * itemsPerPage,
                page * itemsPerPage - 1
            )
        ]);
        
        return NextResponse.json({
            data: fetchedData,
            totalCount: count
        });
    } catch (error) {
        console.error('Error in events API:', error);
        return NextResponse.json(
            { 
                error: 'Internal Server Error',
                message: error instanceof Error ? error.message : 'Unknown error'
            },
            { status: 500 }
        );
    }
    } catch (error) {
        console.error('Error in events API:', error);
        return NextResponse.json(
            { 
                error: 'Internal Server Error',
                message: error instanceof Error ? error.message : 'Unknown error'
            },
            { status: 500 }
        );
    }
}