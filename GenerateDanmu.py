# GenerateDanmu.py

import random
import time

def generate_random_danmu():
    """
    随机生成弹幕内容，并将其保存到 `danmu.log` 文件中。
    弹幕内容为随机字符串，并附加时间和唯一ID。
    """
    # 可选的弹幕词汇
    danmu_words = [
        "太棒了！", "666", "这波操作厉害了！", "学到了！", "感谢分享！",
        "继续加油！", "支持一下！", "不明觉厉！", "前排围观！", "精彩！"
    ]

    # 随机选择一条弹幕
    random_danmu = random.choice(danmu_words)

    # 当前时间戳
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    # 格式化弹幕信息
    msg = f"[{timestamp} 随机用户: {random_danmu}"

    # 将生成的弹幕写入到文件
    with open('danmu.log', 'a', encoding='utf-8') as f:
        f.write(msg + '\n')

    print(f"已生成弹幕: {msg}")

if __name__ == "__main__":
    for i in range(200):
        generate_random_danmu()