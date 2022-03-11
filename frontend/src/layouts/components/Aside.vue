<template>
 <div>
   <!--   LOGO  -->
   <div class="logo">
     <a href="#">
       <i class="el-icon-sunset"></i>
       <span class="text">ECarry</span>
     </a>
   </div>
   <div class="menu">
     <!--   TOP MENU-->
     <ul class="menu top">
       <li >
         <router-link to="/">
           <a href="#">
             <i class="el-icon-menu"></i>
             <span>Dashboard</span>
           </a>
         </router-link>
       </li>
       <li >
         <a href="#">
           <i class="el-icon-goods"></i>
           <span>采购管理</span>
         </a>
       </li>
       <li >
         <router-link to="/contract">
           <a href="#">
             <i class="el-icon-s-order"></i>
             <span>项目管理</span>
           </a>
         </router-link>
       </li>
       <li >
         <router-link to="/server">
           <a href="#">
             <i class="el-icon-s-platform"></i>
             <span>设备管理</span>
           </a>
         </router-link>
       </li>
       <li >
         <router-link to="/spare">
           <a href="#">
             <i class="el-icon-cpu"></i>
             <span>备件管理</span>
           </a>
         </router-link>
       </li>
       <li >
         <router-link to="/user">
           <a href="#">
             <i class="el-icon-s-custom"></i>
             <span>个人中心</span>
           </a>
         </router-link>
       </li>
     </ul>
     <!--    BOTTOM MENU-->
     <ul class="menu">
       <li>
         <a href="#">
           <i class="el-icon-setting"></i>
           <span>设置中心</span>
         </a>
       </li>
       <li>
         <router-link to="/login">
           <a href="#" class="logout">
             <i class="el-icon-switch-button"></i>
             <span>退出登录</span>
           </a>
         </router-link>
       </li>
     </ul>
   </div>
 </div>
</template>
<script>
export default {
  name: 'Aside',
  data () {
    return {
      isActive: ''
    }
  }
}
</script>
<style scoped>

</style>
