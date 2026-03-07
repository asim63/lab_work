# labapp/selenium_tests.py - Asim Poudel | Roll No: 8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

BASE_URL = "http://127.0.0.1:8000"

def get_driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(
        service=Service("chromedriver.exe"),
        options=options
    )
    driver.implicitly_wait(5)
    return driver

def test_notes_can_be_created():
    driver = get_driver()
    try:
        driver.get(f"{BASE_URL}/notes/create/")
        driver.find_element(By.NAME, "title").send_keys(
            "Selenium Note - Asim Poudel Roll 8")
        driver.find_element(By.NAME, "content").send_keys(
            "This note was created by Selenium test.")
        driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
        print("PASS: test_notes_can_be_created - Asim Poudel Roll 8")
        input("Screenshot now - then press Enter...")
    finally:
        driver.quit()

def test_error_occurs_if_description_is_less_than_10_chars_long():
    driver = get_driver()
    try:
        driver.get(f"{BASE_URL}/notes/create/")
        driver.find_element(By.NAME, "title").send_keys(
            "Short Note Test")
        driver.find_element(By.NAME, "content").send_keys(
            "Short")
        driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
        print("PASS: test_error_short_description - Asim Poudel Roll 8")
        input("Screenshot now - then press Enter...")
    finally:
        driver.quit()

if __name__ == "__main__":
    print("=== Selenium Tests - Asim Poudel | Roll No: 8 ===")
    test_notes_can_be_created()
    test_error_occurs_if_description_is_less_than_10_chars_long()
    print("=== All Selenium tests completed ===")