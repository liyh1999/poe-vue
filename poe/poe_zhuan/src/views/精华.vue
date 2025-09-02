<template>
  <div class="jinghua-container">
    <el-row :gutter="20">
      <el-col :span="8">
        <el-button type="primary" class="modern-button filter-button button-click" @click="filterlowItems">低价精华</el-button>
      </el-col>
      <el-col :span="8">
        <el-button type="success" class="modern-button filter-button button-click" @click="filterhighItems">高价精华</el-button>
      </el-col>
      <el-col :span="8">
        <el-button type="info" class="modern-button filter-button button-click" @click="filterallItems">全部精华</el-button>
      </el-col>
    </el-row>
  
    <el-row :gutter="20" class="custom-row">
      <el-col :span="10">
        <el-table v-if="optimizedFilteredItems.length > 0" :data="optimizedFilteredItems" border v-loading="loading" element-loading-text="加载中..." class="modern-table" style="width: 100%;">
          <el-table-column prop="name" label="名称" min-width="120" show-overflow-tooltip>
            <template #default="{ row }">
              <div class="item-name-cell">
                <span class="item-name">{{ row.name }}</span>
              </div>
            </template>
          </el-table-column>
          <el-table-column prop="calculated" label="价格" sortable min-width="80" align="right">
            <template #default="{ row }">
              <span class="price-cell">{{ row.calculated.toFixed(2) }}C</span>
            </template>
          </el-table-column>
          <el-table-column label="购买链接" min-width="60" align="center">
            <template #default="{ row }">
              <a :href="'https://poe.game.qq.com/trade/search/S26赛季/' + row.searchCode" target="_blank" rel="noopener noreferrer" class="trade-link">
                <img :src="row.icon" alt="icon" class="trade-icon" />
              </a>
            </template>
          </el-table-column>
          <el-table-column label="数量" min-width="100" align="center">
            <template #default="{ row }">
              <el-input v-model="row.customQuantity" type="number" placeholder="数量" size="small" class="quantity-input" />
            </template>
          </el-table-column>
        </el-table>
        <div v-else-if="!loading && !error" class="no-data">
          <el-empty description="没有找到符合条件的项" />
        </div>
        <div v-else-if="error" class="error-message">
          <el-alert
            :title="error"
            type="error"
            show-icon
            :closable="false"
          >
            <template #default>
              <p>{{ error }}</p>
              <el-button type="primary" @click="retryFetch">重试</el-button>
            </template>
          </el-alert>
        </div>

        <el-row :gutter="12" class="statistics-row">
          <el-col :span="6">
            <div class="statistic-card">
              <el-statistic title="转化预期收益" :value="`${shouyi.toFixed(2)}C`" class="count-up" />
              <div class="statistic-subtitle">{{ (shouyi/shensheng).toFixed(2) }}D</div>
            </div>
          </el-col>
          <el-col :span="6">
            <div class="statistic-card">
              <el-statistic title="精华总成本" :value="`${chengben.toFixed(2)}C`" class="count-up" />
              <div class="statistic-subtitle">{{ (chengben/shensheng).toFixed(2) }}D</div>
            </div>
          </el-col>
          <el-col :span="6">
            <div class="statistic-card">
              <el-statistic title="命能总成本" :value="`${mingneng_chengben.toFixed(2)}C`" class="count-up" />
              <div class="statistic-subtitle">{{ (mingneng_chengben/shensheng).toFixed(2) }}D</div>
            </div>
          </el-col>
          <el-col :span="6">
            <div class="statistic-card">
              <el-statistic title="利润空间" :value="`${(lirun * 100).toFixed(2)}%`" class="count-up" />
            </div>
          </el-col>
        </el-row>

          <el-row :gutter="16" class="input-row">
            <el-col :span="8">
              <div class="input-group">
                <label class="input-label">每图精华数</label>
                <el-input
                  v-model.number="valueA"
                  type="number"
                  placeholder="请输入数字"
                  class="modern-input"
                />
              </div>
            </el-col>
            <el-col :span="8">
              <div class="input-group">
                <label class="input-label">每图成本(C)</label>
                <el-input
                  v-model.number="valueB"
                  type="number"
                  placeholder="请输入数字"
                  class="modern-input"
                />
              </div>
            </el-col>
            <el-col :span="8">
              <div class="input-group">
                <label class="input-label">每图时间(S)</label>
                <el-input
                  v-model.number="valueC"
                  type="number"
                  placeholder="请输入数字"
                  class="modern-input"
                />
              </div>
            </el-col>
          </el-row>
          <el-row :gutter="16" class="revenue-row">
            <el-col :span="8">
              <div class="revenue-card">
                <el-statistic title="每图收益" :value="`${meituShouyi.toFixed(2)}C`" class="count-up" />
                <div class="revenue-subtitle">{{ (meituShouyi/shensheng).toFixed(2) }}D</div>
              </div>
            </el-col>
            <el-col :span="8">
              <div class="revenue-card">
                <el-statistic title="每小时收益" :value="`${meixiaoshiShouyi.toFixed(2)}C`" class="count-up" />
                <div class="revenue-subtitle">{{ (meixiaoshiShouyi/shensheng).toFixed(2) }}D</div>
              </div>
            </el-col>
            <el-col :span="8">
              <div class="revenue-card">
                <el-statistic title="转化后小时收益" :value="`${(meixiaoshiShouyi+shouyi).toFixed(2)}C`" class="count-up" />
                <div class="revenue-subtitle">{{ ((meixiaoshiShouyi+shouyi)/shensheng).toFixed(2) }}D</div>
              </div>
            </el-col>

          <el-button plain @click="dialogTableVisible = true">
            理论计算方法
          </el-button>

          <el-dialog v-model="dialogTableVisible" title="理论计算方法说明" width="800">
            <div>共有20种破空精华，若有A种低价精华，B种高价目标转化精华，转化成任意精华是等概率的</div>
            <div>则预期收益的理论计算公式即：</div>
            <img :src="imageSrc" alt="描述文字" class="image" />
            <div>价格差-单次转化成本，共B个目标，遍历完B个目标后减去A次转化失败的成本，最后乘以这种低价精华的数量</div>
            <div>公式并不复杂读者自证不难</div>
            <div>容易注意到这里算出来的收益已经扣除了成本为净利润</div>
            <div>因此利润空间即：收益➗(精华成本+命能成本)</div>
            <div>这里的命能成本计算公式也不难注意到即：转化精华数量➗(B➗20)✖单次转化成本</div>
          </el-dialog>


        </el-row>
        </el-col>
     <el-col :span="14">
        <div class="section-header">转精华收益计算</div>
        <div class="cards-container">
          <el-card class="modern-card custom-card card-hover" v-for="(item, index) in saying" :key="index" :style="{ animationDelay: `${index * 0.1}s` }">
            <div class="card-content">
              <div class="card-title">{{ item.title }}</div>
              <div class="card-actions">
                <div v-if="index === 0" class="input-action">
                  <el-input 
                    v-model="shensheng" 
                    placeholder="DC比"
                    size="small"
                    class="action-input"
                  />
                </div>
                <div v-if="index === 1" class="input-action">
                  <el-input 
                    v-model="mingneng" 
                    placeholder="转化成本"
                    size="small"
                    class="action-input"
                  />
                </div>
              </div>
              <div class="right-text">{{ index === 0|| index === 1||index === 2 || index === 3||index === 4||index === 5||index === 6 ||index === 7? '' : item.rightText }}</div> 
              <div class="description" v-if="index === 2">
              <el-button-group>
                <el-button type="primary" @click="resetQuantities">一键清除</el-button> 
                <el-tooltip content="这里默认的数值是根据每图精华数量和刷图时间算出来的" placement="top">
                <el-button type="primary" style="display: flex; align-items: center;">
                  <el-input v-model="newQuantity" placeholder="输入数量" style="width: 50px;" />
                  <span @click="setQuantities(newQuantity)" style="margin-left: 10px;">一键设置</span>
                </el-button>
              </el-tooltip>
              </el-button-group>
            </div>
            <div class="description" v-if="index === 3">
                <el-button type="primary" @click="dialogVisible = true">
                  仓库读取
                </el-button>
    
                <el-dialog
                  title="请输入用户信息"
                  v-model="dialogVisible"
                  width="30%"
                  :before-close="handleDialogClose"
                >
                  <el-form :model="form">
                    <el-form-item label="用户名" :label-width="formLabelWidth">
                      <el-input v-model="form.username" autocomplete="off"></el-input>
                    </el-form-item>
                    <el-form-item label="possid" :label-width="formLabelWidth">
                      <el-input v-model="form.possid" autocomplete="off"></el-input>
                    </el-form-item>
                  </el-form>
                  <template #footer>
                    <span class="dialog-footer">
                      <el-button @click="dialogVisible = false">取消</el-button>
                      <el-button type="primary" @click="handleUserInfoSubmit">确认</el-button>
                    </span>
                  </template>
                </el-dialog>
              </div>
            <div class="description" v-if="index === 4">
              <el-button type="primary" @click="copyNames">一键复制</el-button> 
            </div>
            <div class="description" v-if="index === 5">
              <el-button type="primary" @click="calculateConversionProfit">转化收益计算</el-button> 
            </div>
            <div class="description" v-if="index === 6">
                <el-input 
                v-model="input" 
                style="width: 140px" 
                placeholder="请输入数字" 
                type="number"
                />
            </div>
            <div class="description" v-if="index === 7">
                <el-button type="primary" style="display: flex; align-items: center;">
                  <el-input v-model="count" placeholder="输入数量" style="width: 50px;" />
                  <span @click="changecount" style="margin-left: 10px;">一键打折</span>
                </el-button>
            </div>
          </div>
          <div class="description" >
            {{ item.description }} 
          </div>
        </el-card>
        </div>
      </el-col>
    </el-row>
  </div>
