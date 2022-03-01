<template>
  <div class="container">
    <!-- SIDEBAR -->
    <section id="sidebar" :class="{hide:isHide}">
      <Aside/>
    </section>
    <!-- SIDEBAR -->

    <!--    CONTENT-->
    <section id="content">
      <Header :isHide="isHide" @changHide="changeHide" class="header"/>
      <Main/>
    </section>
    <!--    CONTENT-->
  </div>
</template>
<script>
import Aside from './components/Aside.vue'
import Header from './components/Header.vue'
import Main from './components/Main.vue'

export default {
  name: 'Home',
  data () {
    return {
      isHide: false
    }
  },
  components: {
    Aside,
    Header,
    Main
  },
  methods: {
    changeHide () {
      this.isHide = !this.isHide
    }
  }
}
</script>
<style>

</style>
