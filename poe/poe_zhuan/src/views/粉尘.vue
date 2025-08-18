<template>
  <main class="min-h-screen bg-gray-50 p-6">
    <section class="max-w-7xl mx-auto">
      <h1 class="text-3xl font-bold mb-6 text-center text-gray-800">分解物品表格展示</h1>

      <div class="overflow-x-auto">
        <table class="min-w-full bg-white shadow rounded-xl overflow-hidden">
          <thead class="bg-gray-200 text-gray-700 text-left text-sm uppercase">
            <tr>
              <th class="p-3">名称</th>
              <th class="p-3">图标</th>
              <th class="p-3">
                粉尘数量
                <input
                  v-model.number="threshold"
                  type="number"
                  placeholder="筛选..."
                  class="mt-1 block w-full px-2 py-1 text-sm border rounded focus:outline-none focus:ring"
                />
              </th>
              <th class="p-3">价格</th>
              <th class="p-3 cursor-pointer" @click="toggleSortOrder">
                性价比
                <span v-if="sortOrder === 'desc'">⬇️</span>
                <span v-else>⬆️</span>
              </th>
              <th class="p-3">市集数量</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="item in filteredSortedItems"
              :key="item.name"
              v-intersect="loadVisible"
              class="border-b hover:bg-gray-50"
            >
              <td class="p-3 font-medium text-gray-900">
                <a :href="item.url" target="_blank" rel="noopener" class="hover:underline">
                  {{ item.name }}
                </a>
              </td>
              <td class="p-3">
                <img
                  v-if="item._visible"
                  :src="item.icon"
                  alt="icon"
                  class="w-10 h-10 object-contain"
                />
              </td>
              <td class="p-3">{{ item.val_ilvl84 }}</td>
              <td class="p-3">{{ item.calculated }}</td>
              <td class="p-3 text-blue-600 font-semibold">
                {{ item._visible ? ratio(item).toFixed(2) : '...' }}
              </td>
              <td class="p-3">{{ item.count }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
  </main>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'

const items = ref([])
const threshold = ref(0)
const sortOrder = ref('desc') // 默认性价比降序排序

const ratio = (item) => {
  const dust = Number(item.val_ilvl84) || 0
  const price = Number(item.calculated)
  return price > 0 ? dust / price : 0
}

const filteredSortedItems = computed(() => {
  return items.value
    .filter((item) => Number(item.val_ilvl84) >= threshold.value)
    .sort((a, b) => {
      return sortOrder.value === 'desc'
        ? ratio(b) - ratio(a)
        : ratio(a) - ratio(b)
    })
})

const toggleSortOrder = () => {
  sortOrder.value = sortOrder.value === 'desc' ? 'asc' : 'desc'
}

const loadVisible = (entries, observer) => {
  for (const entry of entries) {
    if (entry.isIntersecting) {
      const name = entry.target.getAttribute('data-key')
      const item = items.value.find(i => i.name === name)
      if (item) item._visible = true
      observer.unobserve(entry.target)
    }
  }
}

onMounted(async () => {
  const res = await fetch('/disenchant_items_updated.json')
  const data = await res.json()
  console.log('样本数据:', data.slice(0, 3)) // ✅ 调试用
  items.value = data.map(item => ({ ...item, _visible: false }))
})
</script>

<script>
export default {
  directives: {
    intersect: {
      mounted(el, binding) {
        const observer = new IntersectionObserver(binding.value, {
          threshold: 0.1
        })
        el.setAttribute('data-key', el.__vnode.key)
        observer.observe(el)
      }
    }
  }
}
</script>

<style scoped>
table {
  border-collapse: collapse;
  width: 100%;
}
th, td {
  text-align: left;
  padding: 12px 16px;
}
th {
  background-color: #f4f4f4;
  font-weight: 600;
}
input[type="number"] {
  margin-top: 4px;
  width: 100%;
}
</style>