<template>
  <div>
    <Breadcrumb :title="title"/>
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
      <!--      搜索框-->
      <form>
        <div class="form-input">
          <input type="search" v-model="searchData" placeholder="请输入区域 项目编号 客户名称查询...">
          <button @click="handleSearch" type="submit" class="search-btn"><i class='el-icon-search' ></i></button>
        </div>
      </form>
    </div>
    <!--    表格数据-->
    <div class="table">
      <el-table
        v-loading="dataLoading"
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
        <el-table-column label="操作"
                         width="150">
          <template slot-scope="scope">
            <el-button
              size="mini"
              @click="handleEdit(scope.$index, scope.row)">编辑</el-button>

            <el-button
              size="mini"
              type="danger"
              @click="handleDelete(scope.$index, scope.row)">删除</el-button>

          </template>
        </el-table-column>
      </el-table>
    </div>
    <!--    页码-->
    <Pagination :total="pagination.total" :pageSize="pagination.pageSize"/>
  </div>
</template>
<script>
import Pagination from '@/components/Pagination'
import Breadcrumb from '@/components/Breadcrumb'

export default {
  name: 'Contract',
  data () {
    return {
      title: '项目管理',
      searchData: '',
      tableData: [],
      dialogFormVisible: false,
      dataLoading: false,
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
      pagination: {
        total: 0
      },
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
  components: {
    Pagination,
    Breadcrumb
  },
  methods: {
    // 搜索
    handleSearch () {
      this.$request
        .get('/contract/' + this.searchData)
        .then((res) => {
          console.log(res)
          this.tableData = res.data
          this.$message({
            type: 'success',
            message: '共找到' + res.data.length + '数据'
          })
          this.searchData = ''
        })
        .catch((e) => {
          console.log(e)
          this.$message({
            type: 'warning',
            message: '未找到数据'
          })
          this.searchData = ''
        })
    },
    // 编辑
    handleEdit (index, row) {
      console.log(index, row.id)
      this.$request
        .get('/contract/' + row.id)
        .then((res) => {
          console.log(res)
          console.log('success', this.tableData)
        })
        .catch((e) => {
          console.log('fail', e)
        })
    },
    // 删除数据
    handleDelete (index, row) {
      this.$confirm('此操作将永久删除该数据, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.tableData.splice(index, 1)
        this.pagination.total = this.tableData.length
        this.$request
          .delete('/contract/' + row.id)
          .then((res) => {
            console.log(res.data)
          })
        this.$message({
          type: 'success',
          message: '删除成功!'
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    handleClose (done) {
      this.$confirm('确认关闭？')
        .then(_ => {
          done()
        })
        .catch(_ => {})
    },
    // 发送数据
    postData () {
      this.$request
        .post('/contract/create/', {
          ...this.form
        })
        .then((res) => {
          this.dialogFormVisible = false
          this.$message({
            type: 'success',
            message: '创建成功!'
          })
          this.tableData.push(res.data)
        })
        .catch((e) => {
          console.log(e)
        })
    }
  },
  mounted () {
    // 获取数据
    this.dataLoading = true
    this.$request
      .get('/contract')
      .then((res) => {
        this.tableData = res.data
        this.pagination.total = res.data.length
      })
      .catch((e) => {
        console.log(e)
      })
      .finally(() => {
        this.dataLoading = false
      })
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
  max-width: 500px;
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
