import { createRouter, createWebHashHistory } from 'vue-router'
const routes = [
    {
        path: '/',
        name: 'main',
        redirect: '/jinghua', // 添加重定向
        children: [
            {
                path: '/jinghua',
                name: 'jinghua',
                component: () => import('../views/精华.vue'),
            },
            {
                path: '/jiachong',
                name: 'jiachong',
                component: () => import('../views/甲虫.vue'),
            },
            {
                path: '/jineng',
                name: 'jineng',
                component: () => import('../views/技能石.vue'),
            },
            {
                path: '/huashi',
                name: 'huashi',
                component: () => import('../views/化石.vue'),
            },
             {
                path: '/fenchen',
                name: 'fenchen',
                component: () => import('../views/粉尘.vue'),
            },
        ]
    },
]
const router = createRouter({
    history: createWebHashHistory(),
    routes
})
export default router
