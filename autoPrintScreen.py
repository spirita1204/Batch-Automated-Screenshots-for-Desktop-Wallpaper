import pyautogui #截圖套件
import time #等待時間套件
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#leetcode網址
leetcode_url = "https://leetcode.com/u/spirita1204/" 
# 設置 chromedriver 的路徑
chromedriver_path = r'D:\project\autoScreeShot\chromedriver-win64\chromedriver.exe'

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
time.sleep(6)

# 自訂截圖範圍 (left, top, width, height)
left = 100
top = 200
height = 1250
# 獲取屏幕尺寸
screen_width, screen_height  = pyautogui.size()

# 截取當前螢幕
my_screenshot = pyautogui.screenshot(region=(left, top, screen_width - 150, height))

# 保存截圖到指定路徑
screenshot_path = r"C:\Users\User\Desktop\screenshot_1.png"
my_screenshot.save(screenshot_path)

# 顯示一條消息
print(f"截圖已保存到 {screenshot_path}")

# 關閉瀏覽器
driver.quit()

