<template>
  <el-table :data="tableData" style="width: 100%">
    <el-table-column prop="id" label="ID" width="100"> </el-table-column>

    <el-table-column prop="projectNum" label="项目编号" width="200"> </el-table-column>

    <el-table-column prop="contractNum" label="合同编号" width="200"> </el-table-column>

    <el-table-column prop="projectName" label="项目名称" width="300"> </el-table-column>

    <el-table-column prop="customerName" label="客户名称" width="250"> </el-table-column>

    <el-table-column
      prop="startDate"
      label="开工日期"
      sortable
      width="180"
      column-key="startDate"
    >
    </el-table-column>

    <el-table-column
      prop="endDate"
      label="结束日期"
      sortable
      width="180"
      column-key="endDate"
    >
    </el-table-column>

  </el-table>
</template>
<script>
const formData = {
  id: '',
  projectNum: '',
  contractNum: '',
  projectName: '',
  startDate: '',
  customerName: '',
  endDate: ''
}
export default {
  name: "Contract",
  data() {
    return {
      tableData: { ...formData }
    };
  },
};
</script>
<style>
</style>