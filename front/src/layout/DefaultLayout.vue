<template>
  <LayoutHeader />
  <div class="layout-container">
    <div class="layout-sider" v-if="!hiddenMenus">
      <LayoutSider>
        <BaseMenus :list="menus" />
      </LayoutSider>
    </div>
    <div class="layout-main">
      <RouterView />
      <LayoutFooter />
    </div>
  </div>
</template>

<script setup lang="ts">
import LayoutHeader from './components/LayoutHeader.vue'
import LayoutSider from './components/LayoutSider.vue'
import LayoutFooter from './components/LayoutFooter.vue'
import BaseMenus from '@/components/BaseMenus.vue'

type Props = {
  hiddenMenus?: boolean
}

const props = defineProps<Props>()

const { hiddenMenus } = props

const menus = [
  { title: '主页', link: '/home' },
  { title: '个人空间', link: '/cdn-space' },
  { title: '公共资源', link: '/public-resource' },
]
</script>

<style scoped lang="less">
.layout-container {
  display: flex;

  .layout-sider {
    height: calc(100vh - 60px);
    flex-shrink: 0;
    width: 200px;
  }

  .layout-main {
    box-sizing: border-box;
    height: calc(100vh - 60px);
    padding: 24px;
    box-sizing: border-box;
    flex-grow: 1;
    overflow-y: auto;
    box-shadow: 0 0 10px inset #654b667b;
  }
}
</style>
