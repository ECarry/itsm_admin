<template>
  <div>
    <div class="search">
      <el-button type="primary" round>新建项目</el-button>
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
          prop="name"
          label="姓名"
          width="180">
        </el-table-column>
        <el-table-column
          prop="address"
          label="地址">
        </el-table-column>
        <el-table-column
          prop="status"
          label="状态">
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Contract',
  data () {
    return {
      tableData: [{
        id: '1',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        id: '2',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1517 弄'
      }, {
        id: '3',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1519 弄'
      }, {
        id: '4',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      }]
    }
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
