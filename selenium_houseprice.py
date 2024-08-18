import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# 設置 Chrome Driver（假設你使用的是 Chrome 瀏覽器）
driver = webdriver.Chrome()
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Data"
ws.append(["Text Content"])
# 開啟目標網站
driver.get("https://price.houseprice.tw")  # 將此網址換成你的目標網站
driver.maximize_window()
# 使用 class 屬性來定位 <span> 元素
span_element = driver.find_element(By.CLASS_NAME, "select_txt")
time.sleep(2)
span_element.click()
time.sleep(2)
span_element = driver.find_element(By.XPATH, "//span[text()='金門縣']")
time.sleep(2)
span_element.click()
time.sleep(2)
span_element = driver.find_element(By.XPATH, "//span[text()='金城鎮']")
time.sleep(2)
span_element.click()
span_element = driver.find_element(By.XPATH, "//span[@data-v-95106727 and contains(@class, 'select_txt') and contains(@class, 'nowrap')]")
time.sleep(2)
span_element.click()
span_element = driver.find_element(By.XPATH, "//span[text()='住宅大樓/華廈']")
time.sleep(2)
span_element.click()
search_button = driver.find_element(By.XPATH, "//a[@class='search_btn']")
time.sleep(2)
search_button.click()
group_elements = driver.find_elements(By.CLASS_NAME, "group")

# 遍歷這些元素並對其進行操作（例如提取文本）
list1 = []
for index, element in enumerate(group_elements):
    # 取出一個元素的文字內容
    text = element.text
    #print(f"Element {index + 1}: {text}")  # 打印每個元素的文字內容
    text = text.split("\n")
    # 將每個取出的元素寫入 Excel
    print(text)
    for text
        ws.append([text])  # 每個元素單獨寫入一行
    except:
        pass
    # 每取出一次資料就保存 Excel 文件
    wb.save("output_step_by_step.xlsx")

driver.quit()