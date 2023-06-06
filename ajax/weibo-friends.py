import csv
import json
import requests

url = "https://weibo.com/ajax/friendships/friends?relate=fans&page=1&uid=1400854834&type=all&newFollowerCount=0"
cookie = "SINAGLOBAL=6388846971669.671.1634624892166; _s_tentry=www.baidu.com; UOR=passport.weibo.com,weibo.com,www.baidu.com; Apache=9101807223992.016.1684642898194; ULV=1684642898201:2:1:1:9101807223992.016.1684642898194:1682349465579; XSRF-TOKEN=kSMNG92OI8UomPN96SNFFa8T; login_sid_t=9749aec59a692c16a4ae0bcfc55c413e; cross_origin_proto=SSL; SCF=Ag0U1eymjSc7LtfIgfdRziPayL8nEH_oEQSuvr2kFZfD5AwUne9x8b4kP1kb00FB9fpJFs_nSkR0oDLkTzZD6hU.; PC_TOKEN=21401e0991; WBStorage=4d96c54e|undefined; wb_view_log=1920*10801; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF4k42dlb01gXGO12Ggl72Z5JpX5o275NHD95Q0So.EeK.7SKnEWs4DqcjT-NHVdrLKdgLj9PQt; SSOLoginState=1685638694; SUB=_2A25JfL52DeRhGeVI4lAQ-S7Jwz6IHXVqC6i-rDV8PUNbmtAGLVbMkW9NTBfPKl6d3Tnd_jyXIA7n6M7p8ysq4-gA; ALF=1717174694; WBPSESS=Dt2hbAUaXfkVprjyrAZT_N5DRzkxkwkj_Cp_s7fIZTY1te8Ep8go9d-vsd1zcu4DifrieGrJQAoM0dQ240CXPpmecrH8pFyN8IEer4TcIUOhydu6HHvMgU4C6E93s5K9SlOr8ApL0huSF9mZyC8ufcqndvIka2blPlmweaEXpFaxGZQvamdeCQgbS00ooIjMo1geZWrVcTN0rnMWGIdT3Q=="
headers = {
    "authority": "weibo.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "client-version": "v2.40.59",
    "cookie": cookie,
    "referer": "https://weibo.com/u/page/follow/1400854834?relate=fans",
    "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "server-version": "v2023.06.01.2",
    "traceparent": "00-453a5fc2f6791600027bc16cfb15a986-ad769601a9a833bf-00",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
    "x-xsrf-token": "kSMNG92OI8UomPN96SNFFa8T"
}

response = requests.get(url, headers=headers)
data = response.json()

users = data["users"]

with open("weibo_data.csv", mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["名字", "简介", "粉丝"])

    for user in users:
        name = user["name"]
        description = user["description"]
        followers_count = user["followers_count"]

        writer.writerow([name, description, followers_count])

print("数据已成功写入CSV文件。")
