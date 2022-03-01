<template>
  <div>
    <div class="search">
      <el-button type="primary" round @click="dialogFormVisible = true">新建项目</el-button>
      <!--      新建项目表单-->
      <el-dialog title="新建项目" :visible.sync="dialogFormVisible">
        <el-form :model="form">
          <el-form-item label="活动名称" :label-width="formLabelWidth">
            <el-input v-model="form.name" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="活动区域" :label-width="formLabelWidth">
            <el-select v-model="form.region" placeholder="请选择活动区域">
              <el-option label="区域一" value="shanghai"></el-option>
              <el-option label="区域二" value="beijing"></el-option>
            </el-select>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
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
        background-color="red"
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
      tableData: '',
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
      formLabelWidth: '200px'
    }
  },
  methods: {
    // 获取数据
    getData () {
      axios.get('http://127.0.0.1:8000/contract/').then((response) => {
        this.tableData = response.data
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
