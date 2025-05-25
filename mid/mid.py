from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading

result = []
result2 = []

def ranks_c(days):
    global result
    driver = webdriver.Chrome()
    driver.get(f'https://www.books.com.tw/web/sys_saletopb/books/?attribute={days}')
    wait = WebDriverWait(driver, 20)
    items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.item')))
    
    for item in items:
        try:
            rank_element = item.find_element(By.CSS_SELECTOR, 'strong.no')
            name_element = item.find_element(By.CSS_SELECTOR, 'div.type02_bd-a h4')
            rank = rank_element.text.strip()
            name = name_element.text.strip()
            result.append((rank, name))
        except Exception:
            continue
    
    driver.quit()

def ranks_f(days):
    global result2
    driver2 = webdriver.Chrome()
    driver2.get(f'https://www.books.com.tw/web/sys_saletopb/fbooks/?attribute={days}')
    wait2 = WebDriverWait(driver2, 20)
    items2 = wait2.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.item')))

    for item2 in items2:
        try:
            rank_element2 = item2.find_element(By.CSS_SELECTOR, 'strong.no')
            name_element2 = item2.find_element(By.CSS_SELECTOR, 'div.type02_bd-a h4')
            rank_f = rank_element2.text.strip()
            name_f = name_element2.text.strip()
            result2.append((rank_f, name_f))
        except Exception:
            continue
    
    driver2.quit()


days_input = input("請輸入想查詢 7 日暢銷榜或 30 日暢銷榜（輸入 7 或 30）：")
if days_input not in ["7", "30"]:
    print("請輸入有效的數字（7 或 30）")
else:
    thread1 = threading.Thread(target=ranks_c, args=(days_input,))
    thread2 = threading.Thread(target=ranks_f, args=(days_input,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    
    print(f'\n中文總榜的 {days_input} 日暢銷榜')
    for rank, name in result:
        print(f'TOP {rank}: {name}')
        
    print(f'\n外文總榜的 {days_input} 日暢銷榜')
    for rank_f, name_f in result2:
        print(f'TOP {rank_f}: {name_f}')