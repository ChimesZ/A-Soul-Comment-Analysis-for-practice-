import json
import time

def get_list(path):
    with open(path,'r',encoding='utf-8') as f:
        replies = json.load(f)
        f.close()
    return replies

def purify_list(raw_list):
    replies_list = []
    for i in range(0,len(raw_list)):
        reply = {}
        reply['User'] = {
            'uname':raw_list[i]['member']['uname'],
            'sex':raw_list[i]['member']['sex'],
            'level':raw_list[i]['member']['level_info']['current_level'],
            'pendant':raw_list[i]['member']['pendant']['name']
        }
        if raw_list[i]['member']['fans_detail'] != None:
            reply['User']['fans'] = {
                'name':raw_list[i]['member']['fans_detail']["medal_name"],
                'level':raw_list[i]['member']['fans_detail']['level']
            }
        else:
            reply['User']['fans'] = ""
        
        reply['content'] = raw_list[i]['content']['message']
        reply['date'] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(raw_list[i]['ctime']))
        reply['like'] = raw_list[i]['like']
        
        replies_list.append(reply)
    return replies_list
        
if __name__ == '__main__':
    replies = list(get_list('replies.json'))
    print(len(replies))
    with open('pure_replies.json','w',encoding='utf-8') as f:
        f.write(json.dumps(purify_list(replies),indent=1,ensure_ascii=False))

