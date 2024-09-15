from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import pyautogui as pg
import numpy as np
import time 

service = Service(executable_path='./msedgedriver.exe')
driver = webdriver.Edge(service=service)

grid = [[[] for _ in range(9)] for _ in range(9)]

def Scan():
    block = driver.find_element(By.XPATH, f"//div[@data-row='0'][@data-column='0']")
    block.click()
    
    for irow in range(0, 9):
        for icol in range(0, 9):
            xpath = f"//div[@data-row='{irow}'][@data-column='{icol}']"
            cell_element = WebDriverWait(driver, 0).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
                
            data_value = cell_element.get_attribute('data-value')
            # print({data_value})
            if data_value == '':
                data_value = 0    
            grid[irow][icol] = int(data_value)

    print(np.array(grid))
    

# while True:
#     row = list(input('Row: '))
#     ints = []
    
#     for n in row:
#         ints.append(int(n))
#     grid.append(ints)
    
#     if len(grid) == 9:
#         break
#     print('Row: ' + str(len(grid)) + ' complete')

# time.sleep(3)


def possible(row, column, number):
    global grid
    #check row
    for i in range(0,9):
        if grid[row][i] == number:
            return False

    #check collum
    for i in range(0,9):
        if grid[i][column] == number:
            return False
    
    #check square
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == number:
                return False

    return True

def Print(matrix):
    final = []
    str_fin = []
    for i in range(0,9):
        final.append(matrix[i])
        
    for lists in final:
        for num in lists:
            str_fin.append(str(num))
    
    counter = []
    
    row = 0
    for num in str_fin:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)
        if len(counter)%9 == 0:
            row += 1
            if row < 9:
                block = driver.find_element(By.XPATH, f"//div[@data-row='{row}'][@data-column='0']")
                block.click()

def solve():
    global grid
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:
                for number in range(1,10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0

                return
    print(np.matrix(grid))
    Print(grid)
    input('More possible solutions')
    
driver.get('https://www.sudokuonline.io/impossible')
Scan()
solve()