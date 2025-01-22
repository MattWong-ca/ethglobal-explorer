'use client';
import { useState, useEffect } from "react";

interface Event {
  name: string;
  // Placeholder interfaces for future data
  date?: string;
  location?: string;
  participants?: number;
  projects?: number;
}

interface TemporaryEventData {
  name: string;
}

export default function Events() {
  const [events, setEvents] = useState<Event[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchEvents = async () => {
      setIsLoading(true);
      try {
        const response = await fetch('/api/events');
        const data = await response.json();
        console.log(data);
        // Transform the data into the Event interface format
        const formattedEvents = data.data.map((event: TemporaryEventData) => ({
          name: event.name,
          date: 'TBD', // placeholder
          location: 'TBD', // placeholder
          participants: 0, // placeholder
          projects: 0, // placeholder
        }));
        setEvents(formattedEvents);
      } catch (error) {
        console.error('Error fetching events:', error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchEvents();
  }, []);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-6">ETHGlobal Events</h1>

      <div className="overflow-x-auto shadow-md rounded-lg">
        {isLoading ? (
          <div className="text-center py-4">Loading...</div>
        ) : (
          <table className="min-w-full table-auto">
            <thead className="bg-purple-100">
              <tr className="text-sm text-black font-large uppercase">
                <th className="px-4 py-2 text-left tracking-wider">Event Name</th>
                <th className="px-4 py-2 text-left tracking-wider">Date</th>
                <th className="px-4 py-2 text-left tracking-wider">Location</th>
                <th className="px-4 py-2 text-left tracking-wider">Participants</th>
                <th className="px-4 py-2 text-left tracking-wider">Projects</th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {events.map((event, index) => (
                <tr key={index} className="hover:bg-gray-50">
                  <td className="px-4 py-2">
                    <span className="text-blue-600 hover:text-blue-800 cursor-pointer">
                      {event.name}
                    </span>
                  </td>
                  <td className="px-4 py-2 text-gray-900">{event.date}</td>
                  <td className="px-4 py-2 text-gray-900">{event.location}</td>
                  <td className="px-4 py-2 text-gray-900">{event.participants}</td>
                  <td className="px-4 py-2 text-gray-900">{event.projects}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}