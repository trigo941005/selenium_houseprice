from selenium import webdriver
from selenium.webdriver.common.by import By

# 設置 Chrome Driver（假設你使用的是 Chrome 瀏覽器）
driver = webdriver.Chrome()

# 開啟目標網站
driver.get("https://price.houseprice.tw")  # 將此網址換成你的目標網站

# 使用 class 屬性來定位 <span> 元素
span_element = driver.find_element(By.CLASS_NAME, "select_txt")

# 提取 span 元素中的文字內容
span_text = span_element.text
print(span_text)  # 預期輸出: 台北市全區

# 確保操作結束後關閉瀏覽器
driver.quit()
