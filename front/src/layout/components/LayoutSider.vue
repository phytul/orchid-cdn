<template>
  <div class="layout-sider">
    <slot />
  </div>
</template>

<script setup lang="ts"></script>

<style scoped lang="less">
.layout-sider {
  height: 100%;
  width: 200px;
  background-color: #ffedec;
  position: fixed;
}
</style>
