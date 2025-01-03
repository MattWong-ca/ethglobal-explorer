'use client';
import { useEffect, useState } from "react";
import { createClient } from '@supabase/supabase-js'
interface Project {
  id: number;
  title: string;
  project_prizes: Prize[];
  description: string;
  event: string;
  url: string;
}

interface Prize {
  name: string;
  img_url: string;
}
export default function Home() {
  const [data, setData] = useState<Project[]>([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [isLoading, setIsLoading] = useState(false);
  const [totalCount, setTotalCount] = useState(0);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedEvent, setSelectedEvent] = useState('');
  const [selectedPrize, setSelectedPrize] = useState('');
  const itemsPerPage = 100;

  const supabase = createClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
  )

  const fetchPageData = async (page: number) => {
    setIsLoading(true);
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
        // First get the projects IDs that have the selected prize
        const { data: projectIds } = await supabase
          .from('project_prizes')
          .select('project_id, prize:prize_id!inner(name)')
          .eq('prize.name', selectedPrize);
        console.log('projectIds', projectIds);
        if (projectIds) {
          const ids = projectIds.map(p => p.project_id);
          query = query.in('id', ids);
          countQuery = countQuery.in('id', ids);
        }
      }

      const { count, error: countError } = await countQuery;
      
      if (countError) throw countError;
      setTotalCount(count || 0);

      const startRange = (page - 1) * itemsPerPage;
      const endRange = startRange + itemsPerPage - 1;
      const { data: fetchedData, error } = await query.range(startRange, endRange);
      console.log('fetchedData', fetchedData);
      if (error) throw error;

      const transformedData = fetchedData.map(project => ({
        ...project,
        project_prizes: project.project_prizes.map(pp => pp.prizes).flat()
      }));

      setData(transformedData);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    const timer = setTimeout(() => {
      setCurrentPage(1);
      fetchPageData(1);
    }, 300);

    return () => clearTimeout(timer);
  }, [searchTerm, selectedEvent, selectedPrize]);

  useEffect(() => {
    fetchPageData(currentPage);
  }, [currentPage]);

  const totalPages = Math.ceil(totalCount / itemsPerPage);

  return (
    <div className="container mx-auto p-4">
      <div className="mb-4 flex gap-4">
        <input
          type="text"
          placeholder="Search projects..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="px-4 py-2 border rounded-md"
        />
        <select
          value={selectedEvent}
          onChange={(e) => setSelectedEvent(e.target.value)}
          className="px-4 py-2 border rounded-md"
        >
          <option value="">All Events</option>
          <option value="Frameworks">Frameworks</option>
          <option value="ETHGlobal Bangkok">ETHGlobal Bangkok</option>
        </select>
        <select
          value={selectedPrize}
          onChange={(e) => setSelectedPrize(e.target.value)}
          className="px-4 py-2 border rounded-md"
        >
          <option value="Finalist">Finalist</option>
          <option value="Filecoin">Filecoin</option>
          <option value="">All Prizes</option>
        </select>
      </div>

      <div className="overflow-x-auto shadow-md rounded-lg">
        {isLoading ? (
          <div className="text-center py-4">Loading...</div>
        ) : (
          <table className="min-w-full table-auto">
            <thead className="bg-gray-100">
              <tr>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Description</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Event</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Prizes</th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {data.map((project) => (
                <tr key={project.id} className="hover:bg-gray-50">
                  <td className="px-6 py-4 whitespace-nowrap">
                    <a 
                      href={project.url} 
                      target="_blank" 
                      rel="noopener noreferrer"
                      className="text-blue-600 hover:text-blue-800 hover:underline"
                    >
                      {project.title}
                    </a>
                  </td>
                  <td className="px-6 py-4">
                    <div className="text-sm text-gray-900 line-clamp-2">{project.description}</div>
                  </td>
                  <td className="px-6 py-4">
                    <div className="text-sm text-gray-900">{project.event}</div>
                  </td>
                  <td className="px-6 py-4">
                    <div className="flex flex-wrap gap-2">
                      {project.project_prizes.map((prize: Prize, index: number) => (
                        <span 
                          key={index}
                          className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800"
                        >
                          {prize.name}
                        </span>
                      ))}
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>

      <div className="flex justify-center mt-4 gap-2">
        <button
          onClick={() => setCurrentPage(prev => Math.max(prev - 1, 1))}
          disabled={currentPage === 1 || isLoading}
          className="px-4 py-2 border rounded-md disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-50"
        >
          Previous
        </button>
        <span className="px-4 py-2">
          Page {currentPage} of {totalPages}
        </span>
        <button
          onClick={() => setCurrentPage(prev => Math.min(prev + 1, totalPages))}
          disabled={currentPage === totalPages || isLoading}
          className="px-4 py-2 border rounded-md disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-50"
        >
          Next
        </button>
      </div>
    </div>
  );
}