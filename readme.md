[python3文档](https://docs.python.org/zh-cn/3/tutorial/index.html)

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