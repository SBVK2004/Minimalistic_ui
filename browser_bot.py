from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def run_browser_automation(script):
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        exec(script, {'driver': driver, 'By': By, 'time': time})
    except Exception as e:
        print("Automation failed:", str(e))
