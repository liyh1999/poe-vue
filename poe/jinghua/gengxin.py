import base64
import gzip
import io
import json
import os
import requests

def decompress_and_parse(compressed_base64_data):
    try:
        # 去除空白字符，过滤非法字符
        compressed_base64_data = compressed_base64_data.strip()
        compressed_base64_data = compressed_base64_data.encode('ascii', 'ignore').decode('ascii')

        # base64 解码
        compressed_bytes = base64.b64decode(compressed_base64_data)

        # gzip 解压
        with gzip.GzipFile(fileobj=io.BytesIO(compressed_bytes), mode='rb') as f:
            decompressed_bytes = f.read()

        # 转为字符串并解析 JSON
        decompressed_json = decompressed_bytes.decode('utf-8')
        decompressed_data = json.loads(decompressed_json)
        return decompressed_data

    except Exception as e:
        print(f"解析数据时出错: {e}")
        raise e

# 目标文件 URL 和保存路径
url = "http://cf.981001.xyz/price2.txt"
save_dir = "/www/wwwroot/poe/jinghua"
save_path = os.path.join(save_dir, "price_data_赛季.json")

try:
    # 下载文件内容
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = 'utf-8'
    compressed_data = response.text

    # 解压并解析
    price_json = decompress_and_parse(compressed_data)

    # 保存 JSON 文件
    os.makedirs(save_dir, exist_ok=True)
    with open(save_path, "w", encoding="utf-8") as json_file:
        json.dump(price_json, json_file, ensure_ascii=False, indent=4)

    print("更新完成 ✅ 数据已保存至：", save_path)

except requests.RequestException as req_err:
    print(f"请求失败: {req_err}")
except Exception as e:
    print(f"处理过程中出错: {e}")
