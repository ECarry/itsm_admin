import axios from 'axios'

const API_HOST = 'http://127.0.0.1:8000'

const instance = axios.create({
  baseURL: API_HOST,
  timeout: 1000
})

export default instance