</template>
  <script>
 import { ElMessage, ElLoading } from "element-plus";
  export default {
    data() {
      return {
        saying: [
          { title: 'DC比', description: '神圣石与混沌石的换算比例', rightText: '右侧文字1' },
          { title: '单次转化成本', description: '原始蓝晶命能的价格*30', rightText: '右侧文字2' },
          { title: '一键清除/设置', description: '统一清除或设置左侧表格里数量标签页的所有内容', rightText: '右侧文字3' },
          { title: '读取仓库', description: '通过图片读取你的精华数量', rightText: '右侧文字3' },
          { title: '一键复制低价精华', description: '复制表格里精华名称标签的内容', rightText: '右侧文字3' },
          { title: '转化收益计算', description: '计算并显示转化收益', rightText: '右侧文字3' },
          { title: '低价阈值', description: '将小于设置值价格的精华定位低价', rightText: '右侧文字3' },
          { title: '精华折扣', description: '奸商你的打包收购价', rightText: '右侧文字3' },
        ],
        imageSrc: '/gongshi.png', // 替换为你的图片 URL
        input:4.0,
        mingneng:"",
        filteredItems: [], // 画表用的
        filteredlowItems: [], // 存储低价精华
        filteredhighItems: [], // 存储高价精华
        filteredallItems: [], // 存储全部精华
        items:[],
        isVisible: false,
        cookie: '',
        username: '咕神咕咕子',
        page:1,
        shouyi:0,
        chengben:0,
        mingneng_chengben:0,
        lirun:0,
        shensheng:0,
        newQuantity: 0, // 用于存储用户输入的新数量值
        valueA: 60,
        valueB: 50,
        valueC: 100,
        meitu_shouyi:0,
        meixiaoshi_shouyi:0,
        dialogTableVisible: false, // 控制弹窗显示状态
        results: [],
        processing: false,
        statusMsg: '准备就绪',
        currentLine: 0,
        textResults: [], // 用于存储识别的结果
        dialogVisible: false,
        activeItem:0,
        activeItem2:0,
        count:8,
        loading: false,
        error: null,
        retryCount: 0,
      form: {
        username: '',
        possid: ''
      },
      formLabelWidth: '80px',
      index: 3, // 确保 index===3 渲染此段内容
      };
    },
    computed: {
        // 使用计算属性优化性能
        optimizedFilteredItems() {
            if (!this.items.length) return [];
            const maxCalculated = parseFloat(this.input) || 0;
            return this.items.filter(item => 
                item.name.includes('破空精华') && item.calculated < maxCalculated
            );
        },
        optimizedFilteredHighItems() {
            if (!this.items.length) return [];
            const maxCalculated = parseFloat(this.input) || 0;
            return this.items.filter(item => 
                item.name.includes('破空精华') && item.calculated > maxCalculated
            );
        },
        optimizedFilteredAllItems() {
            if (!this.items.length) return [];
            return this.items.filter(item => 
                item.name.includes('破空精华') && item.calculated
            );
        },
        // 缓存计算结果
        averagePrice() {
            if (!this.optimizedFilteredAllItems.length) return 0;
            return this.optimizedFilteredAllItems.reduce((sum, item) => sum + item.calculated, 0) / 
                   this.optimizedFilteredAllItems.length;
        },
        meituShouyi() {
            return this.averagePrice * this.valueA - this.valueB;
        },
        meixiaoshiShouyi() {
            return this.valueC > 0 ? this.meituShouyi / this.valueC * 3600 : 0;
        },
        newQuantityCalculated() {
            return this.valueC > 0 ? this.valueA / this.valueC * 3600 / 20 : 0;
        }
    },
    watch: {
        // 监听值的变化并更新计算
        valueA: 'updateCalculations',
        valueB: 'updateCalculations',
        valueC: 'updateCalculations',
        input: 'updateFilteredItems',
    },
    methods: {
        handleClose() 
        {
          this.showDialog = false;
        },
        resetQuantities() 
        {
        this.filteredItems.forEach(item => {
          item.customQuantity = 0;
        });
        },
        setQuantities(value) 
        {
          const quantityValue = parseInt(value); // 确保输入为整数
          if (!isNaN(quantityValue)) {
            this.filteredItems.forEach(item => {
              item.customQuantity = quantityValue;
            });
          } else {
            console.error("请输入有效的数字");
          }
        },
        copyNames() 
        {
          const prefixWords = this.filteredItems
            .map(item => {
              const parts = item.name.split('破空精华');
              return parts[0].trim(); // 获取 "破空精华" 前的词语并去掉多余空格
            })
            .filter(prefix => prefix !== ''); // 过滤掉空字符串（如未找到前缀的情况）
          const result = prefixWords.join('|'); // 使用 | 连接前缀词
          // 复制到剪切板
          navigator.clipboard.writeText(result)
            .then(() => {
              this.$message.success("前缀词已复制到剪切板");
            })
            .catch(err => {
              console.error("复制失败:", err);
              this.$message.error("复制失败，请重试");
            });
        },
        async fetchData() 
        {
            this.loading = true;
            this.error = null;
            try {
                const response = await fetch('/jinghua.json'); // 替换为你的 JSON 路径
                if (!response.ok) throw new Error(`网络响应不正常: ${response.status}`);
                const data = await response.json();
                this.items = data; // 存储 JSON 数据
                // 使用计算属性自动更新筛选结果
                this.updateFilteredItems();
                this.updateCalculations();
                this.activeItem = this.items.find(item => item.name === '原始蓝晶命能');
                const activeCalculated = this.activeItem ? this.activeItem.calculated : null;
                if (activeCalculated !== null) {
                    this.saying[1].rightText = activeCalculated*30+"  C"; 
                    this.mingneng=activeCalculated*30
                }
                this.activeItem2 = this.items.find(item => item.name === '神圣石');
                const activeCalculated2 = this.activeItem ? this.activeItem2.calculated : null;
                this.shensheng=activeCalculated2
                if (activeCalculated2 !== null) {
                    this.saying[0].rightText = activeCalculated2+"  C"; 
                }
            } catch (error) {
                console.error('获取数据时出错:', error);
                this.error = error.message || '获取数据失败，请检查网络连接';
                this.retryCount++;
            } finally {
                this.loading = false;
            }
        },
        retryFetch() {
            this.retryCount = 0;
            this.fetchData();
        },
        updateCalculations() {
            // 使用计算属性自动更新，这里可以添加额外的计算逻辑
            this.meitu_shouyi = this.meituShouyi;
            this.meixiaoshi_shouyi = this.meixiaoshiShouyi;
            this.newQuantity = this.newQuantityCalculated;
        },
        updateFilteredItems() {
            // 使用计算属性自动更新
            this.filteredItems = this.optimizedFilteredItems;
            this.filteredhighItems = this.optimizedFilteredHighItems;
            this.filteredallItems = this.optimizedFilteredAllItems;
        },
        filterlowItems() 
        {
            this.filteredItems = this.optimizedFilteredItems;
        },
        filterhighItems() 
        {
            this.filteredItems = this.optimizedFilteredHighItems;
        },
        filterallItems() 
        {
            this.filteredItems = this.optimizedFilteredAllItems;
        },
        calculateConversionProfit() {
            let totalProfit = 0;
            let total_chengben = 0;
            let total_mingneng_chengben = 0;
            
            // 使用Map优化查找性能
            const highItemMap = new Map();
            this.optimizedFilteredHighItems.forEach(item => {
                highItemMap.set(item.name, item);
            });
            
            // 遍历 filteredItems 中的每个项目
            for (const item of this.optimizedFilteredItems) {
                const itemPrice = item.calculated;  
                total_chengben += itemPrice * item.customQuantity;
                total_mingneng_chengben += item.customQuantity * 1 / (this.optimizedFilteredItems.length / 20) * this.mingneng;
                
                let total = 0;
                // 遍历高价项目计算收益
                for (const highItem of this.optimizedFilteredHighItems) {
                    const highPrice = highItem.calculated;  
                    const priceDifference = highPrice - itemPrice;
                    const profit = (priceDifference - this.mingneng) / 20;
                    total += profit;
                }
                totalProfit += (total - this.optimizedFilteredItems.length / 20 * this.mingneng) * item.customQuantity;
            }
            
            this.chengben = total_chengben;
            this.shouyi = totalProfit;
            this.mingneng_chengben = total_mingneng_chengben;
            this.lirun = totalProfit / (total_chengben + total_mingneng_chengben);
        },
        handleDialogClose() {
        this.dialogVisible = false
         },
        handleUserInfoSubmit() {
            if (!this.form.username || !this.form.possid) {
              this.$message.error('请填写完整信息');
              return;
            }
            // 保存到 localStorage
            localStorage.setItem('username', this.form.username);
            localStorage.setItem('possid', this.form.possid);
          
          this.dialogVisible = false
          // 调用后续处理函数
          this.processUserInfo(this.form.username, this.form.possid)
          
        },
        processUserInfo(username, possid) {
          fetch('/api/process_user_info', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, possid })
          })
            .then(response => {
              if (!response.ok) {
                throw new Error('请求失败');
              }
              return response.json();
            })
            .then(data => {
              console.log('后端返回结果:', data);
        
              if (data.success && Array.isArray(data.essences)) {
                data.essences.forEach(ess => {
                  const match = this.filteredallItems.find(item => item.baseType === ess.name);
                  if (match) {
                    match.customQuantity = ess.count; // 直接赋值即可
                  }
                });
              } else {
                console.warn('未收到有效的 essences 数据');
              }
            })
            .catch(error => {
              console.error('请求出错:', error);
            });
        },
        changecount() {
          const multiplier = Number(this.count);
          this.filteredlowItems.forEach(item => {
            const result = item.calculated * multiplier / 10;
            item.calculated = Math.round(result * 1000) / 1000;  // 保留三位小数（数值类型）
          });
        }



        
    },
    mounted() {
    this.fetchData(); // 组件挂载时获取数据
    this.filterlowItems() // 在组件挂载时调用筛选函数
    const savedUsername = localStorage.getItem('username');
    const savedPossid = localStorage.getItem('possid');
    if (savedUsername) this.form.username = savedUsername;
    if (savedPossid) this.form.possid = savedPossid;
  },
  };
  </script>
  
  <style>
  
  .image {
  width: 100%; /* 设置图片宽度 */
  max-width: 800px; /* 最大宽度限制 */
  height: auto; /* 自动调整高度 */
  text-align: center; /* 使文字和图片居中对齐 */
}
  .header {
    font-family: 'SimHei', sans-serif; /* 使用黑体 */
    font-weight: bold; /* 加粗 */
    font-size: 20px; /* 设置字体大小 */
    color: #000; /* 加深颜色 */
    margin-bottom: 0; /* 设置与卡片的间距 */
  }
  .title {
    font-size: 60px;
    font-family: "SimSun", "宋体", sans-serif; /* 设置为宋体 */
  }

  .title2 {
    font-size: 20px;
    font-weight: bold; /* 加粗 */
    font-family: "SimSun", "SimHei", sans-serif; /* 设置为宋体 */
  }
  .filter-button {
    width: 100%;
    height: 50px;
    font-size: var(--font-size-lg);
    font-weight: 600;
    border-radius: var(--border-radius-large);
    transition: var(--transition-fast);
  }
  
  .filter-button:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-base);
  }
  .custom-row {
    margin-top: 20px; /* 根据需要调整间距 */
  }
  .custom-card {
    margin-bottom: var(--spacing-md);
    border-radius: var(--border-radius-large);
    box-shadow: var(--shadow-light);
    transition: var(--transition-base);
  }
  
  .custom-card:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-dark);
  }
  .card-content {
    display: flex; /* 使用 Flexbox 布局 */
    justify-content: space-between; /* 在两侧对齐 */
    align-items: center; /* 垂直居中对齐 */
  }
  .description {
    font-family: "SimSun", "宋体", sans-serif; /* 设置为宋体 */
  }
  .right-text {
    margin-left: auto; /* 自动填充左边的空间，移动到最右侧 */
    color: #666; /* 设置右侧文字颜色 */
    font-family: "SimSun", "宋体", sans-serif; /* 设置为宋体 */
    font-size: 20px;
  }
  .status {
  margin: 20px 0;
  color: #666;
}

