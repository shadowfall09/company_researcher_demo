import os
from playwright.sync_api import sync_playwright

def ensure_dir(base_dir: str):
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        
    if not os.path.exists(base_dir+"/asset"):
        os.makedirs(base_dir+"/asset")
    if not os.path.exists(base_dir+"/asset/traffic"):
        os.makedirs(base_dir+"/asset/traffic")
    if not os.path.exists(base_dir+"/asset/competitor"):
        os.makedirs(base_dir+"/asset/competitor")
        
        
def screenshot(base_dir: str, company_url: str):
    print("screenshoting...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(company_url)
        page.screenshot(path=base_dir+"/asset/screenshot.png")
        browser.close()
        

def remove_prefix(text: str):
    if text.startswith("```markdown"):
        text = text[11:-3]
    if text.startswith("```python"):
        text = text[9:-3]
    return text

def empty_folder(folder_path: str):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                os.rmdir(dir_path)
                

    