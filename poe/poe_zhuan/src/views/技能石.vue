<template>
  <div class="jineng-container">
    <el-row :gutter="20">
      <el-col :span="12">
        <el-button type="text" class="custom-head" >五军练什么</el-button>
        <el-col :span="18">
            <el-table :data="sortedGemData" border :style="{ marginTop: '15px' }" v-loading="loading" element-loading-text="加载中...">
                <!-- 第一列显示 name -->
                <el-table-column prop="name" label="名称" min-width="60"/>
                <!-- 第二列显示 level 为 1 的 calculated 值 -->
                <el-table-column label="1级价格" min-width="40">
                    <template v-slot="scope">
                        <span @click="navigatelv1ToSearch(scope.row.variants)" style="color: blue; cursor: pointer;">
                        {{ getLevel1Calculated(scope.row.variants).toFixed(2) }}
                    </span>
                    </template>
                </el-table-column>
                <el-table-column label="20级价格" min-width="40">
                    <template v-slot="scope">
                        <span @click="navigatelv20ToSearch(scope.row.variants)" style="color: blue; cursor: pointer;">
                        {{ getLevel20Calculated(scope.row.variants).toFixed(2) }}
                    </span>
                    </template>
                </el-table-column>
                <el-table-column
                    label="价格差值"   min-width="45"
                    sortable
                    :sort-method="priceDifferenceSort"
                    >
                    <template v-slot="scope">
                        {{ (getLevel20Calculated(scope.row.variants) - getLevel1Calculated(scope.row.variants)).toFixed(2) }}
                    </template>
                 </el-table-column>
                 <el-table-column label="市集数量" min-width="40">
                    <template v-slot="scope">
                        {{ getLevel20Count(scope.row.variants) }}
                    </template>
                </el-table-column>
            </el-table>
        </el-col>
        <el-row :gutter="15">
            <el-col :span="5"><div class="grid-content ep-bg-purple" />
              <div class="input-item">
                <div class="label">20级20品未瓦价格</div>
                <el-input
                  v-model.number="valueA"
                  type="number"
                  placeholder="请输入数字"
                 
                />
              </div>
            </el-col>
            <el-col :span="5"><div class="grid-content ep-bg-purple" />
              <div class="input-item">
                <div class="label">20级20品已瓦价格</div>
                <el-input
                  v-model.number="valueB"
                  type="number"
                  placeholder="请输入数字"
                />
              </div>
            </el-col>
            <el-col :span="5"><div class="grid-content ep-bg-purple" />
              <div class="input-item">
                <div class="label">20级降品价格</div>
                <el-input
                  v-model.number="valueC"
                  type="number"
                  placeholder="请输入数字"
                 
                />
              </div>
            </el-col>
    </el-row>
    <el-row :gutter="15">
            <el-col :span="5"><div class="grid-content ep-bg-purple" />
              <div class="input-item">
                <div class="label">20级23品价格</div>
                <el-input
                  v-model.number="valueD"
                  type="number"
                  placeholder="请输入数字"
                />
              </div>
            </el-col>
            <el-col :span="5"><div class="grid-content ep-bg-purple" />
              <div class="input-item">
                <div class="label">21级20品已瓦价格</div>
                <el-input
                  v-model.number="valueE"
                  type="number"
                  placeholder="请输入数字"
                
                />
              </div>
            </el-col>
            <el-col :span="5"><div class="grid-content ep-bg-purple" />
              <div class="input-item">
                <div class="label">同名瓦尔宝石价格</div>
                <el-input
                  v-model.number="valueF"
                  type="number"
                  placeholder="请输入数字"
                />
              </div>
            </el-col>
    </el-row>
    <div class="label">单瓦预期转化收益</div>
        <el-input
        v-model.number="valueG"
        type="number"
        placeholder="请输入数字"
        style="width: 140px;"  
        />
      </el-col>
      <el-col :span="12">
        <el-button type="text" class="custom-head" >什么值得瓦</el-button>
        <el-col :span="18">
            <el-table :data="sorted21GemData" border :style="{ marginTop: '15px' }" v-loading="loading" element-loading-text="加载中...">
                <el-table-column prop="name" label="名称" min-width="60"/>
                <el-table-column label="20级价格" min-width="40">
                    <template v-slot="scope">
                        <span @click="navigatelv20ToSearch(scope.row.variants)" style="color: blue; cursor: pointer;">
                        {{ getLevel20_waCalculated(scope.row.variants).toFixed(2) }}
                    </span>
                    </template>
                </el-table-column>
                <el-table-column label="21级价格" min-width="40">
                    <template v-slot="scope">
                        <span @click="navigatelv21ToSearch(scope.row.variants)" style="color: blue; cursor: pointer;">
                        {{ getLevel21Calculated(scope.row.variants).toFixed(2) }}
                    </span>
                    </template>
                </el-table-column>
                <el-table-column
                    label="利润值"   min-width="45"
                    sortable
                    :sort-method="price21DifferenceSort"
                    >
                    <template v-slot="scope">
                        {{ (getLevel21Calculated(scope.row.variants) - getLevel20_waCalculated(scope.row.variants)*7).toFixed(2) }}
                    </template>
                 </el-table-column>
                 <el-table-column label="市集数量" min-width="40">
                    <template v-slot="scope">
                        {{ getLevel21Count(scope.row.variants)}}
                    </template>
                </el-table-column>
            </el-table>
        </el-col>
          <el-row :gutter="15" style="margin-left: 15px;">
              <el-col :span="5"><div class="grid-content ep-bg-purple" />
                <div class="input-item">
                  <div class="label">20级23品未瓦价格</div>
                  <el-input
                    v-model.number="valueA2"
                    type="number"
                    placeholder="请输入数字"
                  
                  />
                </div>
              </el-col>
              <el-col :span="5"><div class="grid-content ep-bg-purple" />
                <div class="input-item">
                  <div class="label">21级20品已瓦价格</div>
                  <el-input
                    v-model.number="valueB2"
                    type="number"
                    placeholder="请输入数字"
                  />
                </div>
              </el-col>
              <el-col :span="5"><div class="grid-content ep-bg-purple" />
                <div class="input-item">
                  <div class="label">21级23品价格</div>
                  <el-input
                    v-model.number="valueC2"
                    type="number"
                    placeholder="请输入数字"
                  
                  />
                </div>
              </el-col>
          </el-row>
          <el-row :gutter="15" style="margin-left: 15px;">
                  <el-col :span="5"><div class="grid-content ep-bg-purple" />
                    <div class="input-item">
                      <div class="label">21级20品瓦尔价格</div>
                      <el-input
                        v-model.number="valueD2"
                        type="number"
                        placeholder="请输入数字"
                      />
                    </div>
                  </el-col>
                  <el-col :span="5"><div class="grid-content ep-bg-purple" />
                    <div class="input-item">
                      <div class="label">20级23品瓦尔价格</div>
                      <el-input
                        v-model.number="valueE2"
                        type="number"
                        placeholder="请输入数字"
                      />
                    </div>
                  </el-col>
                  <el-col :span="5"><div class="grid-content ep-bg-purple" />
                    <div class="input-item">
                      <div class="label">20级20品瓦尔价格</div>
                      <el-input
                        v-model.number="valueF2"
                        type="number"
                        placeholder="请输入数字"
                      />
                    </div>
                  </el-col>
          </el-row>
          <div class="label" style="margin-left: 25px;">双瓦预期转化收益</div>
              <el-input
              v-model.number="valueG2"
              type="number"
              placeholder="请输入数字"
              style="width: 140px;margin-left: 25px;"  
              />
      </el-col>
    </el-row>
  </div>
