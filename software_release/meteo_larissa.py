from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

CHROMEDRIVER_PATH = "C:/drivers/chromedriver.exe"

options = Options()
# Αν θες να βλέπεις τον Chrome, μην το βάλεις σε headless
# options.add_argument("--headless")

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://penteli.meteo.gr/stations/larissa/")
time.sleep(15)  # περιμένουμε να φορτώσει

# Εντοπίζουμε τα στοιχεία με class='right'
divs = driver.find_elements(By.TAG_NAME, "div")
count = 0
output_lines = []

for d in divs:
    class_name = d.get_attribute("class")
    if "right" in class_name:
        count += 1
        line = f"[{count}] ➜ {d.text.strip()}"
        print(line)
        output_lines.append(line)

final_line = f"🔍 Βρέθηκαν {count} divs που περιέχουν class='right'"
print(final_line)
output_lines.append(final_line)

driver.quit()

# Γράφουμε το αποτέλεσμα στο αρχείο
with open("apoteleismata.txt", "w", encoding="utf-8") as file:
    for line in output_lines:
        file.write(line + "\n")

