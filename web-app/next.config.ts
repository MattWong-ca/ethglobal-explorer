import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'ethglobal.b-cdn.net',
      },
    ],
  },
};

export default nextConfig;
