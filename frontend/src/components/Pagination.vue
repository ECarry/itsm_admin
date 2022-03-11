<template>
  <el-pagination
    style="margin-top: 20px; text-align: center"
    background
    @size-change="handleSizeChange"
    @current-change="handleCurrentChange"
    :page-sizes="[10, 20, 50, 100]"
    layout="total, prev, pager, next, sizes"
    :total="total">
  </el-pagination>
</template>

<script>
export default {
  name: 'Pagination',
  methods: {
    handleSizeChange (val) {
      console.log(`每页 ${val} 条`)
    },
    handleCurrentChange (val) {
      console.log(`当前页: ${val}`)
    }
  },
  props: {
    total: {
      type: Number,
      default: 10
    }
  }
}
</script>

<style scoped>

</style>
