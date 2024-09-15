from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np

service = Service(executable_path='./msedgedriver.exe')
driver = webdriver.Edge(service=service)

grid = [[[] for _ in range(9)] for _ in range(9)]

def Scan():
    for row in range(0, 9):
        for col in range(0, 9):
            xpath = f"//div[@class='cell'][@data-row='{row}'][@data-column='{col}']"
            try:
                cell_element = WebDriverWait(driver, 0).until(
                    EC.visibility_of_element_located((By.XPATH, xpath))
                )
                
                data_value = cell_element.get_attribute('data-value')
                print({data_value})
                
                grid[row][col] = data_value
                
            except Exception as e:
                grid[row][col] = 0

    print(np.array(grid))

driver.get('https://www.sudokuonline.io/impossible')
Scan()

