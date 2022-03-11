<template>
  <el-dialog :title="dialogTitle"
             width="600px"
             :visible.sync="dialogFormVisible"
             :before-close="handleClose">
    <el-form :model="form" :rules="rules" ref="form" status-icon>
      <el-form-item label="合同编号" :label-width="formLabelWidth" prop="contract_num">
        <el-input v-model="form.contract_num" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="签订时间" :label-width="formLabelWidth" prop="contract_date">
        <el-date-picker placeholder="选择日期"
                        v-model="form.contract_date"
                        type="date"
                        style="width: 100%;"
                        format="yyyy-MM-dd"
                        value-format="yyyy-MM-dd"
        ></el-date-picker>
      </el-form-item>
      <el-form-item label="项目编号" :label-width="formLabelWidth" prop="project_num">
        <el-input v-model="form.project_num" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="开工时间" :label-width="formLabelWidth" prop="start_date">
        <el-date-picker placeholder="选择日期"
                        v-model="form.start_date"
                        type="date"
                        style="width: 100%;"
                        format="yyyy-MM-dd"
                        value-format="yyyy-MM-dd"
        ></el-date-picker>
      </el-form-item>
      <el-form-item label="区域" :label-width="formLabelWidth" prop="area">
        <el-input v-model="form.area" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="合同名称" :label-width="formLabelWidth" prop="contract_name">
        <el-input v-model="form.contract_name" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="客户名称" :label-width="formLabelWidth" prop="custom">
        <el-input v-model="form.custom" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="结束时间" :label-width="formLabelWidth" prop="end_date">
        <el-date-picker placeholder="选择日期"
                        v-model="form.end_date"
                        type="date"
                        style="width: 100%;"
                        format="yyyy-MM-dd"
                        value-format="yyyy-MM-dd"
        ></el-date-picker>
      </el-form-item>
      <el-form-item label="电信合同编号" :label-width="formLabelWidth" prop="tele_contract_num">
        <el-input v-model="form.tele_contract_num" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="总金额" :label-width="formLabelWidth" prop="amount">
        <el-input v-model.number="form.amount" type="number" min="0"></el-input>
      </el-form-item>
    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button round @click="closeDialog">取 消</el-button>
      <el-button round type="primary" @click="postData('form')">确 定</el-button>
    </div>
  </el-dialog>
</template>

<script>
export default {
  name: 'project-form',
  props: {
    tableIndex: {
      type: Number,
      default: -1
    },
    dialogFormVisible: {
      type: Boolean,
      default: false
    },
    dialogTitle: {
      type: String,
      default: '新建项目'
    },
    dialogData: {
      type: Object,
      default: function () {
        return {}
      }
    }
  },
  data () {
    return {
      form: {
        contract_num: '',
        contract_date: '',
        project_num: '',
        start_date: '',
        area: '',
        contract_name: '',
        custom: '',
        end_date: '',
        tele_contract_num: '',
        amount: ''
      },
      formLabelWidth: '120px',
      rules: {
        contract_num: [
          { required: true, message: '请输入合同编号', trigger: 'blur' }
        ],
        contract_date: [
          { required: true, message: '请选择时间', trigger: 'blur' }
        ],
        project_num: [
          { required: true, message: '请输入项目编号', trigger: 'blur' }
        ],
        start_date: [
          { required: true, message: '请选择时间', trigger: 'blur' }
        ],
        area: [
          { required: true, message: '请输入所属区域', trigger: 'blur' }
        ],
        contract_name: [
          { required: true, message: '请输入合同名称', trigger: 'blur' }
        ],
        custom: [
          { required: true, message: '请输入客户名称', trigger: 'blur' }
        ],
        end_date: [
          { required: true, message: '请选择时间', trigger: 'blur' }
        ],
        tele_contract_num: [
          { max: 32, message: '长度大于 32 个字符', trigger: 'blur' }
        ],
        amount: [
          { required: true, message: '请输入总金额', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    // 关闭弹窗
    closeDialog () {
      this.$emit('dialogVisible')
    },
    handleClose () {
      this.$confirm('确认关闭？', { roundButton: true })
        .then(_ => {
          this.closeDialog()
        })
        .catch(_ => {})
    },
    // 发送数据
    postData (formName) {
      // 发送前校验数据
      this.$refs[formName].validate((valid) => {
        if (valid) {
          // 判断新建或者修改
          if (this.dialogTitle === '新建项目') {
            // 新建使用 post
            this.$request
              .post('/contract/create/', {
                ...this.form
              })
              .then((res) => {
                this.closeDialog()
                this.$message({
                  type: 'success',
                  message: '创建成功!'
                })
                this.$emit('pushData', res.data)
              })
              .catch((e) => {
                console.log(e)
              })
          } else {
            // 修改使用 put
            this.$request
              .put('/contract/' + this.form.id, {
                ...this.form
              })
              .then((res) => {
                this.closeDialog()
                this.$message({
                  type: 'success',
                  message: '修改成功!'
                })
                this.$emit('updateData', res.data, this.tableIndex)
              })
              .catch((e) => {
                console.log(e)
              })
          }
        } else {
          console.log('error submit')
          return false
        }
      })
    }
  },
  watch: {
    dialogData (val) {
      this.form = val
    }
  }
}
</script>

<style scoped>

</style>
