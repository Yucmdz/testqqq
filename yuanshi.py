import requests
import json

# 构造POST请求的数据
url = 'https://nsiscp.jscert.cn:8078/api/activity/EFF4104CE81487E73BE383FE89FD825C/asset/white_list'
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC8xMjcuMC4wLjE6MTAwMDFcL2FwaVwvYXV0aFwvbG9naW4iLCJpYXQiOjE2ODYwMTQyNzMsImV4cCI6MTY4NjEwMDY3MywibmJmIjoxNjg2MDE0MjczLCJqdGkiOiI0RHV4cHF4cER0THB0d3R5Iiwic3ViIjoiNzYxQkQzMEYyRURENTMxNUYyQkM0QkY4QTI1MEQxRDMiLCJwcnYiOiIyM2JkNWM4OTQ5ZjYwMGFkYjM5ZTcwMWM0MDA4NzJkYjdhNTk3NmY3In0.iFj7a2jHXdk2Uu3zeCQNhUPAkuJ6p4V2ZuySzX3HUyA',
    'Cookie': '1'
}
# 5-10  填4-11  
for page in range(1,11):
    data = {
        'page': str(page),
        'pageSize': '50',
        'assetUrl': '',
        'findType': '',
        'startTime': '',
        'endTime': ''
    }
    response = requests.post(url, headers=headers, data=data)
    response_json = json.loads(response.text)
    with open("资产.txt", "a", encoding="utf-8") as f:
        for item in response_json['data']['list']:
            asset_url = item['assetUrl']
            f.write(f"{asset_url}\n")