</template>


<script>
export default {
    data() {
        return {
            gemdata: [],  // 存储筛选后的数据
            valueA:0,
            valueB:0,
            valueC:0,
            valueD:0,
            valueE:0,
            valueF:0,
            valueG:0,
            valueA2:0,
            valueB2:0,
            valueC2:0,
            valueD2:0,
            valueE2:0,
            valueF2:0,
            valueG2:0,
            loading: false,
            error: null,
        };
    },
    computed: 
    {
        sortedGemData() {
        return this.gemdata
            .map(item => ({
            ...item,
            priceDifference: this.getLevel20Calculated(item.variants) - this.getLevel1Calculated(item.variants)
            }))
            .sort((a, b) => b.priceDifference - a.priceDifference) // 从大到小排序
            .slice(0, 12); // 取前十五个
        },
        sorted21GemData() {
        return this.gemdata
            .map(item => ({
            ...item,
            priceDifference: this.getLevel21Calculated(item.variants) - this.getLevel20_waCalculated(item.variants)*7
            }))
            .sort((a, b) => b.priceDifference - a.priceDifference) // 从大到小排序
            .slice(0, 12); // 取前十五个
        },
    },
    watch: {
    // 监听值的变化并更新计算
    valueA: 'updateCalculations',
    valueB: 'updateCalculations',
    valueC: 'updateCalculations',
    valueD: 'updateCalculations',
    valueE: 'updateCalculations',
    valueF: 'updateCalculations',
    valueA2: 'updateCalculations',
    valueB2: 'updateCalculations',
    valueC2: 'updateCalculations',
    valueD2: 'updateCalculations',
    valueE2: 'updateCalculations',
    valueF2: 'updateCalculations'
  },
    methods: {
        updateCalculations()
        {
            this.valueG=(1/4+1/8+1/4*1/10)*this.valueB+1/8*this.valueE+7/80*this.valueD+1/4*this.valueF+1/4*10/20*this.valueC-this.valueA
            console.log(7/80*this.valueD)
        },
        async fetchAndMergeItems() 
        {
            this.loading = true;
            this.error = null;
            try {
                // 使用 fetch API 获取 JSON 数据
                const response = await fetch('/gem.json');
                if (!response.ok) throw new Error(`网络响应不正常: ${response.status}`);
                const data = await response.json();
                // 合并相同名称的项目
                const mergedItems = {};
                data.forEach(item => {
                    // 如果这个 name 还没有出现过，就创建一个新数组
                    if (!mergedItems[item.name]) {
                        mergedItems[item.name] = {
                            name: item.name,
                            variants: []  // 用于存储不同类型的 `level` 和 `corrupted` 的组合
                        };
                    }
                    // 将当前项目的 level 和 corrupted 添加到 variants 中
                    mergedItems[item.name].variants.push({
                        level: item.level,
                        corrupted: item.corrupted,
                        calculated: item.calculated,  // 根据需要添加其他属性
                        count: item.count,  // 根据需要添加其他属性
                        searchCode:item.searchCode
                    });
                });
                // 转换合并结果为数组
                const mergedArray = Object.values(mergedItems);
                // 筛选出所有包含 level=20 且 corrupted=false 的 variant
                // 将筛选结果存储在 gem_lv20 中
                this.gemdata = mergedArray;
                console.log("合并后的数据", this.gemdata);
            } catch (error) {
                console.error("获取或处理 JSON 数据时出错:", error);
                this.error = error.message || '获取数据失败，请检查网络连接';
            } finally {
                this.loading = false;
            }
        },
        navigatelv1ToSearch(variants)
        {
            const level1Item = variants.find(item => item.level === 1);
            const url = `https://poe.game.qq.com/trade/search/S26%E8%B5%9B%E5%AD%A3/${level1Item.searchCode}`; // 构建完整的 URL
            window.open(url, '_blank'); // 在新标签页中打开链接
        },
        navigatelv20ToSearch(variants)
        {
            const level1Item = variants.find(item => item.level === 20&&item.corrupted === false&&item.count>3);
            const url = `https://poe.game.qq.com/trade/search/S26%E8%B5%9B%E5%AD%A3/${level1Item.searchCode}`; // 构建完整的 URL
            window.open(url, '_blank'); // 在新标签页中打开链接
        },
        navigatelv21ToSearch(variants)
        {
            const level1Item = variants.find(item => item.level === 21&&item.corrupted === true&&item.count>3);
            const url = `https://poe.game.qq.com/trade/search/S26%E8%B5%9B%E5%AD%A3/${level1Item.searchCode}`; // 构建完整的 URL
            window.open(url, '_blank'); // 在新标签页中打开链接
        },
        getLevel1Calculated(variants) 
        {
        const level1Item = variants.find(item => item.level === 1);
        return level1Item ? level1Item.calculated : 0;
        },
        getLevel20Calculated(variants) 
        {
        const level1Item = variants.find(item => item.level === 20&&item.corrupted === false&&item.count>3);
        return level1Item ? level1Item.calculated : 0;
        },
        getLevel20_waCalculated(variants) 
        {
        const level1Item = variants.find(item => item.level === 20&&item.corrupted === false&&item.count>3);
        return level1Item ? level1Item.calculated : 100000;
        },
        getLevel21Calculated(variants) 
        {
        const level1Item = variants.find(item => item.level === 21&&item.corrupted === true&&item.count>3 );
        return level1Item ? level1Item.calculated : 0;
        },
        getLevel20Count(variants) 
        {
        const level1Item = variants.find(item => item.level === 20&&item.corrupted === false);
        return level1Item ? level1Item.count : 0;
        },
        getLevel21Count(variants) 
        {
        const level1Item = variants.find(item => item.level === 21&&item.corrupted === true);
        return level1Item ? level1Item.count : 0;
        },
        priceDifferenceSort(a, b) 
        {
      const aDifference = this.getLevel20Calculated(a.variants) - this.getLevel1Calculated(a.variants);
      const bDifference = this.getLevel20Calculated(b.variants) - this.getLevel1Calculated(b.variants);
      return aDifference - bDifference; // 返回差值比较结果
        },
        price21DifferenceSort(a, b) 
        {
      const aDifference = this.getLevel21Calculated(a.variants) - this.getLevel20_waCalculated(a.variants)*7;
      const bDifference = this.getLevel21Calculated(b.variants) - this.getLevel20_waCalculated(b.variants)*7;
      return aDifference - bDifference; // 返回差值比较结果
        },
    },
    mounted() {
        this.fetchAndMergeItems(); // 组件挂载时获取数据
    }
};
</script>
<style lang="less" scoped>
.jineng-container {
  padding: var(--spacing-md);
  max-width: 100%;
  overflow-x: auto;
}

.custom-head {
  border: none;
  color: var(--text-primary);
  background-color: transparent;
  font-size: var(--font-size-xl);
  font-weight: 600;
  margin-bottom: var(--spacing-md);
  display: block;
  width: 100%;
  text-align: center;
}

/* 表格样式 */
.el-table {
  width: 100%;
  font-size: var(--font-size-sm);
}

/* 输入组样式 */
.input-group {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-xs);
  margin-bottom: var(--spacing-md);
}

.input-label {
  font-size: var(--font-size-sm);
  font-weight: 500;
  color: var(--text-primary);
  margin-bottom: var(--spacing-xs);
}

/* 响应式设计 */
@media (max-width: 768px) {
  .jineng-container {
    padding: var(--spacing-sm);
  }
  
  .custom-head {
    font-size: var(--font-size-lg);
  }
  
  .el-col {
    margin-bottom: var(--spacing-md);
  }
}

@media (max-width: 480px) {
  .custom-head {
    font-size: var(--font-size-base);
  }
}
</style>

