<template>
  <div class="login-container">
    <div class="login-form">
      <div class="title-container">Login</div>

      <div class="form-input">
        <el-form
          :model="ruleForm"
          :rules="rules"
          ref="ruleForm"
          label-width="100px"
          class="demo-ruleForm"
        >
          <el-form-item label="邮箱" prop="email">
            <el-input v-model="ruleForm.email"></el-input>
          </el-form-item>

          <el-form-item label="密码" prop="password">
            <el-input
              type="password"
              v-model="ruleForm.password"
            ></el-input>
          </el-form-item>

          <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')"
              >登录</el-button
            >
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "Login",
  data() {
    var validateEmail = (rule, value, callback) => {
      axios
        .get("http://127.0.0.1:8000/user/verify/email/" + this.ruleForm.email, {
          responseType: "json",
        })
        .then((response) => {
          if (response.data.count === 0) {
            callback(new Error("邮箱不存在！"));
          }
        });
    };
    return {
      ruleForm: {
        email: "",
        password: "",
      },
      rules: {
        email: [
          { required: true, message: "请输入邮箱地址", trigger: "blur" },
          {
            type: "email",
            message: "请输入正确的邮箱地址",
            trigger: ["change", "blur"],
          },
          { validator: validateEmail, trigger: "blur" },
        ],
        password: [
          { required: true, message: "请输入密码", trigger: "blur" },
          {
            min: 8,
            max: 32,
            message: "长度大于 8 小于32个字符",
            trigger: "blur",
          },
        ],
      },
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          // 登录
          axios
            .post("login", {
              email: this.ruleForm.email,
              password: this.ruleForm.password,
            })
            .then((response) => {
              console.log(response.data);
              this.$router.push("/");
            })
            .catch((error) => {
              console.log(error.response.data);
            });
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
  },
};
</script>
<style>
</style>
