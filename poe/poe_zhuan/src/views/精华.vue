<template>
    <el-row :gutter="20">
      <el-col :span="8">
        <el-button type="text" class="custom-button" @click="filterlowItems">低价精华</el-button>
      </el-col>
      <el-col :span="8">
        <el-button type="text" class="custom-button" @click="filterhighItems">高价精华</el-button>
      </el-col>
      <el-col :span="8">
        <el-button type="text" class="custom-button" @click="filterallItems">全部精华</el-button>
      </el-col>
    </el-row>
  
    <el-row :gutter="80" class="custom-row">
      <el-col :span="8">
        <el-table v-if="filteredItems.length > 0" :data="filteredItems" border>
          <el-table-column prop="name" label="名称" min-width/>
          <el-table-column prop="calculated" label="价格" sortable min-width="60"/>
          <el-table-column label="购买链接" min-width="40">
                <template #default="{ row }">
                    <a :href="'https://poe.game.qq.com/trade/search/S26赛季/' + row.searchCode" target="_blank" rel="noopener noreferrer">
                    <img :src="row.icon" alt="icon" class="icon" style="width: 30px; height: auto;" />
                    </a>
                </template>
                </el-table-column>
          <el-table-column label="数量">
            <template #default="{ row }">
              <el-input v-model="row.customQuantity" type="number" placeholder="请输入数量" />
            </template>
          </el-table-column>
        </el-table>
        <div v-else>没有找到符合条件的项。</div>

        <el-row :gutter="20">
          <el-col :span="8"><div class="grid-content ep-bg-purple" />
            <el-statistic title="当前转化预期收益" :value="`${shouyi.toFixed(2)}C`" />
            <div :style="{ marginLeft: '15px' }">{{ (shouyi/shensheng).toFixed(2) }}D</div>
          </el-col>
          <el-col :span="6"><div class="grid-content ep-bg-purple" />
            <el-statistic title="当前精华总成本" :value="`${chengben.toFixed(2)}C`" />
            <div :style="{ marginLeft: '15px' }">{{ (chengben/shensheng).toFixed(2) }}D</div>
          </el-col>
          <el-col :span="6"><div class="grid-content ep-bg-purple" />
            <el-statistic title="当前命能总成本" :value="`${mingneng_chengben.toFixed(2)}C`" />
            <div :style="{ marginLeft: '15px' }">{{ (mingneng_chengben/shensheng).toFixed(2) }}D</div>
          </el-col>
          <el-col :span="4"><div class="grid-content ep-bg-purple" />
            <el-statistic title="利润空间" :value="`${(lirun * 100).toFixed(2)}%`" />
          </el-col>
        </el-row>

          <el-row :gutter="20">
            <el-col :span="8"><div class="grid-content ep-bg-purple" />
              <div class="input-item">
                <div class="label">每图精华数</div>
                <el-input
                  v-model.number="valueA"
                  type="number"
                  placeholder="请输入数字"
                 
                />
              </div>
            </el-col>
            <el-col :span="8"><div class="grid-content ep-bg-purple" />
              <div class="input-item">
                <div class="label">每图成本(C)</div>
                <el-input
                  v-model.number="valueB"
                  type="number"
                  placeholder="请输入数字"
                 
                />
              </div>
            </el-col>
            <el-col :span="8"><div class="grid-content ep-bg-purple" />
              <div class="input-item">
                <div class="label">每图时间(S)</div>
                <el-input
                  v-model.number="valueC"
                  type="number"
                  placeholder="请输入数字"
               
                />
              </div>
            </el-col>
          </el-row>
          <el-row :gutter="20">
          <el-col :span="8"><div class="grid-content ep-bg-purple" />
            <el-statistic title="每图收益" :value="`${(meitu_shouyi).toFixed(2)}C`" />
            <div :style="{ marginLeft: '15px' }">{{ (meitu_shouyi/shensheng).toFixed(2) }}D</div>
          </el-col>
          <el-col :span="8"><div class="grid-content ep-bg-purple" />
            <el-statistic title="每小时收益" :value="`${meixiaoshi_shouyi.toFixed(2)}C`" />
            <div :style="{ marginLeft: '15px' }">{{ (meixiaoshi_shouyi/shensheng).toFixed(2) }}D</div>
          </el-col>
          <el-col :span="8"><div class="grid-content ep-bg-purple" />
            <el-statistic title="转化后小时收益" :value="`${(meixiaoshi_shouyi+shouyi).toFixed(2)}C`" />
            <div :style="{ marginLeft: '15px' }">{{ ((meixiaoshi_shouyi+shouyi)/shensheng).toFixed(2) }}D</div>
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
        <div class="header">转精华收益计算</div> <!-- 添加表头 -->
        <el-card class="custom-card" v-for="(item, index) in saying" :key="index">
          <div class="card-content">
            <div class="title2">{{ item.title }}</div>
            <div class="description" v-if="index === 0" style="display: flex; justify-content: flex-end; align-items: center;">
              <el-input 
                v-model="shensheng" 
                style="width: 120px; font-size: 24px;margin-left:700px" 
                size="small"
              />
            </div>
            <div class="description" v-if="index === 1" style="display: flex; justify-content: flex-end; align-items: center;">
              <el-input 
                v-model="mingneng" 
                style="width: 120px; font-size: 24px;margin-left:620px" 
                size="small"
              />
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
      </el-col>
    </el-row>
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
      form: {
        username: '',
        possid: ''
      },
      formLabelWidth: '80px',
      index: 3, // 确保 index===3 渲染此段内容
      };
    },
    watch: {
    // 监听值的变化并更新计算
    valueA: 'fetchData',
    valueB: 'fetchData',
    valueC: 'fetchData',
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
            try {
                const response = await fetch('/jinghua.json'); // 替换为你的 JSON 路径
                if (!response.ok) throw new Error('网络响应不正常');
                const data = await response.json();
                this.items = data; // 存储 JSON 数据
                const maxCalculated = parseFloat(this.input); // 获取输入的数字
                this.filteredItems = this.items.filter(item => 
                item.name.includes('破空精华') && item.calculated < maxCalculated,
                );
                this.filteredhighItems = this.items.filter(item => 
                item.name.includes('破空精华') && item.calculated > maxCalculated,
                );
                this.filteredlowItems = this.items.filter(item => 
                    item.name.includes('破空精华') && item.calculated < maxCalculated,
                );
                this.filteredallItems = this.items.filter(item => 
                item.name.includes('破空精华') && item.calculated 
                 );
                 const average =
                this.filteredallItems.reduce((sum, item) => sum + item.calculated , 0) /
                this.filteredallItems.length;
                this.meitu_shouyi=average*this.valueA-this.valueB
                this.meixiaoshi_shouyi=this.meitu_shouyi/this.valueC*3600
                this.newQuantity=this.valueA/this.valueC*3600/20
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
            }
        },
        filterlowItems() 
        {
            const maxCalculated = parseFloat(this.input); // 获取输入的数字
            if (isNaN(maxCalculated)) return; // 如果输入不是数字，直接返回
            this.filteredItems = this.items.filter(item => 
                item.name.includes('破空精华') && item.calculated < maxCalculated,
            );
        },
        filterhighItems() 
        {
            const maxCalculated = parseFloat(this.input); // 获取输入的数字
            if (isNaN(maxCalculated)) return; // 如果输入不是数字，直接返回
            this.filteredItems = this.items.filter(item => 
                item.name.includes('破空精华') && item.calculated > maxCalculated,
            );
        },
        filterallItems() 
        {
            const maxCalculated = parseFloat(this.input); // 获取输入的数字
            if (isNaN(maxCalculated)) return; // 如果输入不是数字，直接返回
            this.filteredItems = this.items.filter(item => 
                item.name.includes('破空精华') && item.calculated 
            );
        },
        calculateConversionProfit() {
        let totalProfit = 0;
        let total_chengben=0
        let total_mingneng_chengben=0
        // 遍历 filteredItems 中的每个项目
        for (const item of this.filteredItems) 
        {
            let total=0;
            const itemPrice = item.calculated;  
            total_chengben+=itemPrice*item.customQuantity
            total_mingneng_chengben+=item.customQuantity*1/(this.filteredItems.length/20)*this.mingneng
            // 遍历 filteredHighItems 中的每个高价项目
            for (const highItem of this.filteredhighItems) 
            {
                const highPrice = highItem.calculated;  
                // 计算价格差
                const priceDifference = highPrice - itemPrice;
                // 计算收益
                const profit = (priceDifference - this.mingneng) / 20
                // 累加到总收益
                total += profit;
            }
            totalProfit+=(total-this.filteredItems.length/20*this.mingneng)*item.customQuantity
        }
        this.chengben=total_chengben
        this.shouyi=totalProfit
        this.mingneng_chengben=total_mingneng_chengben
        this.lirun=totalProfit/(total_chengben+total_mingneng_chengben)
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
          fetch('https://47.117.185.5:5002/process_user_info', {
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
  .custom-button {
    border: none; /* 去掉边框 */
    color: rgb(4, 4, 4); /* 字体颜色 */
    background-color: transparent; /* 背景透明 */
    font-size: 40px;
    font-family: "SimSun", "宋体", sans-serif; /* 设置为宋体 */
  }
  .custom-row {
    margin-top: 20px; /* 根据需要调整间距 */
  }
  .custom-card {
    margin-bottom: 0; /* 设置卡片间距 */
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
  </style>
  