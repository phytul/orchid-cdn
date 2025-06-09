import { createRouter, createWebHistory } from 'vue-router'
import CdnSpace from '@/views/CdnSpace/CdnSpace.vue'
import LayoutDefault from '@/layout/LayoutDefault/LayoutDefault.vue'
import HomePage from '@/views/HomePage/HomePage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: LayoutDefault,
      children: [
        {
          path: '/',
          redirect: '/home',
        },
        {
          path: '/home',
          name: 'home',
          component: HomePage,
        },
        {
          path: '/cdn-space',
          name: 'cdn-space',
          component: CdnSpace,
        },
      ],
    },
  ],
})

export default router