progress {
  display: block;
  width: 300px;
  margin-top: 10px;
}

.results {
  margin-top: 20px;
  padding: 10px;
  border: 1px solid #eee;
}

/* 布局优化样式 */
.jinghua-container {
  padding: var(--spacing-md);
  max-width: 100%;
  overflow-x: auto;
}

/* 表格样式优化 */
.modern-table {
  width: 100%;
  font-size: var(--font-size-sm);
}

.item-name-cell {
  max-width: 100%;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.item-name {
  font-weight: 500;
  color: var(--text-primary);
}

.price-cell {
  font-weight: 600;
  color: var(--primary-color);
}

.trade-link {
  display: inline-block;
  transition: var(--transition-fast);
}

.trade-link:hover {
  transform: scale(1.1);
}

.trade-icon {
  width: 24px;
  height: 24px;
  border-radius: var(--border-radius-small);
}

.quantity-input {
  width: 80px;
}

/* 统计卡片样式 */
.statistics-row {
  margin: var(--spacing-lg) 0;
}

.statistic-card {
  background: linear-gradient(135deg, var(--primary-color), var(--primary-light));
  color: white;
  border-radius: var(--border-radius-large);
  padding: var(--spacing-md);
  text-align: center;
  box-shadow: var(--shadow-base);
  transition: var(--transition-base);
  margin-bottom: var(--spacing-sm);
}

.statistic-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-dark);
}

