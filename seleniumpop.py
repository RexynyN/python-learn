from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_binary

def script(path):
    script = ""
    with open(path, "r", encoding="utf-8") as f:
        script = f.read()
    
    return script


def main ():
    driver = webdriver.Chrome()
    driver.get("https://mangadex.org/chapter/d4af4c7a-2102-4af5-84a6-6627c2695882/1")
    # for i in range(10):
    #     driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    element_present = EC.presence_of_element_located((By.CLASS_NAME, 'md--page'))
    WebDriverWait(driver, timeout=30).until(element_present)

    for i in range(0, 5):
        driver.find_elements(By.TAG_NAME, "body")[0].send_keys(Keys.ARROW_RIGHT) 
        driver.find_elements(By.TAG_NAME, "body")[0].send_keys(Keys.ARROW_RIGHT) 

    driver.implicitly_wait(15)
    returned = driver.execute_script(script("seleniumpop.js"))
    with open("mangadex.txt", "w", encoding="utf-8") as f:
        f.write(str(returned))

    # print(len(returned))

    # to scroll till page bottom
    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")


    # #open tab
    # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    # #or 
    # driver.execute_script('''window.open("http://bings.com","_blank");''')


    # # Load a page 
    # driver.get('http://stackoverflow.com/')

    # # close the tab
    # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w') 

    # # switch tabs
    # window_name = self.selenium.window_handles[-1]
    # self.selenium.switch_to.window(window_name=window_name)
    input()


def how_the_fuck ():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager
    import time

    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get("https://www.climatempo.com.br/")

    time.sleep(5)

    tempo = driver.find_element(By.ID, "current-weather-temperature")

    print(f"Hoje o tempo é de {tempo.text} graus.");


if __name__ == "__main__":
    main()  
    # how_the_fuck()