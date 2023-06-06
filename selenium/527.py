import os
from selenium import webdriver

def save_images(url, save_directory):
    driver = webdriver.Chrome()
    driver.get(url)

    # 创建目录用于保存下载的图片
    os.makedirs(save_directory, exist_ok=True)

    # 获取所有图片元素
    img_elements = driver.find_elements("tag name", "img")

    # 遍历图片元素并保存图片
    for index, element in enumerate(img_elements):
        image_url = element.get_attribute("src")
        if image_url:
            # 检查图片元素的宽度是否大于0
            if element.size["width"] > 0:
                # 下载图片到指定目录
                save_path = os.path.join(save_directory, f"image_{index}.png")
                driver.execute_script(f"arguments[0].setAttribute('download', '{save_path}');", element)
                element.screenshot(save_path)
                print(f"Downloaded image: {save_path}")

    driver.quit()

if __name__ == "__main__":
    url = "https://www.woyaogexing.com/touxiang/katong/2023/1284241.html"  # 替换为您要抓取图片的链接
    save_directory = "./head/"  # 替换为保存图片的目录
    save_images(url, save_directory)
