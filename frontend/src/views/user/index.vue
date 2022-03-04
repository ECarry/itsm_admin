<template>
  <div>
    <Breadcrumb :title="title"/>
    <el-descriptions class="margin-top" :column="3" border>
      <template slot="extra">
        <el-button type="primary" size="small">操作</el-button>
      </template>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-user"></i>
          用户名
        </template>
        {{ userInfo.username }}
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-mobile-phone"></i>
          手机号
        </template>
        {{ userInfo.mobile }}
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-message"></i>
          邮箱
        </template>
        {{ userInfo.email }}
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-location-outline"></i>
          居住地
        </template>
        苏州市
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-tickets"></i>
          备注
        </template>
        <el-tag size="small">学校</el-tag>
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-office-building"></i>
          联系地址
        </template>
        江苏省苏州市吴中区吴中大道 1188 号
      </el-descriptions-item>
    </el-descriptions>
  </div>
</template>
<script>
import Breadcrumb from '@/components/Breadcrumb'
export default {
  name: 'User',
  components: {
    Breadcrumb
  },
  data () {
    return {
      userInfo: {
        name: '',
        username: '',
        email: '',
        mobile: ''
      },
      title: '用户信息'
    }
  },
  mounted () {
    // 获取用户数据
    this.$request
      .get('/user/detail/', {
        headers: {
          Authorization: 'Bearer ' + sessionStorage.access
        }
      })
      .then((response) => {
        console.log(response.data)
        this.userInfo = { ...response.data }
      })
  }
}
</script>
<style>
</style>
