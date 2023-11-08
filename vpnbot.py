from selenium import webdriver


browser = webdriver.Firefox()
url = 'http://localhost/voting.php'


browser.get(url)
XPATH_X = "/html/body/div/div/div[1]/div[1]/div[2]/form[1]/input"


next_button = browser.find_element_by_xpath(XPATH_X)
print("Trying to click the button to vote.")
next_button.click()
print("Button clicked.")

exit()

# TRADUZIR ESSE CÓDIGO PARA PYTHON

# :loop

# taskkill /IM VPN.exe
# taskkill /IM geckodriver.exe

# echo "STARTING..."
# cmd.exe /c "start C:\Users\filip\Desktop\VPN.exe"

# timeout 6 

# echo "[!] Starting the Voting process..."
# cmd.exe /c "python C:\Users\filip\Desktop\vote.py"

# timeout 6

# echo "[+] Voting done."
# taskkill /IM geckodriver.exe

# timeout 3

# echo " Killing the VPN"
# taskkill /IM VPN.exe

# goto loop