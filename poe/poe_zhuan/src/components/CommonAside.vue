<template>
    <div class="sidebar-container">
        <div class="sidebar-header">
            <h3 class="sidebar-title">POE工具</h3>
        </div>
        <el-menu 
            class="sidebar-menu" 
            :default-active="$route.path"
            background-color="transparent"
            text-color="var(--text-regular)"   
            :collapse-transition="false" 
            active-text-color="var(--primary-color)"
            router>
            <el-menu-item 
                :index="item.path" 
                v-for="item in list" 
                :key="item.label" 
                @click="handleClick(item)"
                class="menu-item">
                <img class="menu-icon" :src="item.icon" alt="icon" /> 
                <span class="menu-text">{{item.label}}</span>
            </el-menu-item>
        </el-menu>
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
    setup() {
        const list = [
            {
                path: '/jinghua',
                name: 'jinghua',
                label: '精华',
                icon: jhcon,
                url: '/jinghua'
            },

            {
                path: '/jiachong',
                name: 'jiachong',
                label: '圣甲虫',
                icon: jccon,
                url: '/jiachong'
            },
            {
                path: '/jineng',
                name: 'jineng',
                label: '技能石',
                icon: jinengcon,
                url: '/jineng'
            },
            {
                path: '/huashi',
                name: 'huashi',
                label: '化石',
                icon: huashicon,
                url: '/huashi'
            },
            {
                path: '/fenchen',
                name: 'fenchen',
                label: '粉尘',
                icon: fenchencon,
                url: '/fenchen'
            },

        ];
        const router = useRouter()  // 这是Vue3中使用router的方法，跟Vue2不太一样，需要注意一下
        const handleClick = (item) => {
            console.log(item.name)
            router.push({
                name: item.name
            });
        }
        return {
            list,
            handleClick,
        }
    }
}
</script>

<style lang="less" scoped>
.sidebar-container {
    height: 100vh;
    background: var(--bg-secondary);
    display: flex;
    flex-direction: column;
}

.sidebar-header {
    padding: var(--spacing-lg);
    border-bottom: 1px solid var(--border-light);
    text-align: center;
}

.sidebar-title {
    margin: 0;
    font-size: var(--font-size-xl);
    font-weight: 600;
    color: var(--text-primary);
    background: linear-gradient(135deg, var(--primary-color), var(--primary-light));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.sidebar-menu {
    flex: 1;
    border-right: none;
    padding: var(--spacing-md) 0;
}

.menu-item {
    margin: var(--spacing-xs) var(--spacing-md);
    border-radius: var(--border-radius-base);
    transition: var(--transition-fast);
    
    &:hover {
        background-color: var(--bg-tertiary);
        transform: translateX(4px);
    }
    
    &.is-active {
        background: linear-gradient(135deg, var(--primary-color), var(--primary-light));
        color: white;
        
        .menu-icon {
            filter: brightness(0) invert(1);
        }
    }
}

.menu-icon {
    width: 24px;
    height: 24px;
    margin-right: var(--spacing-md);
    transition: var(--transition-fast);
}

.menu-text {
    font-size: var(--font-size-base);
    font-weight: 500;
    transition: var(--transition-fast);
}

/* 响应式设计 */
@media (max-width: 768px) {
    .sidebar-container {
        display: none;
    }
}
</style>
