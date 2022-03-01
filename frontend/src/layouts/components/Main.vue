<template>
    <div class="main">
      <div class="head-title">
        <h1>Dashboard</h1>
        <el-breadcrumb separator="/">
          <el-breadcrumb-item>Dashboard</el-breadcrumb-item>
          <el-breadcrumb-item>Home</el-breadcrumb-item>
        </el-breadcrumb>
      </div>
      <div class="app-main">
        <router-view/>
      </div>
    </div>
</template>
<script>
export default {
  name: 'Main'
}
</script>
<style>

</style>
