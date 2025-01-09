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
  const [data, setData] = useState<Project[]>([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [isLoading, setIsLoading] = useState(true);
  const [totalCount, setTotalCount] = useState(0);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedEvent, setSelectedEvent] = useState('');
  const [selectedPrize, setSelectedPrize] = useState('');
  const [selectedTag, setSelectedTag] = useState('');
  const itemsPerPage = 100;

  const fetchPageData = async (page: number) => {
    setIsLoading(true);
    try {
      const params = new URLSearchParams({
        page: page.toString(),
        searchTerm: searchTerm,
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
    }, 300);

    return () => clearTimeout(timer);
  }, [searchTerm, selectedEvent, selectedPrize, selectedTag]);

  useEffect(() => {
    fetchPageData(currentPage);
  }, [currentPage]);

  const totalPages = Math.ceil(totalCount / itemsPerPage);

  return (
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
            <option key={index} value={event}>{event}</option>
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
  );
}