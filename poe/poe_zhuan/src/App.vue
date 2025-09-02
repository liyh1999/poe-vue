<template>
  <div class="app-container">
    <el-container class="main-container">
      <el-aside width="200px" class="sidebar">
        <common-aside></common-aside>
      </el-aside>
      <el-container class="content-container">
        <el-header height="60px" class="header">
          <common-header></common-header>
        </el-header>
        <el-main class="main-content">
          <router-view v-slot="{ Component }">
            <transition name="fade" mode="out-in">
              <component :is="Component" />
            </transition>
          </router-view>
        </el-main>
      </el-container>
    </el-container>
    <mobile-navigation />
  </div>
</template>

<script>
import CommonAside from "./components/CommonAside.vue";
import CommonHeader from "./components/CommonHeader.vue";
import MobileNavigation from "./components/MobileNavigation.vue";

export default {
  components: {
      CommonAside,
      CommonHeader,
      MobileNavigation,
  }
}
</script>

<style lang="less" scoped>
.app-container {
  height: 100vh;
  width: 100%;
  background: var(--bg-primary);
}

.main-container {
  height: 100%;
}

.sidebar {
  background: var(--bg-secondary);
  border-right: 1px solid var(--border-light);
  box-shadow: var(--shadow-light);
  z-index: 1000;
}

.content-container {
  background: var(--bg-primary);
}

.header {
  background: var(--bg-secondary);
  border-bottom: 1px solid var(--border-light);
  box-shadow: var(--shadow-light);
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.main-content {
  background: var(--bg-primary);
  padding: var(--spacing-lg);
  overflow-y: auto;
}

/* 页面切换动画 */
.fade-enter-active,
.fade-leave-active {
  transition: opacity var(--transition-base);
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .sidebar {
    display: none;
  }
  
  .main-content {
    padding: var(--spacing-md);
    padding-bottom: 80px; /* 为移动端导航留出空间 */
  }
  
  .header {
    height: 50px;
  }
}

@media (max-width: 480px) {
  .main-content {
    padding: var(--spacing-sm);
    padding-bottom: 80px; /* 为移动端导航留出空间 */
  }
}
</style>

