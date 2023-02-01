import shutil
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep 
from binascii import a2b_base64
import os
import json 
import requests

# ===================================== CONFIGS ==========================================

URLS = [
    "https://mangadex.org/chapter/f59b9628-f1fe-427b-b935-22c91076f699/1", 
]

SCRAPPING_URL = "https://mangadex.org/chapter/f59b9628-f1fe-427b-b935-22c91076f699/1"

SCRIPT_PATH = "clover.js"

DEFAULT_TIMER = 30

# ========================================================================================

def data_url_to_image(data, filename):
    if(data.find(",") != -1):
        data = data.split(",")[-1]
        if(not os.path.isdir(os.getcwd() + "\\output")):
            os.mkdir(os.getcwd() + "\\output")

        binary_data = a2b_base64(data)
        with open(os.getcwd() + "\\output\\" + filename, 'wb') as f:
            f.write(binary_data)
    else:
        print("Opa, deu algo de errado.")

def script(path):
    script = ""
    with open(path, "r", encoding="utf-8") as f:
        script = f.read()
    
    return script

def main():
    global_script = script(SCRIPT_PATH)

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get("https://google.com") # Bootstrap the browser

    driver.get(SCRAPPING_URL)
    # myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'mx-auto md--page flex ')))

    sleep(DEFAULT_TIMER)

    driver.execute_script(global_script)
    num_pages = driver.execute_script("return window.getNumberPages();")

    for _ in range(num_pages - 1):
        screen = driver.find_element(By.TAG_NAME, "body")
        screen.send_keys(Keys.ARROW_RIGHT)
        sleep(0.5)

    imgs = [None]
    while None in imgs:
        sleep(10)
        imgs = driver.execute_script("return window.getChapterImgs();")
        print(imgs)

    for index, img in enumerate(imgs):
        driver.get(img)
        dataurl = driver.execute_script("return window.scrapImage();")
        data_url_to_image(dataurl, f"{index}.jpg")

    driver.quit()


def assert_path(path):
    if not os.path.isdir(path):
        os.mkdir(path)


def what_in_the_actual_fuck(path):
    with open('imgs.json') as f:
        data = json.load(f)

    assert_path(path)

    for image_url in data:
        print(image_url)
        r = requests.get(image_url, stream = True)
        r.raw.decode_content = True

        name = image_url.split("/")[-1]

        with open(f"{path}\\{name}",'wb') as f:
            shutil.copyfileobj(r.raw, f)

if __name__ == "__main__":
    # main()
    what_in_the_actual_fuck("kill_me_when_seen")