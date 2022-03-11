<template>
  <div class="form-input">
    <div class="input">
      <label>用户名:</label>
      <input type="text" class="text" v-model="username">
    </div>

    <div class="input">
      <label>密码:</label>
      <input type="password" class="text" v-model="password">
    </div>

    <div class="input">
      <input type="checkbox" class="checkbox" v-model="checked">
      <label>记住我</label>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      title: 'Login',
      username: '',
      password: '',
      checked: false
    }
  }
}
</script>

<style scoped>

</style>
