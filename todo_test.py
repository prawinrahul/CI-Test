from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://127.0.0.1:5500/todo.html")
driver.maximize_window()

def add_task(task):
    try:
        task_input = driver.find_element(By.XPATH,"//input[@id='taskInput']")
        task_input.send_keys(task)

        add_button = driver.find_element(By.XPATH,"//button[@onclick='addTask()']")
        add_button.click()
        time.sleep(10)


    except Exception as e:
        print("An error occurred while adding a task:", e)

def test_add_task():
    add_task("Task 1")
    add_task("Task 2")
    add_task("Task 3")

try:
    test_add_task()
    print("Test for adding tasks passed.")
except AssertionError:
    print("Test for adding tasks failed.")

 
          
