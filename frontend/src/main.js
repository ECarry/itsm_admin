import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
import './style/reset.css'
import './style/style.css'
import 'element-ui/lib/theme-chalk/index.css'
import axiosInstance from './utils/request'

Vue.config.productionTip = false
Vue.prototype.$request = axiosInstance

Vue.use(ElementUI)

// eslint-disable-next-line no-new
new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
