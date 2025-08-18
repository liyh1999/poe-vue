<template>
    <el-header>
        <div class="l-content">
        </div>
        <div class="r-content">
            <el-dropdown>
                <span class="el-dropdown-link">
                    <img class="user" :src="getImgSrc()" alt="相关" />
                </span>
                <template #dropdown>
                    <el-dropdown-menu>
                        <el-dropdown-item >
                            <a href="https://qm.qq.com/q/kyipB6grio" target="_blank" rel="noopener noreferrer">
                            联系方式
                            </a>
                        </el-dropdown-item>
                        <el-dropdown-item >
                            <a href="https://gitee.com/hhzxxx/exilence-next-tx-release.git" target="_blank" rel="noopener noreferrer">
                             易刷数据库
                             </a>
                        </el-dropdown-item>
                        <el-dropdown-item >
                            <a href="https://price.filtereditor.cn/" target="_blank" rel="noopener noreferrer">
                             一乐物价榜
                             </a>
                        </el-dropdown-item>
                    </el-dropdown-menu>
                </template>
            </el-dropdown>
        </div>
    </el-header>
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
header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    background: #F0F4F9;
}
.l-content {
    display: flex;
    align-items: center;
    .el-button {
        margin-right: 16px;
        margin-left: 10px;
    }
    h3 {
        color: #fff;
    }
}
.r-content {
    .user {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        margin-right: 10px;
    }
}
</style>
