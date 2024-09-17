from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
#works for tables
driver = webdriver.Chrome(options=Options())
def main():

    driver.get('https://bwt.cbp.gov/details/09250401/POV')

#assert "Border" in driver.title


    wait = WebDriverWait(driver, 50)
    tbody = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="sectionB"]/div/table/tbody')))

    data = []

    for tr in tbody.find_elements(By.XPATH, '//tr'):
        row = [item.text for item in tr.find_elements(By.XPATH, './/td')]
        data.append(row)
    print(data)

    #Related to Handshake WORKS
    #this gives me 26
    WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "style__card___XOQvr"))
    )
    cards = driver.find_elements(By.CLASS_NAME, "style__card___XOQvr")
    for card in cards:
        title = card.text
        print(title)
   
    
    with open('borderData.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

if __name__ == '__main__':
    main()