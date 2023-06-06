import os
from selenium import webdriver
from selenium.webdriver.common.by import By
def download_image(url, save_directory):
    driver = webdriver.Chrome()
    driver.get(url)

    # 创建目录用于保存下载的图片
    os.makedirs(save_directory, exist_ok=True)

    # 获取图片元素
    img_element = driver.find_element(By.CLASS_NAME, "artCont")

    img_fz = img_element.find_elements(By.TAG_NAME, "li")
    for tp in img_fz:
        tp.find_element(By.TAG_NAME, "img")
        image_url = img_element.get_attribute("src")
        #记录image_url内容
        print(image_url)

        if image_url:
        # 下载图片到指定目录
            save_path = os.path.join(save_directory, "image.png")
            driver.execute_script(f"arguments[0].setAttribute('download', '{save_path}');", img_element)
            img_element.screenshot(save_path)
            print(f"Downloaded image: {save_path}")

    # 获取图片链接


    driver.quit()

if __name__ == "__main__":
    url = "https://www.woyaogexing.com/touxiang/katong/2023/1284241.html"  # 替换为您要抓取图片的页面链接
    save_directory = "./head/"  # 替换为保存图片的目录
    download_image(url, save_directory)
