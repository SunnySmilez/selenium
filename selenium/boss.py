from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import requests
import http.client
import json

def webDriver():
    # 设置Chrome选项（可选）
    chrome_options = Options()
    # 以无头模式运行（可选）
    #chrome_options.add_argument("--headless")

    # 指定浏览器驱动路径
    driver_path = "/Users/zhouzhi/Downloads/chromedriver_mac64/chromedriver"  # 替换为你的ChromeDriver路径

    # 创建Chrome驱动程序的Service对象
    service = Service(driver_path)
    # 创建Chrome浏览器实例
    driver = webdriver.Chrome(service=service, options=chrome_options)

    #cookie_str="lastCity=101010100; sid=sem_pz_bdpc_dasou_title; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1685642512; wd_guid=7d78e58a-7e53-4896-a436-1798f8f68aa3; historyState=state; _bl_uid=h3lXOi92eRba8zr59bzgy8h83syw; boss_login_mode=sms; __zp_seo_uuid__=fed5f520-8ce7-4281-bdb5-91b2f8717e6b; __g=sem_pz_bdpc_dasou_title; wbg=0; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1686146762; wt2=DOvqNilJT2nGxJGYX_PWkwXRrUFLSsQFXwN3n1A8sECuK7o8eChkmvkuVVdYrbuN-_Qyax6ZUQmAJuYU7hOaHcw~~; __c=1685642512; __l=r=https%3A%2F%2Fwww.baidu.com%2Fother.php%3Fsc.060000jYAOcGJIMt0_-om_EGHrLK80DqcDyz9XFpu7Oc0dThZZ5ep6mC_R9RkiZU8zyd5HIiBbZRvcCOpTBNHZCRA5FH8GUs4diPy9337AP9tScMpU8Cdtt6hNAY4RpF5_MAa3Yoy8hBTMCNdQttMKtNjHRwUmNfshbAbP2M_m3G5apeweGFwtt--nnJyXFToJWBOlguzezktahY3-WHUB2QL9x2.7D_NR2Ar5Od663rj6t8AGSPticrtXFBPrM-kt5QxIW94UhmLmry6S9wiGyAp7BEIu80.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqmhq1Tqpkko60IgP-T-qYXgK-5H00mywxIZ-suHY10ZIEThfqmhq1Tqpkko60ThPv5H00IgF_gv-b5HDdPjf4PHTkrjR0UgNxpyfqnHRzn1mYnHc0UNqGujYknWDkrHRLr0KVIZK_gv-b5HDzrjcv0ZKvgv-b5H00pywW5R9awfKspyfqnfKWpyfqn1bs0APzm1YdP1fY%26dt%3D1685699427%26wd%3Dboss%25E7%259B%25B4%25E8%2581%2598%26tpl%3Dtpl_12826_31784_0%26l%3D1544957185%26ai%3D0_60872259_1_1%26us%3DlinkVersion%253D1%2526compPath%253D10036.0-10032.0%2526label%253D%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkType%253D%2526linkText%253DBOSS%2525E7%25259B%2525B4%2525E8%252581%252598%2525E2%252580%252594%2525E2%252580%252594%2525E6%252589%2525BE%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258ABOSS%2525E7%25259B%2525B4%2525E8%252581%252598%2525EF%2525BC%25258C&l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3Dpython%26city%3D100010000&s=3&g=%2Fwww.zhipin.com%2Fbeijing%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&friend_source=0&s=3&friend_source=0; __a=42993414.1685642512..1685642512.64.1.64.64; geek_zp_token=V1Qt4lF-z921ZgXdNhyRwdKiK47znSwg~~; __zp_stoken__=d333eOAxKewMFXjMMJ1RWXFhAeT86eQVdfF4%2FAxpVPzgAckooOUFhGmx9RQZrTVBlNm5HJA9dfhdvMFk8cFFfd1FjPD5eOz1RWw0zc0leRCcPCQMdDngIVUtdVGVVbXsudFd1X319CzwtfiU%3D"

    headers = {
        'authority': 'www.zhipin.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        #'cookie': cookie_str,
        'if-modified-since': 'Wed, 07 Jun 2023 12:14:45 GMT',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }

    for key, value in headers.items():
        driver.execute_cdp_cmd('Network.setExtraHTTPHeaders', {'headers': {key: value}})

    # 访问目标网页
    url = "https://www.zhipin.com/web/geek/job?query=%E8%BF%90%E8%90%A5&city=101010100"  # 替换为你要访问的JavaScript渲染页面的URL
    driver.get(url)
    time.sleep(2)
    # 等待页面加载完成（可选）
    wait = WebDriverWait(driver, 60)  # 设置等待时间，根据实际情况调整
    ajax_element = wait.until(EC.visibility_of_element_located((By.ID, "wrap")))

    data = ajax_element.text

    # 获取页面源代码
    print(data)
    # 在此处添加提取数据的逻辑，例如使用BeautifulSoup或lxml解析HTML

    # 关闭webdriver
    driver.quit()

