<template>
  <LayoutHeader />
  <LayoutSider />
  <div class="layout-content">
    <RouterView />
  </div>
  <LayoutFooter />
</template>

<script setup lang="ts">
import LayoutHeader from '../components/LayoutHeader/LayoutHeader.vue'
import LayoutSider from '../components/LayoutSider/LayoutSider.vue'
import LayoutFooter from '../components/LayoutFooter/LayoutFooter.vue'
</script>

<style scoped></style>
