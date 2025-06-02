import { createRouter, createWebHistory } from 'vue-router'
import CdnSpace from '../views/CdnSpace/CdnSpace.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'cdn-space',
      component: CdnSpace,
    },
  ],
})

export default router
