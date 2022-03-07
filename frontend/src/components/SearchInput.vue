<template>
  <el-input placeholder="请输入内容"
            v-model.trim="searchValue"
            style="width: 500px"
            class="input-with-select">
    <el-select v-model="selectValue" slot="prepend" placeholder="请选择" style="width: 120px">
      <el-option :label="SearchForm.search1.label" :value="SearchForm.search1.value"></el-option>
      <el-option :label="SearchForm.search2.label" :value="SearchForm.search2.value"></el-option>
      <el-option :label="SearchForm.search3.label" :value="SearchForm.search3.value"></el-option>
    </el-select>
    <el-button slot="append" icon="el-icon-search" @click="search"></el-button>
  </el-input>
</template>

<script>
export default {
  name: 'SearchInput',
  props: {
    SearchForm: {
      type: Object,
      default: function () {
        return {}
      }
    }
  },
  data () {
    return {
      selectValue: '',
      searchValue: ''
    }
  },
  methods: {
    search () {
      this.$emit('search', this.selectValue, this.searchValue)
    }
  }
}
</script>

<style scoped>

</style>
