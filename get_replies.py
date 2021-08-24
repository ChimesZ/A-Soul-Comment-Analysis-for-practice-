import requests
import json
import time

headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }


url1 = 'https://api.bilibili.com/x/v2/reply/main?next='
url2 = '&type=1&oid=797915674&mode=3&plat=1'

def get_json(url1,url2):
    replies = []
    for page in range(1,250):
        r = requests.get(url1 + str(page) + url2)
        r_json = r.json()
        if r_json['data']['replies'] != None:
            replies += r_json['data']['replies']
            time.sleep(3)
        else:
            break
    return replies

def write_replies(replies):
    with open('replies.json','w',encoding='utf-8') as f:
        f.write(json.dumps(replies,indent=1,ensure_ascii=False))

if __name__ == '__main__':
    write_replies(get_json(url1,url2))

