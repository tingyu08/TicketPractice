import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    """ 初始化 Selenium WebDriver """
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # 最大化視窗
    prefs = {"profile.managed_default_content_settings.images": 2}  # 不載入圖片
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

try:
    driver = setup_driver()
    driver.get("https://ticket-training.onrender.com/")
    wait = WebDriverWait(driver, 15)

    # 開始倒數
    coutdown_input = driver.find_element(By.ID, "countdownInput")
    coutdown_input.clear()  # 清除舊值
    coutdown_input.send_keys("1")
    startbutton = driver.find_element(By.ID, "startButton")
    startbutton.send_keys(Keys.RETURN)
    time.sleep(1)

    purchaseButton = driver.find_element(By.ID, "purchaseButton")
    purchaseButton.send_keys(Keys.RETURN)
    purchasebutton = driver.find_element(By.CLASS_NAME, "purchase-button")
    purchasebutton.send_keys(Keys.RETURN)
    
    # 選區域
    place = driver.find_element(By.XPATH, "//body/div[5]/div[3]/div[4]/div[1]/div")
    place.click()

    # 選張數
    select = driver.find_element(By.CLASS_NAME, "quantity-select")
    select.send_keys(Keys.DOWN)
    select.send_keys(Keys.ENTER)

    # 打勾
    checkbox = driver.find_element(By.ID, "terms-checkbox")
    checkbox.send_keys(Keys.SPACE)

    # 填驗證碼
    write = driver.find_element(By.ID, "captcha-input")
    img = driver.find_element(By.ID, "captcha-image")
    write.send_keys(img.get_attribute("data-answer"))
    write.send_keys(Keys.ENTER)

except Exception as e:
    print("❌ 發生錯誤:", e)

finally:
    input("按 Enter 鍵關閉瀏覽器...")
    driver.quit()
    