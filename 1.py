import os

def generate_category_links(dishes_dir='./'):
    # 获取dishes目录下所有文件夹名
    categories = [name for name in os.listdir(dishes_dir) if os.path.isdir(os.path.join(dishes_dir, name))]
    # 生成HTML代码
    for cat in sorted(categories):
        print(f'<li><a href="category.html?cat={cat}">{cat.capitalize()}</a></li>')

if __name__ == "__main__":
    generate_category_links()
