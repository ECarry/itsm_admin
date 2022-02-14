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

          <el-form-item label="密码" prop="pass">
            <el-input
              type="password"
              v-model="ruleForm.pass"
              autocomplete="off"
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
export default {
  name: 'Login',
  data () {
    return {
      ruleForm: {
        email: '',
        pass: ''
      },
      rules: {
        email: [
          { required: true, message: '请输入邮箱地址', trigger: 'blur' },
          {
            type: 'email',
            message: '请输入正确的邮箱地址',
            trigger: ['change']
          }
        ],
        pass: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          {
            min: 8,
            max: 32,
            message: '长度大于 8 小于32个字符',
            trigger: 'blur'
          }
        ]
      }
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.$router.push('/')
        } else {
          console.log('error submit!!')
          return false
        }
      })
    }
  }
}
</script>
<style>
</style>