def req():

    conn = http.client.HTTPSConnection("www.zhipin.com")

    headers = {
        'authority': 'www.zhipin.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': 'warlockjssdkcross=%7B%22distinct_id%22%3A%221859606b3bb196-0def5d919ebcae-17525635-2007040-1859606b3bcedb%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%221859606b3bb196-0def5d919ebcae-17525635-2007040-1859606b3bcedb%22%7D; sid=sem; __zp_seo_uuid__=e377195c-8fe4-4ecf-ae16-ac8cd9d1d0c1; __g=sem; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1685719840; wd_guid=43f002a0-ea2b-4016-82da-2ed2b6936b4f; historyState=state; _bl_uid=IOlvmiFLe0tqCh238mnCeXd4hwnw; __fid=dd5af575903bcd7006513463362f0ddf; lastCity=101010100; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1686208320; __zp_stoken__=3da3efH8mZB5ZaSgtc2tsNGM1QSlTEWIBcxBOWlonQS0PcygmFTRFKy9OLktFOnpgWn9fYH4AXQkkDD0AISVzYysRDkRpPRRsbXIhTxA7N0VjGB4ZdHQiHQttRiYCTBEuGEZtGwwGUANtTTk%3D; __c=1685719840; __l=r=https%3A%2F%2Fwww.google.com%2F&l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3D%25E8%25BF%2590%25E8%2590%25A5%26city%3D101010100&s=3&g=%2Fwww.zhipin.com%2Freturnee_jobs%2F%3Fka%3Dtab_overseas_click%26sid%3Dsem%26qudao%3Dgoogle_pc%26ad_group%3D%25E6%2589%25BE%25E5%25B7%25A5%25E4%25BD%259Cpc%25E5%258C%2597%25E7%25BE%258E01%26gclid%3DCjwKCAjwpuajBhBpEiwA_ZtfhZ3l-R4Xkg_UAHLkaQnc0h-qNRYZBzJwXYl-yvSeryK02m3pKrz2URoCowsQAvD_BwE&friend_source=0&s=3&friend_source=0; __a=16718020.1673259300.1673259300.1685719840.29.2.28.28',
        'referer': 'https://www.zhipin.com/web/geek/job?query=%E8%BF%90%E8%90%A5&city=101010100',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
                       '(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'),
        'x-requested-with': "XMLHttpRequest"
    }

    path = ("/wapi/zpgeek/search/joblist.json?scene=1&query=%E8%BF%90%E8%90%A5&city=101010100"
            "&experience=&payType=&partTime=&degree=&industry=&scale=&stage="
            "&position=&jobType=&salary=&multiBusinessDistrict=&multiSubway="
            "&page=1&pageSize=30")

    conn.request("GET", path, headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(json.loads(data.decode("utf-8")))

if __name__ == "__main__":
    req()