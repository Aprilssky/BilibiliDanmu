import requests
import time

# B站获取弹幕对象
class Danmu():
    def __init__(self, room_id):
        # 弹幕url
        self.url = 'https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory'
        # 请求头
        self.headers = {
            'Host': 'api.live.bilibili.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
        }
        # 定义POST传递的参数
        self.data = {
            'roomid': room_id,
            'csrf_token': '',
            'csrf': '',
            'visit_id': '',
        }
        # 读取日志
        try:
            with open('danmu.log', mode='r', encoding='utf-8') as file:
                self.log = file.readlines()
        except FileNotFoundError:
            self.log = []

    def get_danmu(self):
        while True:
            try:
                # 获取直播间弹幕
                html = requests.post(url=self.url, headers=self.headers, data=self.data).json()
                # 解析弹幕列表
                for content in html['data']['room']:
                    # 获取昵称
                    nickname = content['nickname']
                    # 获取发言
                    text = content['text']
                    # 获取发言时间 HH:mm:ss
                    timeline = content['timeline'].split(" ")[1]
                    # 记录发言
                    msg = timeline + ' ' + nickname + ': ' + text
                    # 判断对应消息是否存在于日志，如果不存在则打印并保存
                    if msg + '\n' not in self.log:
                        print(msg)
                        # 保存日志
                        with open('danmu.log', mode='a', encoding='utf-8') as log_file_write:
                            log_file_write.write(msg + '\n')
                        # 添加到日志列表
                        self.log.append(msg + '\n')
                # 暂停1秒防止cpu占用过高
                time.sleep(1)
            except requests.exceptions.RequestException as e:
                print(f"网络异常，正在重试...: {e}")
                time.sleep(5)  # 等待5秒后重试

# 使用示例
if __name__ == "__main__":
    room_id = 3137024  # 替换为实际的房间号
    danmu = Danmu(room_id)
    danmu.get_danmu()
