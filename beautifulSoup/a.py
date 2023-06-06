from bs4 import BeautifulSoup

def remove_duplicates_and_extras(html):
    soup = BeautifulSoup(html, 'html.parser')

    # 遍历所有元素并创建唯一键字典
    elements = soup.find_all()
    prev_unique_key = None

    for element in elements:
        tag_name = element.name
    class_name = ' '.join(element.get('class', []))

    unique_key = f'{tag_name}-{class_name}'

    if unique_key == prev_unique_key:
        element.decompose()
    else:
        prev_unique_key = unique_key

    # 格式化处理后的代码并删除空行
    processed_html = soup.prettify().strip()

    return processed_html

# 读取HTML文件
input_file_path = '/Users/zhouzhi/Desktop/next/python-spider/beautifulSoup/input.html'
with open(input_file_path, 'r') as f:
    html = f.read()

# 处理HTML代码
processed_html = remove_duplicates_and_extras(html)

# 将处理后的HTML代码写入文件
output_file_path = '/Users/zhouzhi/Desktop/next/python-spider/beautifulSoup/output.html'
with open(output_file_path, 'w') as f:
    f.write(processed_html)

print(f'处理后的HTML代码已写入文件：{output_file_path}')