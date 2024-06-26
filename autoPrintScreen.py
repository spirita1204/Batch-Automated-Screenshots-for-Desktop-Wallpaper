import pyautogui #截圖套件
import time #等待時間套件
import ctypes #系統控制套件
import os #系統控制套件
import winreg as reg #系統控制套件
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# 保存截圖到指定路徑
screenshot_path = r"C:\Users\User\Desktop\screenshot_1.png"
# leetcode網址
leetcode_url = "https://leetcode.com/u/spirita1204/" 
# 設置 chromedriver 的路徑
chromedriver_path = r'D:\project\autoScreeShot\chromedriver-win64\chromedriver.exe'
 
# 設置壁紙函數
def change_wallpaper(image_path):
    try:
        image_path = os.path.abspath(image_path)
        # 更改桌布样式到置中
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, r'Control Panel\Desktop', 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(key, "WallpaperStyle", 0, reg.REG_SZ, "1")  # 1 表示居中
        reg.SetValueEx(key, "TileWallpaper", 0, reg.REG_SZ, "0")  # 0 表示不平铺
        reg.CloseKey(key)
        # 20: Change the wallpaper
        result = ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
        if not result:
            raise ctypes.WinError()
        print("Wallpaper changed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# 截圖函數
def screenshot():
    # 自訂截圖範圍 (left, top, width, height)
    left = 100
    top = 200
    height = 1275
    # 獲取屏幕尺寸
    screen_width, screen_height = pyautogui.size()
 
    # 截取當前螢幕
    my_screenshot = pyautogui.screenshot(region=(left, top, screen_width - 200, height))
 
    my_screenshot.save(screenshot_path)
    
def chrome_launch():
   
    service = Service(chromedriver_path)
 
    # 設置 Chrome 選項
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # 啟動時最大化窗口
    chrome_options.add_argument("--kiosk")  # 全屏模式
 
    # 初始化 WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
 
    # 打開瀏覽器並導航到 LeetCode 網頁
    driver.get(leetcode_url)
 
    # 等待頁面加載完成
    time.sleep(5)

    # 截圖並儲存
    screenshot()

    # 關閉瀏覽器
    driver.quit()

def main():
    chrome_launch()
    # 設置壁紙
    change_wallpaper(screenshot_path)
 
if __name__ == "__main__":
    main()