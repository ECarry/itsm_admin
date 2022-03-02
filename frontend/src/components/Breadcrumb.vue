<template>
  <div class="head-title">
    <h1>{{title}}</h1>
    <el-breadcrumb separator="/">
      <el-breadcrumb-item to="/">Dashboard</el-breadcrumb-item>
      <el-breadcrumb-item>{{title}}</el-breadcrumb-item>
    </el-breadcrumb>
  </div>
</template>

<script>
export default {
  name: 'Breadcrumb',
  props: {
    title: {
      type: String,
      default: 'Dashboard'
    }
  }
}
</script>

<style scoped>

</style>
