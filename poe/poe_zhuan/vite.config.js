import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import fs from 'fs'  // 导入 fs 模块

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  server: {
    host: '0.0.0.0', // 允许外部访问
    port: 5173,      // 你希望使用的端口
    https: {
      key: fs.readFileSync('/www/wwwroot/poe/ssl/private.key'),  // 这里指定私钥路径
      cert: fs.readFileSync('/www/wwwroot/poe/ssl/server.crt'),  // 这里指定证书路径
    }
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
