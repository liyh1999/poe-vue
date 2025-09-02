<template>
    <div class="header-container">
        <div class="header-left">
            <h1 class="app-title">POE 道具分析工具</h1>
        </div>
        <div class="header-right">
            <el-dropdown trigger="click" class="user-dropdown">
                <span class="user-avatar">
                    <img class="avatar-img" :src="getImgSrc()" alt="用户头像" />
                    <span class="user-name">工具</span>
                </span>
                <template #dropdown>
                    <el-dropdown-menu class="dropdown-menu">
                        <el-dropdown-item class="dropdown-item">
                            <a href="https://qm.qq.com/q/kyipB6grio" target="_blank" rel="noopener noreferrer">
                                <i class="el-icon-phone"></i>
                                联系方式
                            </a>
                        </el-dropdown-item>
                        <el-dropdown-item class="dropdown-item">
                            <a href="https://gitee.com/hhzxxx/exilence-next-tx-release.git" target="_blank" rel="noopener noreferrer">
                                <i class="el-icon-document"></i>
                                易刷数据库
                            </a>
                        </el-dropdown-item>
                        <el-dropdown-item class="dropdown-item">
                            <a href="https://price.filtereditor.cn/" target="_blank" rel="noopener noreferrer">
                                <i class="el-icon-data-line"></i>
                                一乐物价榜
                            </a>
                        </el-dropdown-item>
                    </el-dropdown-menu>
                </template>
            </el-dropdown>
        </div>
    </div>
</template>


<script>
export default {
    setup() {
        let getImgSrc = () => {

            return new URL("../components/icons/Chaos.png", import.meta.url).href;
        };
        return {
            getImgSrc,
        }
    }
}
</script>

<style lang="less" scoped>
.header-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    height: 100%;
    padding: 0 var(--spacing-lg);
    background: var(--bg-secondary);
}

.header-left {
    display: flex;
    align-items: center;
}

.app-title {
    margin: 0;
    font-size: var(--font-size-xl);
    font-weight: 600;
    color: var(--text-primary);
    background: linear-gradient(135deg, var(--primary-color), var(--primary-light));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.header-right {
    display: flex;
    align-items: center;
}

.user-dropdown {
    cursor: pointer;
}

.user-avatar {
    display: flex;
    align-items: center;
    padding: var(--spacing-sm) var(--spacing-md);
    border-radius: var(--border-radius-round);
    background: var(--bg-tertiary);
    transition: var(--transition-fast);
    
    &:hover {
        background: var(--primary-light);
        color: white;
        transform: translateY(-1px);
        box-shadow: var(--shadow-base);
    }
}

.avatar-img {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    margin-right: var(--spacing-sm);
    border: 2px solid var(--border-light);
    transition: var(--transition-fast);
}

.user-name {
    font-size: var(--font-size-sm);
    font-weight: 500;
    color: var(--text-primary);
}

.dropdown-menu {
    border-radius: var(--border-radius-large);
    box-shadow: var(--shadow-dark);
    border: 1px solid var(--border-light);
}

.dropdown-item {
    padding: var(--spacing-sm) var(--spacing-md);
    transition: var(--transition-fast);
    
    &:hover {
        background: var(--bg-tertiary);
    }
    
    a {
        display: flex;
        align-items: center;
        color: var(--text-primary);
        text-decoration: none;
        transition: var(--transition-fast);
        
        &:hover {
            color: var(--primary-color);
        }
        
        i {
            margin-right: var(--spacing-sm);
            font-size: var(--font-size-sm);
        }
    }
}

/* 响应式设计 */
@media (max-width: 768px) {
    .header-container {
        padding: 0 var(--spacing-md);
    }
    
    .app-title {
        font-size: var(--font-size-lg);
    }
    
    .user-name {
        display: none;
    }
    
    .avatar-img {
        width: 28px;
        height: 28px;
    }
}

@media (max-width: 480px) {
    .app-title {
        font-size: var(--font-size-base);
    }
    
    .header-container {
        padding: 0 var(--spacing-sm);
    }
}
</style>
