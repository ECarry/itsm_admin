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
          <el-form-item label="用户名" prop="username">
            <el-input v-model="ruleForm.username"></el-input>
          </el-form-item>

          <el-form-item label="密码" prop="password">
            <el-input
              type="password"
              v-model="ruleForm.password"
            ></el-input>
          </el-form-item>

          <el-checkbox v-model="ruleForm.checked">记住我</el-checkbox>

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
import axios from 'axios'

export default {
  name: 'Login',
  data () {
    var validateUsername = (rule, value, callback) => {
      if (!value) {
        callback(new Error('请输入用户名'))
      } else if (value) {
        axios
          .get('http://127.0.0.1:8000/user/verify/username/' + value, {
            responseType: 'json'
          })
          .then((response) => {
            if (response.data.count === 0) {
              callback(new Error('用户名不存在'))
            } else {
              callback()
            }
          })
      }
    }
    return {
      ruleForm: {
        username: localStorage.username,
        password: '',
        checked: false
      },
      rules: {
        username: [
          { required: true, validator: validateUsername, trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          {
            min: 8,
            max: 32,
            message: '密码长度需要大于8个小于32个字符',
            trigger: 'blur'
          }
        ]
      }
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          // 登录
          axios
            .post('http://127.0.0.1:8000/user/login/', {
              username: this.ruleForm.username,
              password: this.ruleForm.password
            })
            .then((response) => {
              if (this.ruleForm.checked) {
                sessionStorage.clear()
                // 记住我，将返回的数据写入浏览器中的 localstorage
                localStorage.access = response.data.access
                localStorage.username = response.data.username
              } else {
                // 没记住，则写入 sessionStorage
                localStorage.clear()
                sessionStorage.access = response.data.access
                sessionStorage.usernmae = response.data.username
              }
              // this.$router.push('/')
            })
            .catch((error) => {
              console.log(error.response.data)
            })
        } else {
          console.log('error submit!')
        }
      })
    }
  }
}
</script>
<style>
.login-container {
  display: flex;
  align-items: center;
  justify-content: center;
}
.form-input {
  margin: 10px  20px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.demo-ruleForm {
  margin: 5px;
  justify-content: center;
  align-items: center;
}
</style>
