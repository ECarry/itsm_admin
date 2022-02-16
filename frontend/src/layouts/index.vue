<template>
  <el-container>
    <el-aside width="210px">
        <Aside/>
    </el-aside>
    <el-container>
      <el-header>
          <Header/>
      </el-header>
      <el-main>
          <Main/>
      </el-main>
    </el-container>
  </el-container>
</template>
<script>
import Aside from './components/Aside.vue'
import Header from './components/Header.vue'
import Main from './components/Main.vue'

export default {
  name: 'Home',
  components: {
    Aside,
    Header,
    Main
  }
}
</script>
<style>
</style>
