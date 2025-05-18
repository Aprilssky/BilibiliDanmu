from searchuser import search_user_from_log
from listenDanmu import Danmu

# 使用示例
if __name__ == "__main__":
    room_id = 3137024  # 替换为实际的房间号
    danmu = Danmu(room_id)
    danmu.get_danmu()

    user_to_search = "随机用户"
    results = search_user_from_log(user_to_search)
    if results:
        print(f"找到 {len(results)} 条与用户 '{user_to_search}' 相关的记录：")
        for record in results:
            print(record)
    else:
        print(f"未找到与用户 '{user_to_search}' 相关的记录。")
