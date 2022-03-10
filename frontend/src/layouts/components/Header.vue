<template>
    <nav>
      <div class="left-btn">
      <i @click="changeMenu" v-if="isHide" class="el-icon-s-unfold btn"></i>
      <i @click="changeMenu" v-else class="el-icon-s-fold btn"></i>
      </div>
      <div class="right-content">
      <el-switch v-model="isDark"></el-switch>
      <!--        消息弹窗-->
      <el-popover
        placement="bottom-end"
        title="通知"
        width="500"
        trigger="click"
        >
        <el-button slot="reference" style="border: none; background: none">
          <a href="#" class="notification">
            <el-badge :value="messages" class="item">
              <i style="color: var(--blue)" class="el-icon-message-solid"></i>
            </el-badge>
          </a>
        </el-button>
        <div class="header-message">
          <img src="@/assets/nothing.png" alt="">
          <span>暂无消息</span>
        </div>
      </el-popover>
      <a href="#" class="profile">
        <img src="../../assets/people.jpg" alt="">
      </a>
      </div>
    </nav>
</template>
<script>
export default {
  name: 'Header',
  props: ['isHide'],
  data () {
    return {
      isDark: false,
      messages: 12
    }
  },
  methods: {
    changeMenu () {
      // 点击切换按钮,改变父组件属性 isHide
      this.$emit('changHide')
    }
  }
}
</script>
<style>
</style>
