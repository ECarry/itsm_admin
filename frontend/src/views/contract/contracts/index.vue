<template>
  <div>
    <div class="search">
      <!--      新建项目表单-->
      <el-button type="primary" round @click="dialogFormVisible = true">新建项目</el-button>
      <el-dialog title="新建项目"
                 :visible.sync="dialogFormVisible"
                 :before-close="handleClose"
      >
        <el-form :model="form" :rules="rules">
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
          <el-form-item label="总金额" :label-width="formLabelWidth" prop="total_sum">
            <el-input v-model.number="form.total_sum" type="number" min="0" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="postData">确 定</el-button>
        </div>
      </el-dialog>
      <form action="#">
        <div class="form-input">
          <input type="search" placeholder="Search...">
          <button type="submit" class="search-btn"><i class='el-icon-search' ></i></button>
        </div>
      </form>
    </div>
    <div class="table">
      <el-table
        :data="tableData"
        :cell-style="{background: 'var(--light)'}"
        :header-cell-style="{background: 'var(--blue)', color: 'var(--light)'}"
        style="width: 100%
        ">
        <el-table-column
          prop="id"
          label="ID"
          width="50">
        </el-table-column>
        <el-table-column
          prop="contract_num"
          label="合同编号">
        </el-table-column>
        <el-table-column
          prop="contract_date"
          label="签订时间">
        </el-table-column>
        <el-table-column
          prop="project_num"
          label="项目编号">
        </el-table-column>
        <el-table-column
          prop="start_date"
          label="开工时间">
        </el-table-column>
        <el-table-column
          prop="area"
          label="区域">
        </el-table-column>
        <el-table-column
          prop="contract_name"
          label="合同名称">
        </el-table-column>
        <el-table-column
          prop="custom"
          label="客户">
        </el-table-column>
        <el-table-column
          prop="end_date"
          label="完工时间">
        </el-table-column>
        <el-table-column
          prop="tele_contract_num"
          label="电信合同编号">
        </el-table-column>
        <el-table-column
          prop="total_sum"
          label="总金额">
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  name: 'Contract',
  data () {
    return {
      tableData: [],
      dialogFormVisible: false,
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
        total_sum: ''
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
        total_sum: [
          { required: true, message: '请输入总金额', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    handleClose (done) {
      this.$confirm('确认关闭？')
        .then(_ => {
          done()
        })
        .catch(_ => {})
    },
    // 获取数据
    getData () {
      axios.get('http://127.0.0.1:8000/contract/').then((response) => {
        this.tableData = response.data
      })
    },
    // 发送数据
    postData () {
      console.log({ ...this.form })
      axios
        .post('http://127.0.0.1:8000/contract/create/', {
          ...this.form
        })
    }
  },
  mounted () {
    this.getData()
  }
}
</script>
<style >
.search {
  height: 50px;
  display: flex;
  align-items: center;
}

.search form {
  margin-left: 10px;
  max-width: 300px;
  width: 100%;
  margin-right: auto;
}

.search form .form-input {
  display: flex;
  align-items: center;
  height: 36px;
}
.search form .form-input input {
  flex-grow: 1;
  padding: 0 16px;
  height: 100%;
  border: none;
  background: var(--light);
  border-radius: 36px 0 0 36px;
  outline: none;
  width: 100%;
  color: var(--dark);
}
.search form .form-input button {
  width: 36px;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: var(--blue);
  color: var(--light);
  font-size: 18px;
  border: none;
  outline: none;
  border-radius: 0 36px 36px 0;
  cursor: pointer;
}

.table {
  margin-top: 20px;
}
</style>
