<template>
  <div class="base-menus">
    <ul class="menus-list">
      <li v-for="(item, index) in list" :key="index">
        <router-link :to="item.link || '#'" active-class="current">{{ item.title }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
type MenusList = {
  title: string
  icon?: string
  link?: string
  // children?: MenusList[]
}[]

type Props = {
  list?: MenusList
}

const props = defineProps<Props>()

const { list } = props
</script>
<style scoped lang="less">
.base-menus {
  .menus-list {
    padding: 16px 12px;

    a {
      display: block;
      padding: 8px 16px;
      border-radius: 8px;
      font-weight: bold;
      color: #654b66;

      &.current {
        background-color: rgba(203, 147, 200, 0.3);
        color: #986e99;
        font-weight: bold;
      }
    }
  }
}
</style>