.statistic-subtitle {
  font-size: var(--font-size-sm);
  opacity: 0.9;
  margin-top: var(--spacing-xs);
}

/* 输入组样式 */
.input-row {
  margin: var(--spacing-md) 0;
}

.input-group {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-xs);
}

.input-label {
  font-size: var(--font-size-sm);
  font-weight: 500;
  color: var(--text-primary);
  margin-bottom: var(--spacing-xs);
}

/* 收益卡片样式 */
.revenue-row {
  margin: var(--spacing-md) 0;
}

.revenue-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border-light);
  border-radius: var(--border-radius-large);
  padding: var(--spacing-md);
  text-align: center;
  box-shadow: var(--shadow-light);
  transition: var(--transition-base);
}

.revenue-card:hover {
  transform: translateY(-1px);
  box-shadow: var(--shadow-base);
}

.revenue-subtitle {
  font-size: var(--font-size-sm);
  color: var(--text-secondary);
  margin-top: var(--spacing-xs);
}

/* 右侧卡片区域 */
.section-header {
  font-size: var(--font-size-xl);
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: var(--spacing-lg);
  text-align: center;
}

.cards-container {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-md);
}

.card-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: var(--spacing-sm);
}

.card-title {
  font-size: var(--font-size-base);
  font-weight: 600;
  color: var(--text-primary);
  flex: 1;
  min-width: 200px;
}

.card-actions {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
}

.input-action {
  display: flex;
  align-items: center;
}

.action-input {
  width: 120px;
}

/* 响应式设计 */
@media (max-width: 1200px) {
  .jinghua-container {
    padding: var(--spacing-sm);
  }
  
  .el-col {
    margin-bottom: var(--spacing-md);
  }
}

@media (max-width: 768px) {
  .jinghua-container {
    padding: var(--spacing-sm);
  }
  
  .filter-button {
    height: 40px;
    font-size: var(--font-size-base);
    margin-bottom: var(--spacing-sm);
  }
  
  .statistic-card {
    padding: var(--spacing-sm);
    margin-bottom: var(--spacing-sm);
  }
  
  .card-content {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .card-title {
    min-width: auto;
    margin-bottom: var(--spacing-sm);
  }
  
  .section-header {
    font-size: var(--font-size-lg);
  }
}

@media (max-width: 480px) {
  .filter-button {
    height: 35px;
    font-size: var(--font-size-sm);
  }
  
  .statistic-card {
    padding: var(--spacing-xs);
  }
  
  .section-header {
    font-size: var(--font-size-base);
  }
  
  .action-input {
    width: 100px;
  }
}
  </style>
  