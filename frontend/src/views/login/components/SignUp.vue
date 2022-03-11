<template>
    <div class="signup-form">
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
            <el-input v-model="ruleForm.verifyCode"></el-input>
            <el-button @click="handleSendVerifyCode" style="margin-top: 10px">获取验证码</el-button>
          </el-form-item>
          <!--        BUTTON-->
          <div class="button">
            <div class="button-content"></div>
            <button @click="submitForm('ruleForm')">Signup</button>
          </div>
        </el-form>
      </div>
    </div>
</template>

<script>
export default {
  name: 'SignUp',
  data () {
    const validateUsername = (rule, value, callback) => {
      if (!value) {
        callback(new Error('请输入用户名'))
      } else if (value) {
        this.$request
          .get('/user/verify/username/' + value, { responseType: 'json' })
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

    const validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        console.log('validatePass callback')
        callback()
      }
    }

    const validatePass2 = (rule, value, callback) => {
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
    const validateEmail = (rule, value, callback) => {
      if (value) {
        this.$request
          .get('/user/verify/email/' + value, {
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

    const validateVerifyCode = (rule, value, callback) => {
      if (!value) {
        callback(new Error('请输入验证码'))
      } else {
        console.log('validateVerifyCode callback')
        callback()
      }
    }

    return {
      title: 'Signup',
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
          this.$request
            .post('/user/create/', {
              username: this.ruleForm.username,
              email: this.ruleForm.email,
              password: this.ruleForm.password,
              checkPass: this.ruleForm.checkPass,
              verifyCode: this.ruleForm.verifyCode
            })
            .then((response) => {
              // 将返回的数据存到 localstorage
              sessionStorage.clear()
              localStorage.clear()
              localStorage.id = response.data.id
              localStorage.username = response.data.username
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
        this.$message({
          type: 'error',
          message: '请输入邮箱!'
        })
        return false
      }
      this.$request
        .get('/email/verify/' + this.ruleForm.email, {
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
