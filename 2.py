import os
import json

def scan_dishes(dishes_root='./'):
    categories = {}
    for cat in os.listdir(dishes_root):
        cat_path = os.path.join(dishes_root, cat)
        if not os.path.isdir(cat_path):
            continue
        dishes = []
        for item in os.listdir(cat_path):
            item_path = os.path.join(cat_path, item)
            if os.path.isdir(item_path):
                # 文件夹
                dishes.append({
                    "name": item,
                    "path": item,
                    "isFolder": True
                })
            elif item.endswith('.md'):
                # md文件
                dishes.append({
                    "name": item[:-3],  # 去掉.md
                    "path": item,
                    "isFolder": False
                })
        categories[cat] = dishes
    return categories

if __name__ == "__main__":
    data = scan_dishes()
    with open('dishes.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
