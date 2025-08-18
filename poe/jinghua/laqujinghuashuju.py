import json

# 定义读取和写入的文件路径
input_file_path = r'/www/wwwroot/poe/jinghua/price_data_赛季.json'
output_file_path = r'/www/wwwroot/poe/poe_zhuan/public/jinghua.json'

# 定义要检查的字符
target_char_1 = '原始蓝晶命能'
target_char_2 = '钙化'
target_char_3 = '应变'
target_char_4 = '升格'
target_char_5 = '强敌'
target_char_6 = '破空精华'
target_char_7 = '神圣石'

def filter_items(input_path, output_path, target_char_1, target_char_2, target_char_3, target_char_4, target_char_5, target_char_6, target_char_7):
    try:
        # 读取 JSON 文件
        with open(input_path, 'r', encoding='utf-8') as infile:
            data = json.load(infile)
        # 确保数据是一个列表
        if not isinstance(data, list):
            raise ValueError('JSON 数据的根元素应该是一个列表')
        # 过滤：包含任意目标字符串，且 calculated 字段不为 0
        filtered_items = [
            item for item in data
            if (
                any(target in item.get('name', '') for target in [
                    target_char_1, target_char_2, target_char_3,
                    target_char_4, target_char_5, target_char_6, target_char_7
                ])
                and item.get('calculated', 0) != 0
            )
        ]
        # 写入过滤结果
        with open(output_path, 'w', encoding='utf-8') as outfile:
            json.dump(filtered_items, outfile, ensure_ascii=False, indent=2)

    except Exception as e:
        print(f'处理文件时出错: {e}')


# 调用函数
filter_items(
    input_file_path, output_file_path,
    target_char_1, target_char_2, target_char_3,
    target_char_4, target_char_5, target_char_6, target_char_7
)
print("价格写入")
