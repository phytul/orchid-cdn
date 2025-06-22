import { createRouter, createWebHistory } from 'vue-router'
import CdnSpace from '@/views/CdnSpace/CdnSpace.vue'
import DefaultLayout from '@/layout/DefaultLayout.vue'
import HomePage from '@/views/HomePage/HomePage.vue'
import PublicResource from '@/views/PublicResource/PublicResource.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: DefaultLayout,
      // props: { hiddenMenus: true },
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
        {
          path: '/public-resource',
          name: 'public-resource',
          component: PublicResource,
        },
      ],
    },
  ],
})

export default router
