<template>
    <div class="sidebar-background">
    <el-menu class="el-menu-vertical-demo" 
              :style="{ backgroundColor: '#F0F4F9' }" 
              text-color="#66ccff"   
              :collapse-transition="false" 
              active-text-color="#ffd04b">
        <el-menu-item :index="item.path+''" v-for="item in list" :key="item.label" @click="handleClick(item)">
            <img class="icons" :src="item.icon" alt="icon" /> 
            <span class="label-text">{{item.label}}</span>
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
                path: '/jineg',
                name: 'jineng',
                label: '技能石',
                icon: jinengcon,
                url: '/jieng'
            },
            {
                path: '/huashi',
                name: 'huashi',
                label: '化石',
                icon: huashicon,
                url: '/huashi'
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
.icons {
    width: 30%;
    height: 30px;
    margin-right: 20px;
}
.el-menu-vertical-demo {
    width: 100%;
    border-right: none;
    h3 {
        color: #fff;
        text-align: center;
        margin-top: 20px;
    }
}
.label-text {
    font-size: 20px;
}
.sidebar-background {
    background-color: #EFF4F9; /* 侧边栏背景颜色 */
    height: 100vh; /* 设置为全高 */
    padding: 10px; /* 可选，设置内边距 */
}
</style>
