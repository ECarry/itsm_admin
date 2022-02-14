<template>
  <div>
    <el-menu
      default-active="1-4-1"
      class="el-menu-vertical-demo"
      :collapse="isCollapse"
      router
    >
      <div class="logo-container">
        <div class="logo">
          <i class="el-icon-eleme"></i>
          <div class="logo-name">ITSM</div>
        </div>
        <i id="btn" class="el-icon-s-unfold" @click="handleCollapse"></i>
      </div>

      <el-menu-item index="/">
        <i class="el-icon-menu"></i>
        <span slot="title">DashBoard</span>
      </el-menu-item>

      <el-submenu>
        <template slot="title">
          <i class="el-icon-shopping-cart-full"></i>
          <span slot="title">合同管理</span>
        </template>
        <el-menu-item index="/contract">所有合同</el-menu-item>
        <el-menu-item index="/server">维保设备</el-menu-item>
      </el-submenu>

      <el-submenu>
        <template slot="title">
          <i class="el-icon-cpu"></i>
          <span slot="title">备件管理</span>
        </template>
        <el-menu-item index="/product">型号管理</el-menu-item>
        <el-menu-item index="/spare">所有备件</el-menu-item>
      </el-submenu>

      <el-submenu>
        <template slot="title">
          <i class="el-icon-s-custom"></i>
          <span slot="title">个人中心</span>
        </template>
        <el-menu-item>我的信息</el-menu-item>
      </el-submenu>
    </el-menu>
  </div>
</template>
<script>
export default {
  name: "Aside",
  data() {
    return {
      isCollapse: false,
    };
  },
  methods: {
    handleCollapse() {
      console.log("click");
      this.isCollapse = !this.isCollapse;
    },
  },
};
</script>
<style>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
.logo-container .logo {
  display: flex;
  height: 50px;
  width: 100%;
  align-items: center;
}

.logo-container .logo i {
  font-size: 28px;
  margin-right: 5px;
}

.logo-container .logo .logo-name {
  font-size: 20px;
}

.logo-container #btn {
  position: absolute;
  top: 6px;
  font-size: 20px;
  text-align: center;
  left: 150px;
}
</style>