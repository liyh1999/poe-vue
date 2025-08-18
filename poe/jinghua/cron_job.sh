#!/bin/bash

cd /www/wwwroot/poe/jinghua

LOG_FILE="/www/wwwroot/poe/jinghua/update_log.log"
NOW=$(date "+%Y-%m-%d %H:%M:%S")

{
    echo "=== [$NOW] 开始更新 ==="
    
    echo "执行 gengxin.py..."
    python3 gengxin.py
    if [ $? -eq 0 ]; then
        echo "gengxin.py 执行成功"
    else
        echo "gengxin.py 执行失败"
    fi

    echo "执行 laqujinghuashuju.py..."
    python3 laqujinghuashuju.py
    if [ $? -eq 0 ]; then
        echo "laqujinghuashuju.py 执行成功"
    else
        echo "laqujinghuashuju.py 执行失败"
    fi
    
echo "执行gengxinfen.py..."
    python3 gengxin_fen.py
    if [ $? -eq 0 ]; then
        echo "gengxinfen.py 执行成功"
    else
        echo "gengxinfen.py 执行失败"
    fi
    echo "=== [$NOW] 结束 ==="
    echo ""
} >> "$LOG_FILE" 2>&1
