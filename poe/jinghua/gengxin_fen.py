import json
import os

# 读取 disenchant_items.json（原始）
with open("./disenchant_items.json", "r", encoding="utf-8") as f:
    disenchant_data = json.load(f)

# 如果更新后的 json 已存在，优先读取它作为 base 数据
updated_file = "/www/wwwroot/poe/poe_zhuan/public/disenchant_items_updated.json"
if os.path.exists(updated_file):
    with open(updated_file, "r", encoding="utf-8") as f:
        disenchant_data = json.load(f)
    print("读取已存在的 disenchant_items_updated.json 进行更新...")

# 读取 item.json
with open("./price_data_赛季.json", "r", encoding="utf-8") as f:
    item_data = json.load(f)

# 构建 name -> {calculated, icon, count, searchCode} 映射
item_map = {
    item["name"]: {
        "calculated": item.get("calculated"),
        "icon": item.get("icon"),
        "count": item.get("count"),
        "searchCode": item.get("searchCode")
    }
    for item in item_data
}

# 更新 disenchant_data 中每个 item
for item in disenchant_data:
    name = item.get("name")
    if name in item_map:
        # 更新非空字段
        for key, value in item_map[name].items():
            if value is not None:
                item[key] = value

        # 更新 url 字段，如果存在 searchCode 则替换url为新链接
        search_code = item_map[name].get("searchCode")
        if search_code:
            base_url = "https://poe.game.qq.com/trade/search/S27%E8%B5%9B%E5%AD%A3/"
            item["url"] = base_url + search_code

# 保存更新后的数据
with open(updated_file, "w", encoding="utf-8") as f:
    json.dump(disenchant_data, f, ensure_ascii=False, indent=2)

print("更新完成，已保存为 disenchant_items_updated.json")
