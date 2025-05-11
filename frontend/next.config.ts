import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
  /* config options here */
  output: 'export',
  trailingSlash: true, // required for static export
  basePath: '/static',        // keep root-relative
  assetPrefix: '',
};

export default nextConfig;
