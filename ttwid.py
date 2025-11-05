import requests
import json


def get_douyin_ttwid():
    
    url = "https://ttwid.bytedance.com/ttwid/union/register/"
    
    payload = {
        "region": "cn",
        "aid": 1768,
        "needFid": False,
        "service": "www.douyin.com",
        "migrate_info": {"ticket": "", "source": "node"},
        "cbUrlProtocol": "https",
        "union": True
    }
    
    session = requests.Session()
    session.headers.update({
        "content-type": "application/json",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    })
    
    response = session.post(url, data=json.dumps(payload))
    return session.cookies.get("ttwid")


if __name__ == "__main__":
    ttwid = get_douyin_ttwid()
    print(f"ttwid: {ttwid}")