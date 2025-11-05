# Douyin ttwid Generator

Get valid `ttwid` cookies from ByteDance's official endpoint. Required for making authenticated requests to Douyin (TikTok China) APIs.

## Quick Start

```bash
pip install requests
python ttwid.py
```

## Usage

```python
from ttwid import get_douyin_ttwid

# Get a fresh ttwid token
ttwid = get_douyin_ttwid()
print(f"ttwid: {ttwid}")

# Use in your requests
import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Cookie": f"ttwid={ttwid}"
}

response = requests.get("https://www.douyin.com/aweme/v1/web/aweme/detail/", headers=headers)
```

## What is ttwid?

`ttwid` is ByteDance's client authentication cookie. Without it, you'll get `403 Forbidden` errors when accessing Douyin APIs.

**Token format (URL-decoded):**
```
1|<base64_id>|<timestamp>|<signature>
```

**Example:**
```
1|z_Dh-7_b2gZ7TSpFniufNsf8GnZs2EqMgDo0mT2CTOU|1761838010|f80eea6f334a...
```

## How It Works

1. Calls `https://ttwid.bytedance.com/ttwid/union/register/`
2. Sends registration payload with `aid: 1768` (Douyin web)
3. Receives server-signed `ttwid` in response cookies
4. Token valid for 365 days

## Configuration

Modify the `aid` parameter for different ByteDance platforms:
- `1768` - Douyin web
- `6383` - Douyin live streaming  
- `1128` - Xigua Video
- `13` - Toutiao



## License

MIT

## Disclaimer

For educational and research purposes only. Respect ByteDance's Terms of Service.
