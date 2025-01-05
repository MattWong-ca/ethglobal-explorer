import { createClient } from '@supabase/supabase-js';
import { NextResponse } from 'next/server';

const supabase = createClient(
    process.env.SUPABASE_URL!,
    process.env.SUPABASE_SERVICE_KEY!
);

export async function GET(request: Request) {
    const { searchParams } = new URL(request.url);
    const page = parseInt(searchParams.get('page') || '1');
    const searchTerm = searchParams.get('searchTerm') || '';
    const selectedEvent = searchParams.get('event') || '';
    const selectedPrize = searchParams.get('prize') || '';
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
      `);

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
        console.error('Error:', error);
        return NextResponse.json(
            { error: 'Internal Server Error' },
            { status: 500 }
        );
    }
}