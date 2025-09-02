<template>
  <div class="mobile-nav" v-if="isMobile">
    <div class="nav-item" 
         v-for="item in navItems" 
         :key="item.name"
         :class="{ active: $route.path === item.path }"
         @click="navigateTo(item)">
      <img class="nav-icon" :src="item.icon" alt="icon" />
      <span class="nav-label">{{ item.label }}</span>
    </div>
  </div>
</template>

<script>
import { useRouter } from 'vue-router'
import jhcon from '@/components/icons/Zeal7.png';
import jccon from '@/components/icons/LesserScarabUnique.png';
import jinengcon from '@/components/icons/Cleave.png';
import huashicon from '@/components/icons/PerfectFossil.png';
import fenchencon from '@/components/icons/CurrencyModValues.ico';

export default {
  name: 'MobileNavigation',
  setup() {
    const router = useRouter();
    
    const navItems = [
      {
        path: '/jinghua',
        name: 'jinghua',
        label: '精华',
        icon: jhcon,
      },
      {
        path: '/jiachong',
        name: 'jiachong',
        label: '圣甲虫',
        icon: jccon,
      },
      {
        path: '/jineng',
        name: 'jineng',
        label: '技能石',
        icon: jinengcon,
      },
      {
        path: '/huashi',
        name: 'huashi',
        label: '化石',
        icon: huashicon,
      },
      {
        path: '/fenchen',
        name: 'fenchen',
        label: '粉尘',
        icon: fenchencon,
      },
    ];
    
    const navigateTo = (item) => {
      router.push({ name: item.name });
    };
    
    return {
      navItems,
      navigateTo,
    };
  },
  computed: {
    isMobile() {
      return window.innerWidth <= 768;
    }
  },
  mounted() {
    window.addEventListener('resize', this.handleResize);
  },
  beforeUnmount() {
    window.removeEventListener('resize', this.handleResize);
  },
  methods: {
    handleResize() {
      this.$forceUpdate();
    }
  }
};
</script>

<style lang="less" scoped>
.mobile-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: var(--bg-secondary);
  border-top: 1px solid var(--border-light);
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding: var(--spacing-sm) 0;
  box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
  z-index: 1000;
}

.nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: var(--spacing-xs);
  border-radius: var(--border-radius-base);
  transition: var(--transition-fast);
  cursor: pointer;
  min-width: 60px;
  
  &:hover {
    background: var(--bg-tertiary);
  }
  
  &.active {
    background: var(--primary-color);
    color: white;
    
    .nav-icon {
      filter: brightness(0) invert(1);
    }
    
    .nav-label {
      color: white;
    }
  }
}

.nav-icon {
  width: 24px;
  height: 24px;
  margin-bottom: var(--spacing-xs);
  transition: var(--transition-fast);
}

.nav-label {
  font-size: var(--font-size-xs);
  font-weight: 500;
  color: var(--text-regular);
  transition: var(--transition-fast);
}

/* 桌面端隐藏 */
@media (min-width: 769px) {
  .mobile-nav {
    display: none;
  }
}
</style>
