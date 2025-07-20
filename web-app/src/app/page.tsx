'use client';
import { useEffect, useState } from "react";
import Image from "next/image";
import { allEvents, allPrizes, eventDisplayNames } from '@/lib/constants';

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
  const initialParams = typeof window !== 'undefined' 
    ? new URLSearchParams(window.location.search)
    : new URLSearchParams();

  const [data, setData] = useState<Project[]>([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [isLoading, setIsLoading] = useState(true);
  const [totalCount, setTotalCount] = useState(0);
  const [searchTerm, setSearchTerm] = useState(initialParams.get('q') || '');
  const [selectedEvent, setSelectedEvent] = useState(initialParams.get('event') || 'ETHGlobal Prague');
  const [selectedPrize, setSelectedPrize] = useState(initialParams.get('prize') || '');
  const [selectedTag, setSelectedTag] = useState(initialParams.get('tag') || '');
  const itemsPerPage = 100;
  
  const fetchPageData = async (page: number) => {
    setIsLoading(true);
    try {
      const params = new URLSearchParams({
        page: page.toString(),
        q: searchTerm,
        event: selectedEvent,
        prize: selectedPrize,
        tag: selectedTag
      });

      const response = await fetch(`/api/projects?${params}`);
      const { data: fetchedData, totalCount } = await response.json();
      
      setData(fetchedData);
      setTotalCount(totalCount);
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
      
      const params = new URLSearchParams();
      if (searchTerm) params.set('q', searchTerm);
      if (selectedEvent) params.set('event', selectedEvent);
      if (selectedPrize) params.set('prize', selectedPrize);
      if (selectedTag) params.set('tag', selectedTag);
      
      const newUrl = `${window.location.pathname}${params.toString() ? '?' + params.toString() : ''}`;
      window.history.pushState({}, '', newUrl);
    }, 300);

    return () => clearTimeout(timer);
  }, [searchTerm, selectedEvent, selectedPrize, selectedTag]);

  useEffect(() => {
    fetchPageData(currentPage);
  }, [currentPage]);

  
  useEffect(() => {
    const handlePopState = () => {
      const params = new URLSearchParams(window.location.search);
      setSearchTerm(params.get('q') || '');
      setSelectedEvent(params.get('event') || '');
      setSelectedPrize(params.get('prize') || '');
      setSelectedTag(params.get('tag') || '');
    };

    window.addEventListener('popstate', handlePopState);
    return () => window.removeEventListener('popstate', handlePopState);
  }, []);

  const totalPages = Math.ceil(totalCount / itemsPerPage);

  return (
    <div>
      <nav className="sticky top-0 bg-white border-b border-gray-200 py-3">
        <div className="px-4 flex justify-between items-center">
          <div className="font-semibold">
            <a href="https://www.ethglobalexplorer.com" className="hover:text-gray-600">
              <span className="inline">ETHGlobal Explorer</span>
            </a>
          </div>
          <a 
            href="https://github.com/MattWong-ca/ethglobal-explorer" 
            target="_blank" 
            rel="noopener noreferrer"
            className="text-gray-700 hover:text-gray-900"
          >
            <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
              <path fillRule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clipRule="evenodd" />
            </svg>
          </a>
        </div>
      </nav>

      <div className="container mx-auto p-4">
        <div className="mb-4 flex flex-col md:flex-row gap-4">
          <input
            type="text"
            placeholder="Search projects..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="px-4 py-2 border rounded-md w-full md:w-64 text-black"
          />
          <select
            value={selectedEvent}
            onChange={(e) => setSelectedEvent(e.target.value)}
            className="px-4 py-2 border rounded-md w-full md:w-48 text-black"
          >
            <option value="">All Events</option>
            {allEvents.map((event, index) => (
              <option key={index} value={event}>
                {eventDisplayNames[event] || event}
              </option>
            ))}
          </select>
          <select
            value={selectedPrize}
            onChange={(e) => setSelectedPrize(e.target.value)}
            className="px-4 py-2 border rounded-md w-full md:w-48 text-black"
          >
            <option value="">All Prizes</option>
            {allPrizes.map((prizeName, index) => (
              <option key={index} value={prizeName}>{prizeName}</option>
            ))}
          </select>
          {/* 
            Current Tag filter only does a single keyword search on the description,
            so it's not completely reflective of all projects related to the tag. 
            Ideally it searches for multiple keywords (eg. "stables", "stablecoin").
            In the future, vector search should be implemented.
          */}
          <select
            value={selectedTag}
            onChange={(e) => setSelectedTag(e.target.value)}
            className="px-4 py-2 border rounded-md w-full md:w-48 text-black"
          >
            <option value="">All Tags</option>
            <option value="AI Agent">AI Agents</option>
            <option value="Stablecoin">Stablecoins</option>
            <option value="NFT">NFTs</option>
            <option value="DAO">DAOs</option>
          </select>
        </div>

        <div className="overflow-x-auto shadow-md rounded-lg">
          {isLoading ? (
            <div className="text-center py-4">Loading...</div>
          ) : (
            <table className="min-w-full table-auto">
              <thead className="bg-purple-100">
                <tr className="text-sm text-black font-large uppercase">
                  <th className="px-2 py-1 text-left tracking-wider">Name</th>
                  <th className="px-2 py-1 text-left tracking-wider">Description</th>
                  <th className="py-1 text-left tracking-wider">Event</th>
                  <th className="py-1 text-left tracking-wider">Prizes</th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-200">
                {data.map((project) => (
                  <tr key={project.id} className="hover:bg-gray-50">
                    <td className="px-2 py-1 max-w-[130px]">
                      <a 
                        href={project.url} 
                        target="_blank" 
                        rel="noopener noreferrer"
                        className="text-sm text-blue-600 hover:text-blue-800 hover:underline truncate block"
                      >
                        {project.title}
                      </a>
                    </td>
                    <td className="px-2 py-1 min-w-[400px] max-w-[800px]">
                      <div className="text-sm text-gray-900 truncate">{project.description}</div>
                    </td>
                    <td className="min-w-[100px]">
                      <div className="text-sm text-gray-900">
                        {eventDisplayNames[project.event] || project.event}
                      </div>
                    </td>
                    <td className="py-1">
                      <div className="flex flex-wrap gap-2">
                        {project.project_prizes.map((prize: Prize, index: number) => (
                          <Image 
                            key={index}
                            src={prize.img_url}
                            alt={prize.name}
                            title={prize.name}
                            className={`h-6 w-6 object-contain ${prize.img_url == 'https://ethglobal.b-cdn.net/organizations/xdat5/square-logo/default.png' ? '' : 'rounded-full'}`}
                            width={24}
                            height={24}
                          />
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
    </div>
  );
}