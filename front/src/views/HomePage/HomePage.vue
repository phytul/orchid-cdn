<template>
  <div class="home-page">
    <div class="welcome-message">
      <p class="title-zh">Orchid CDN</p>
      <p class="message-desc">Help designers/developers managing resources easily</p>
    </div>
    <div class="action-buttons">
      <el-button type="primary" @click="handleGetStarted">Get Started</el-button>
      <el-button @click="handleLearnMore">Learn More</el-button>
    </div>
    <div class="home-main">
      <div class="dash-board">
        <el-card class="db-card">
          <el-row>
            <el-col :span="6">
              <el-statistic title="Daily active users" :value="268500" />
            </el-col>
            <el-col :span="6">
              <el-statistic title="Total Transactions" :value="9292" />
            </el-col>
            <el-col :span="6">
              <el-statistic title="Server Status" value="Close" />
            </el-col>
            <el-col :span="6">
              <el-statistic title="Memory usage" value="1.2 / 3 T" />
            </el-col>
          </el-row>
        </el-card>
      </div>
      <div class="desc-container">
        <el-card v-for="(item, index) in descCardList" :key="index" class="desc-card">
          <div class="card-content">
            <p class="title">{{ item.title }}</p>
            <p class="description">
              {{ item.description }}
            </p>
          </div>
        </el-card>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ElMessage } from 'element-plus'

const descCardList = [
  {
    title: "What's a CDN?",
    description: `
      CDN (Content Delivery Network) is a globally distributed network of servers designed to
      deliver internet content—such as web pages, images, videos, and other static or dynamic
      files—more efficiently to users.
    `,
  },
  {
    title: "Why're we here",
    description: `
      We are here to provide a seamless and efficient content delivery experience for users
      worldwide, ensuring high availability and performance.
    `,
  },
  {
    title: 'Our Mission',
    description: `
      Our mission is to empower developers and organizations by providing a reliable and
      scalable CDN solution that enhances the performance of their applications.
    `,
  },
]

/**
 * Handle the "Get Started" button click event.
 */
const handleGetStarted = () => {
  ElMessage({
    type: 'info',
    message: '敬请期待',
  })
}

/**
 * Handle the "Learn More" button click event.
 */
const handleLearnMore = () => {
  ElMessage({
    type: 'info',
    message: '敬请期待',
  })
}
</script>

<style scoped lang="less">
.home-page {
  display: flex;
  width: 100%;
  margin: 0 auto;
  padding: 0 32px;
  flex-direction: column;
  align-items: center;
  gap: 32px;

  .welcome-message {
    display: flex;
    align-items: center;
    flex-direction: column;
    font-weight: bold;
    gap: 12px;

    p {
      margin: 0;
      color: #986e99;
    }

    .title-zh {
      padding-top: 48px;
      font-size: 60px;
      font-weight: 900;
    }

    .message-desc {
      font-size: 16px;
      font-weight: normal;
      color: #666;
    }
  }

  .action-buttons {
    display: flex;
    gap: 12px;
    justify-content: center;
  }

  .home-main {
    display: flex;
    flex-direction: column;
    gap: 24px;

    .desc-container {
      display: flex;
      justify-content: center;
      gap: 24px;

      .desc-card {
        flex: 1;
        max-width: 320px;

        &:hover {
          transform: scale(1.02);
        }

        p {
          margin: 0;

          &.title {
            font-size: 16px;
            font-weight: bold;
            color: #333;
            padding-bottom: 8px;
          }

          &.description {
            font-size: 14px;
            color: #666;
          }
        }
      }
    }

    .dash-board {
      flex: 1;

      .db-card {
        &:hover {
          transform: scale(1.02);
        }
      }
    }

    .el-col {
      text-align: center;
    }
  }
}
</style>
