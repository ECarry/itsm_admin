<template>
  <div class="login-container">
    <div class="login-form">
      <!--      title-->
      <div class="title-container" >{{ title }}</div>
      <!--      INPUT FORM-->
        <Login v-if="showLogin" ref="title"/>
        <SignUp v-else ref="title"/>
<!--        <el-form-->
<!--          :model="ruleForm"-->
<!--          :rules="rules"-->
<!--          ref="ruleForm"-->
<!--          label-width="80px"-->
<!--          class="demo-ruleForm"-->
<!--        >-->
<!--          <el-form-item label="用户名" prop="username">-->
<!--            <el-input v-model="ruleForm.username"></el-input>-->
<!--          </el-form-item>-->

<!--          <el-form-item label="密码" prop="password">-->
<!--            <el-input-->
<!--              type="password"-->
<!--              v-model="ruleForm.password"-->
<!--            ></el-input>-->
<!--          </el-form-item>-->

<!--          <el-checkbox v-model="ruleForm.checked">记住我</el-checkbox>-->
<!--        </el-form>-->
      <!--        BUTTON-->
      <div class="button">
        <div class="button-content"></div>
        <button>{{ btnText }}</button>
      </div>
      <!--      TIP-->
      <div class="tip">
        <div v-if="showLogin">还没有账号? <span @click="changeLogin">点击注册</span></div>
        <div v-else>已有账号? <span @click="changeLogin">点击登录</span></div>
      </div>
    </div>
  </div>
</template>
<script>
import Login from '@/views/login/components/Login'
import SignUp from '@/views/login/components/SignUp'

export default {
  name: 'Index',
  data () {
    return {
      showLogin: true,
      title: 'Login',
      btnText: 'Login'
    }
  },
  components: {
    Login,
    SignUp
  },
  methods: {
    changeLogin () {
      this.showLogin = !this.showLogin
    }
  },
  updated () {
    this.title = this.$refs.title.title
    this.btnText = this.$refs.title.title
  }
  // data () {
  //   const validateUsername = (rule, value, callback) => {
  //     if (!value) {
  //       callback(new Error('请输入用户名'))
  //     } else if (value) {
  //       this.$request
  //         .get('http://127.0.0.1:8000/user/verify/username/' + value, {
  //           responseType: 'json'
  //         })
  //         .then((response) => {
  //           if (response.data.count === 0) {
  //             callback(new Error('用户名不存在'))
  //           } else {
  //             callback()
  //           }
  //         })
  //     }
  //   }
  //   return {
  //     ruleForm: {
  //       username: localStorage.username,
  //       password: '',
  //       checked: false
  //     },
  //     rules: {
  //       username: [
  //         { required: true, validator: validateUsername, trigger: 'blur' }
  //       ],
  //       password: [
  //         { required: true, message: '请输入密码', trigger: 'blur' },
  //         {
  //           min: 8,
  //           max: 32,
  //           message: '密码长度需要大于8个小于32个字符',
  //           trigger: 'blur'
  //         }
  //       ]
  //     }
  //   }
  // },
  // methods: {
  //   submitForm (formName) {
  //     this.$refs[formName].validate(valid => {
  //       if (valid) {
  //         // 登录
  //         this.$request
  //           .post('http://127.0.0.1:8000/user/login/', {
  //             username: this.ruleForm.username,
  //             password: this.ruleForm.password
  //           })
  //           .then((response) => {
  //             if (this.ruleForm.checked) {
  //               sessionStorage.clear()
  //               // 记住我，将返回的数据写入浏览器中的 localstorage
  //               localStorage.access = response.data.access
  //               localStorage.username = response.data.username
  //               this.$router.push('/user')
  //             } else {
  //               // 没记住，则写入 sessionStorage
  //               localStorage.clear()
  //               sessionStorage.access = response.data.access
  //               sessionStorage.usernmae = response.data.username
  //               this.$router.push('/user')
  //             }
  //             this.$message({
  //               type: 'success',
  //               message: '登录成功!'
  //             }
  //             )
  //           })
  //           .catch((error) => {
  //             console.log(error.response.data)
  //             this.$message({
  //               type: 'error',
  //               message: '密码错误!'
  //             })
  //           })
  //       } else {
  //         console.log('error submit!')
  //       }
  //     })
  //   }
  // }
}
</script>
<style>
.login-container {
  min-height: 100vh;
  min-width: 100vw;
  display: flex;
  align-items: center;
  justify-content: center;
  background-image: linear-gradient(135deg, #43cbef 10%, #9708cc 100%);
}

.login-container .login-form {
  background-color: #fff;
  max-width: 500px;
  width: 100%;
  padding: 20px 30px 30px 30px;
  border-radius: 25px;
  box-shadow: 0 5px 10px rgba(0,0,0,0.3);
}

.login-container .login-form .title-container {
  font-size: 32px;
  margin-bottom: 30px;
  font-weight: 500;
  position: relative;
}

.login-container .login-form .title-container::before {
  position: absolute;
  content: '';
  bottom: 0;
  left: 0;
  height: 3px;
  width: 32px;
  background: linear-gradient(135deg, #43cbef 10%, #9708cc 100%);
}

.login-container .login-form .form-input {
  margin: 10px  20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.login-container .login-form .form-input .input {
  width: 100%;
  line-height: 40px;
  margin: 10px auto;

}

.login-container .login-form .form-input .input label {
  font-size: 16px;
}

.login-container .login-form .form-input .input .text {
  width: 100%;
  height: 40px;
  padding: 10px 20px;
  outline: none;
  border-radius: 25px;
  border: 1px solid #43cbef;
}

.login-container .login-form .form-input .input .text:focus {
  border: 2px solid #9708cc;
}

.login-container .login-form .form-input .input .checkbox {
  margin-right: 10px;
}

.login-container .login-form .tip {
  margin-top: 20px;
}

.login-container .login-form .tip span:hover{
  color: #43cbef;
  cursor: pointer;
}

.login-container .login-form .button{
  position: relative;
  width: 100%;
  height: 50px;
  margin-top: 30px;
  border-radius: 25px;
  overflow: hidden;
}

.login-container .login-form .button .button-content{
  position: absolute;
  height: 100%;
  width: 300%;
  left: -100%;
  background-image: linear-gradient(135deg, #43cbef 10%, #9708cc 100%);
  border-radius: 25px;
}

.login-container .login-form .button:hover .button-content{
  left: 0;
}

.login-container .login-form .button button{
  position: relative;
  height: 100%;
  width: 100%;
  background: none;
  outline: none;
  border: none;
  font-size: 18px;
  letter-spacing: 1px;
  color: #fff;
}

.login-container .login-form .button button:hover{
  cursor: pointer;
}
</style>
