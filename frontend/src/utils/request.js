import axios from 'axios'

const API_HOST = 'http://127.0.0.1:8000'

const token = sessionStorage.getItem('access') ? sessionStorage.getItem('access') : localStorage.getItem('access')

const instance = axios.create({
  baseURL: API_HOST,
  timeout: 3000,
  headers: {
    Authorization: 'Bearer ' + token
  }
})

export default instance
