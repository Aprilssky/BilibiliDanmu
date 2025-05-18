def search_user_from_log(username):
    """
    根据用户名从 danmu.log 文件中搜索相关记录。

    参数:
        username (str): 要搜索的用户名。

    返回:
        list: 包含匹配记录的列表，每条记录为字符串格式。
    """
    matched_records = []

    try:
        # 打开 danmu.log 文件进行读取
        with open('danmu.log', 'r', encoding='utf-8') as file:
            for line in file:
                # 检查行中是否包含指定的用户名
                if f'随机用户: {username}' in line:
                    matched_records.append(line.strip())
    except FileNotFoundError:
        print("错误：文件 'danmu.log' 未找到，请确保文件存在且路径正确。")
    except Exception as e:
        print(f"发生错误：{e}")

    return matched_records
