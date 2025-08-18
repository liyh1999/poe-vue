from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import numpy as np
import re
import gc
import requests  # 如果需要请求外部API
from urllib.parse import quote
app = Flask(__name__)
CORS(app)  # 允许所有前端跨域访问
import json
# 精华名称列表
essence_names = [
    "贪婪", "轻视", "憎恨", "悲痛", "恐惧", "愤怒", "折磨", "哀惜", "肆虐", "苦难",
    "雷霆", "疑惑", "厌恶", "热情", "煎熬", "刻毒", "傲视", "忌妒", "凄惨", "忌惮"
]

@app.route("/upload", methods=["POST"])
def upload_image():
    try:
        if "image" not in request.files:
            return jsonify({"success": False, "error": "未上传文件"})

        file = request.files["image"]
        with Image.open(file.stream) as img:
            img_resized = img.resize((600, 600))

            regions = [(23, 23, 70, 577), (530, 23, 577, 577)]
            text_results = []

            from paddleocr import PaddleOCR
            ocr = PaddleOCR(use_angle_cls=True, lang="en", rec_char_type="en", rec_algorithm="CRNN", det_db_box_thresh=0.3)

            for idx, (left, top, right, bottom) in enumerate(regions):
                img_cropped = img_resized.crop((left, top, right, bottom))
                height = img_cropped.height
                line_height = height // 12

                for i in range(12):
                    top_crop = i * line_height
                    bottom_crop = (i + 1) * line_height if i < 11 else height
                    cropped_img = img_cropped.crop((0, top_crop, img_cropped.width, bottom_crop))

                    scale_factor = 24
                    sr_img = cropped_img.resize((cropped_img.width * scale_factor, cropped_img.height * scale_factor), Image.LANCZOS)

                    result = ocr.ocr(np.array(sr_img), cls=True)

                    if result and result != [None]:
                        line_text = "".join([line[1][0] for res in result for line in res])
                        filtered_text = re.match(r"\d*", line_text).group(0)
                        text_results.append(filtered_text.strip())
                    else:
                        text_results.append("0")

                    del cropped_img, sr_img, result
                    gc.collect()

            del ocr
            gc.collect()

        formatted_results = [{f"{name}之破空精华": text_results[i] if i < len(text_results) else "0"} for i, name in enumerate(essence_names)]
        print(formatted_results)
        return jsonify({"success": True, "text_results": formatted_results})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

    finally:
        gc.collect()

# ✅ 新增接口：接收前端 username + possid
@app.route("/process_user_info", methods=["POST"])
@app.route("/process_user_info", methods=["POST"])
def process_user_info():
    try:
        data = request.get_json()
        username = data.get("username")
        possid = data.get("possid")  # 实际上是一整串cookie字符串
        if not username or not possid:
            return jsonify({"success": False, "error": "参数不完整"})
        print(f"[INFO] 收到用户请求：username={username}, possid={possid}")
        # 转换 cookie 字符串为字典
        def parse_cookie_string(cookie_str):
            cookies = {}
            for pair in cookie_str.split(';'):
                if '=' in pair:
                    key, value = pair.strip().split('=', 1)
                    cookies[key] = value
            return cookies
        cookies = parse_cookie_string(possid)
        # 构建请求
        encoded_username = quote(username, encoding='utf-8')
        url = f'https://poe.game.qq.com/character-window/get-stash-items?accountName={encoded_username}&realm=pc&league=S26赛季&tabs=1&tabIndex=0'
        response = requests.get(url, cookies=cookies)
        if response.status_code != 200:
            return jsonify({"success": False, "error": f"请求失败，状态码：{response.status_code}"}), 500
        data = json.loads(response.text)
        # 提取 items 部分
        for item in data["tabs"]:
            if item.get("type") == "EssenceStash":
                ES_url=f'https://poe.game.qq.com/character-window/get-stash-items?accountName={encoded_username}&realm=pc&league=S26赛季&tabs=1&tabIndex={item.get("i")}'
        ES_response = requests.get(ES_url, cookies=cookies)
        ES_data=json.loads(ES_response.text)
        ES_items_data = ES_data["items"]
        essence_result = []
        for item in ES_data.get("items", []):
            base_type = item.get("baseType", "")
            # 只保留含 “破空精华” 的项
            if "破空精华" not in base_type:
                continue
            # 初始化数量
            count = 0
            # 查找 “堆叠数量” 属性
            properties = item.get("properties", [])
            for prop in properties:
                if prop.get("name") == "堆叠数量":
                    values = prop.get("values", [])
                    if values and isinstance(values[0][0], str):
                        stack_str = values[0][0]  # e.g., "87 / 9"
                        match = re.match(r"(\d+)", stack_str)
                        if match:
                            count = int(match.group(1))
                    break
            # 添加到结果数组
            essence_result.append({
                "name": base_type,
                "count": count
            })
        #然后从result_data里找到精华仓库是那个，再次发申请
        return jsonify({"success": True, "essences": essence_result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True, ssl_context=('/www/wwwroot/poe/cert.pem', '/www/wwwroot/poe/key.pem'))
