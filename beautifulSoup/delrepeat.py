from bs4 import BeautifulSoup
from bs4.element import Comment

def remove_duplicates_and_extras(html):
    soup = BeautifulSoup(html, 'html.parser')

    # 删除脚本标签
    for script in soup.find_all('script'):
        script.decompose()

    # 删除样式标签
    for style in soup.find_all('style'):
        style.decompose()

    # 删除链接标签（CSS、JavaScript等文件引入）
    for link in soup.find_all('link'):
        link.decompose()

    # 删除注释
    for comment in soup(text=lambda text: isinstance(text, Comment)):
        comment.extract()

    # 删除相同样式的HTML代码块
    elements = soup.find_all()
    prev_element = None
    for element in elements:
        # 检查元素是否为None以及属性是否存在
        if prev_element is not None and prev_element.attrs is not None and element.attrs is not None:
            # 检查元素的class和style属性
            if element.attrs.get('class') == prev_element.attrs.get('class') and element.attrs.get('style') == prev_element.attrs.get('style'):
                element.decompose()
        prev_element = element

    # 查找相同样式的代码块，并删除重复的代码块
    unique_dict = {}
    for element in soup.find_all():
        tag_name = element.name
    class_name = ' '.join(element.get('class', []))
    unique_key = f'{tag_name}-{class_name}'
    if unique_key not in unique_dict:
        unique_dict[unique_key] = element
    else:
        element.decompose()

    # 删除多余的空行
    for element in soup.find_all():
        if element.string is None and not element.contents:
            element.decompose()

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
