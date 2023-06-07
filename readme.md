[python3文档](https://docs.python.org/zh-cn/3/tutorial/index.html)
[python文档](https://www.liaoxuefeng.com/wiki/1016959663602400)

[selenium文档](https://www.selenium.dev/zh-cn/documentation/webdriver/getting_started/upgrade_to_selenium_4/)

# 查看google版本
`chrome://version`

# 安装对应chormDrive
[chromDrive下载地址](https://sites.google.com/chromium.org/driver/?pli=1)


# 支持的选择器属性

- ID
- XPATH 
- LINK_TEXT 
- PARTIAL_LINK_TEXT 
- NAME 
- TAG_NAME
- CLASS_NAME 
- CSS_SELECTOR

# 使用方式
    `
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By
        
        images = driver.find_elements(By.XPATH, "//img")
        id = driver.find_element(By.ID, "demo")
    `

# 使用场景
### cookie
### 窗口
### 标签页
### frame

[scrapy](https://docs.pythontab.com/scrapy/scrapy0.24/intro/overview.html)

# App 爬虫
- [爬虫思路分析](https://zhuanlan.zhihu.com/p/343303142)
- [airtest框架文档](https://airtest.doc.io.netease.com/)
- [Appium框架](https://www.kancloud.cn/testerhome/appium_docs_cn/2001595)
- [爬虫工程师成长路径](https://cuiqingcai.com/9075.html)
- [AirtestIDE安装](https://airtest.netease.com/download.html?download=mac/AirtestIDE-mac-1.2.15.dmg&&site=io)
- [adb安装工具集安装](https://developer.android.com/studio/releases/platform-tools?hl=zh-cn)
- [adb使用文档](https://developer.android.com/studio/command-line/adb.html?hl=zh-cn)
- 手机设置开发者模式（设置->系统和更新->开发人员选项->调试->USB调试）
- [airtest快速上手](https://airtest.readthedocs.io/zh_CN/latest/README_MORE.html)
- [airtest api](https://airtest.readthedocs.io/zh_CN/latest/all_module/airtest.core.api.html)

# App 自动化
- uiautomator
- [下载andrio工具包 - Command line tools only](https://developer.android.com/studio)
    `
        pip3 install uiautomator
        brew install openjdk
        添加环境变量
        vim ~/.zshrc
        export PATH="/usr/local/opt/openjdk/bin:$PATH"
    `
- Airtest
- Poco

  `
      # 选择Android模式时，AirtestIDE自动插入的初始化语句
    
      from poco.drivers.android.uiautomation import AndroidUiautomationPoco
      poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    
      # 点击设置图标
      poco(desc="设置").click()
  `
- [Airtest爬虫应用](https://zhuanlan.zhihu.com/p/55266133)
- [爬虫书籍](https://item.jd.com/12436581.html?dist=jd)

# 整体思路整理
1. 判断是否能直接抓取数据（ajax），带着cookie及header信息
   - charles使用，google network查看
   - 数据加密不可使用
   - 有验签流程不可用
   - 不发起ajax请求不可用
2. 判断使用selenium抓取数据（web）
   - 设置WebDeriverWait(driver, 30).Until(EC.presence_of_element_located((By.CLASS_NAME, "content")))
   - 设置agent
   - 设置proxy
3. 判断使用airtest抓取数据（app）

- 封装框架
  - agent
  - proxy
  - mysql
  - redis
  - 传参
  - cookie
  - 维护一个proxy库
  - 获取房价的爬虫
  - 各资讯网站抓取关键词的讯息
  - 各个网站的抓取示意
  - 抓取指定类目商品信息
  - PhantomJS?