<template>
  <div>
  <el-descriptions title="用户信息">
    <el-descriptions-item label="姓名">{{ userInfo.name }}</el-descriptions-item>
    <el-descriptions-item label="用户名">{{ userInfo.username }}</el-descriptions-item>
    <el-descriptions-item label="手机号">{{ userInfo.mobile }}</el-descriptions-item>
    <el-descriptions-item label="邮箱">{{ userInfo.email }}</el-descriptions-item>
  </el-descriptions>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'User',
  data () {
    return {
      userInfo: {
        name: '',
        username: '',
        email: '',
        mobile: ''
      }
    }
  },
  methods: {
    getUserDetail () {
      axios.get('http://127.0.0.1:8000/user/detail/', {
        headers: {
          Authorization: 'Bearer ' + sessionStorage.access
        }
      }).then((response) => {
        console.log(response.data)
        this.userInfo = { ...response.data }
      })
    }
  },
  mounted () {
    this.getUserDetail()
  }
}
</script>
<style>
</style>
