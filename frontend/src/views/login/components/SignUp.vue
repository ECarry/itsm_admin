<template>
  <div class="signup-container">
    <div class="signup-form">
      <div class="title-container">SignUp</div>

      <div class="form-input">
        <el-form
          :model="ruleForm"
          :rules="rules"
          ref="ruleForm"
          label-width="100px"
          class="demo-ruleForm"
        >
          <el-form-item label="用户名" prop="username">
            <el-input type="text" v-model="ruleForm.username"></el-input>
          </el-form-item>

          <el-form-item label="密码" prop="password">
            <el-input
              type="password"
              v-model="ruleForm.password"
            ></el-input>
          </el-form-item>

          <el-form-item label="重复密码" prop="checkPass">
            <el-input
              type="password"
              v-model="ruleForm.checkPass"
            ></el-input>
          </el-form-item>

          <el-form-item label="企业邮箱" prop="email">
            <el-input v-model="ruleForm.email"></el-input>
          </el-form-item>

          <el-form-item label="验证码" prop="verifyCode">
            <el-input v-model="ruleForm.verifyCode"></el-input
            ><el-button @click="handleSendVerifyCode">获取验证码</el-button>
          </el-form-item>

          <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')"
              >注册</el-button
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
  name: 'SignUp',
  data () {
    var validateUsername = (rule, value, callback) => {
      if (!value) {
        callback(new Error('请输入用户名'))
      } else if (value) {
        axios.get('http://127.0.0.1:8000/user/verify/username/' + value, { responseType: 'json' })
          .then((response) => {
            if (response.data.count === 1) {
              callback(new Error('用户名已存在'))
            } else {
              console.log('validateUsername callback')
              callback()
            }
          })
      }
    }

    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        console.log('validatePass callback')
        callback()
      }
    }

    var validatePass2 = (rule, value, callback) => {
      if (!value) {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.ruleForm.password) {
        callback(new Error('两次输入密码不一致'))
      } else {
        console.log('validatePass2 callback')
        callback()
      }
    }
    // 自定义邮箱验证邮箱是否注册
    var validateEmail = (rule, value, callback) => {
      if (value) {
        axios
          .get('http://127.0.0.1:8000/user/verify/email/' + value, {
            responseType: 'json'
          })
          .then((response) => {
            if (response.data.count === 1) {
              callback(new Error('邮箱已存在'))
            } else {
              console.log('validateEmail callback')
              callback()
            }
          })
      }
    }

    var validateVerifyCode = (rule, value, callback) => {
      if (!value) {
        callback(new Error('请输入验证码'))
      } else {
        console.log('validateVerifyCode callback')
        callback()
      }
    }

    return {
      ruleForm: {
        username: '',
        email: '',
        password: '',
        checkPass: '',
        verifyCode: ''
      },
      rules: {
        username: [
          { required: true, validator: validateUsername, trigger: 'blur' }
        ],
        email: [
          {
            required: true,
            type: 'email',
            message: '请输入正确的邮箱地址',
            trigger: ['change', 'blur']
          },
          { validator: validateEmail, trigger: 'blur' }
        ],
        password: [
          { min: 8, max: 32, message: '密码长度需要大于8个小于32个字符', trigger: 'blur' },
          { required: true, validator: validatePass, trigger: 'blur' }
        ],
        checkPass: [
          { required: true, validator: validatePass2, trigger: 'blur' }
        ],
        verifyCode: [
          { required: true, validator: validateVerifyCode, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          axios
            .post('http://127.0.0.1:8000/user/create/', {
              username: this.ruleForm.username,
              email: this.ruleForm.email,
              password: this.ruleForm.password,
              checkPass: this.ruleForm.checkPass,
              verifyCode: this.ruleForm.verifyCode
            })
            .then((response) => {
              this.$router.push('/login')
            })
            .catch((error) => {
              console.log(error.response.data)
            })
        } else {
          console.log(valid)
        }
      })
    },
    handleSendVerifyCode () {
      if (!this.ruleForm.email) {
        return false
      }
      axios
        .get(`http://127.0.0.1:8000/email/verify/${this.ruleForm.email}`, {
          responseType: 'json'
        })
        .then((response) => {
          console.log(response.data)
        })
    }
  }
}
</script>

<style scoped>
.title-container {
  font-size: 32px;
}
</style>
