<template>
  <div class="login-container">
    <div class="login-form">
      <!--      title-->
      <div class="title-container" >{{ title }}</div>
      <!--      INPUT FORM-->
        <Login v-if="showLogin" ref="ruleForm"/>
        <SignUp v-else ref="ruleForm"/>

      <!--      TIP-->
      <div class="tip">
        <div v-if="showLogin">还没有账号? <span @click="changeLogin">点击注册</span></div>
        <div v-else>已有账号? <span @click="changeLogin">点击登录</span></div>
      </div>
    </div>
  </div>
</template>
<script>
import Login from '@/views/login/components/Login'
import SignUp from '@/views/login/components/SignUp'

export default {
  name: 'Index',
  data () {
    return {
      showLogin: true,
      title: 'Login',
      btnText: 'Login'
    }
  },
  components: {
    Login,
    SignUp
  },
  methods: {
    changeLogin () {
      this.showLogin = !this.showLogin
    }
  },
  updated () {
    this.title = this.$refs.ruleForm.title
    this.btnText = this.$refs.ruleForm.title
  }
}
</script>
<style>

</style>
