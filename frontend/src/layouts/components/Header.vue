<template>
    <nav>
      <div class="left-btn">
      <i @click="changeMenu" v-if="isHide" class="el-icon-s-unfold btn"></i>
      <i @click="changeMenu" v-else class="el-icon-s-fold btn"></i>
      </div>
      <div class="right-content">
      <el-switch v-model="isDark"></el-switch>
      <a href="#" class="notification">
        <el-badge :value="messages" class="item">
          <i class="el-icon-message-solid"></i>
        </el-badge>
      </a>
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
