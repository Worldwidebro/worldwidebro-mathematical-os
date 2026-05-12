import react from '@vitejs/plugin-react'

export default {
  plugins: [react()],
  server: {
    port: 5174,
    proxy: {
      '/mcp': {
        target: 'http://localhost:9002',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/mcp/, '')
      },
      '/temporal': {
        target: 'http://localhost:7233',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/temporal/, '')
      }
    }
  }
}
