<template>
  <div>
    <!--    面包屑-->
    <Breadcrumb :title="title"/>
    <!--    新建 搜索-->
    <div class="search">
      <!--      新建项目表单-->
      <el-button type="primary" round @click="handleCreate" style="margin-right: 10px">新建项目</el-button>
      <ProjectForm :dialogFormVisible="dialogFormVisible"
                   :dialogTitle="dialogTitle"
                   :dialogData="dialogData"
                   :tableIndex="tableIndex"
                   @dialogVisible="dialogVisible"
                   @pushData="pushData"
                   @updateData="updateData"/>
      <SearchInput :SearchForm="SearchForm" @search="search" ref="searchForm"/>
      <el-button type="info" round plain @click="resetSearchForm" style="margin-left: 10px">重置</el-button>
    </div>
    <!--    表格数据-->
    <div class="table">
      <el-table
        v-loading="dataLoading"
        :data="tableData"
        :cell-style="{background: 'var(--light)'}"
        :header-cell-style="{background: 'var(--blue)', color: 'var(--light)'}"
        style="width: 100%; border-radius: 20px"
        >
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
          prop="amount"
          label="总金额">
        </el-table-column>
        <el-table-column label="操作"
                         width="150">
          <template slot-scope="scope">
            <el-button size="mini"
                       round
                       @click="handleEdit(scope.$index, scope.row)">编辑</el-button>

            <el-button size="mini"
                       round
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
import ProjectForm from './components/ProjectForm'
import SearchInput from '@/components/SearchInput'

export default {
  name: 'Contract',
  data () {
    return {
      title: '项目管理',
      tableData: [],
      dataLoading: false,
      dialogFormVisible: false,
      dialogTitle: '',
      dialogData: {},
      tableIndex: -1,
      pagination: {
        total: 0
      },
      SearchForm: {
        search1: {
          label: '项目编号',
          value: 'projectNum'
        },
        search2: {
          label: '客户',
          value: 'custom'
        },
        search3: {
          label: '区域',
          value: 'area'
        }
      }
    }
  },
  components: {
    ProjectForm,
    Pagination,
    Breadcrumb,
    SearchInput
  },
  methods: {
    // 更改 dialogFormVisible
    dialogVisible () {
      this.dialogFormVisible = false
      this.dialogTitle = '新建项目'
    },
    // 后端返回数据插入表格
    pushData (data) {
      this.tableData.push(data)
    },
    //
    updateData (data, index) {
      this.tableData.splice(index, 1, data)
    },
    // 新建项目
    handleCreate () {
      this.dialogTitle = '新建项目'
      this.dialogFormVisible = true
      this.dialogData = {}
    },
    // 搜索
    search (label, value) {
      if (label && value) {
        this.$request
          .get('/contract/' + label + '/' + value)
          .then((res) => {
            this.tableData = res.data
            this.$message({
              type: 'success',
              message: '共找到' + res.data.length + '数据'
            })
          })
          .catch((e) => {
            console.log(e)
            this.$message({
              type: 'warning',
              message: '未找到数据'
            })
          })
      } else {
        this.$message({
          type: 'warning',
          message: '请选择搜索项和输入搜索内容'
        })
      }
    },
    // 重置搜索框
    resetSearchForm () {
      this.getData()
      this.$refs.searchForm.searchValue = ''
      this.$refs.searchForm.selectValue = ''
    },
    // 编辑
    handleEdit (index, row) {
      console.log('index', index)
      this.dialogTitle = '编辑项目'
      this.dialogFormVisible = true
      this.$request
        .get('/contract/' + row.id)
        .then((res) => {
          this.dialogData = res.data
          this.tableIndex = index
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
        type: 'warning',
        roundButton: true
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
    // 获取数据
    getData () {
      this.dataLoading = true
      this.$request
        .get('/contract')
        .then((res) => {
          this.tableData = res.data
          this.pagination.total = res.data.length
        })
        .catch((e) => {
          console.log(e)
          this.$router.push('/login')
        })
        .finally(() => {
          this.dataLoading = false
        })
    }
  },
  mounted () {
    // 获取数据
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
