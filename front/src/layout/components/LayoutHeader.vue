<template>
  <div class="layout-header">
    <div class="header-left">
      <h2 class="title">兰韵</h2>
    </div>
    <div class="header-right"></div>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped lang="less">
.layout-header {
  display: flex;
  width: 100vw;
  height: 60px;
  line-height: 60px;
  background-color: #986e99;
  box-shadow: 0 2px 8px rgba(0, 21, 41, 0.08);

  .header-left {
    .title {
      padding: 0 24px;
      color: #fff;
    }
  }
}
</style>
