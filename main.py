from selenium import webdriver
import json
import time
from selenium.webdriver.common.by import By
import threading

config = json.load(open('./config.json', 'r'))
elements = config['elements-classes'][0]

# options = webdriver.FirefoxOptions()
# options.headless = True

def join_bot(username, t_no):
    print(f"Now starting Thread No. {t_no}")

    driver = webdriver.Firefox(executable_path="./geckodriver.exe")

    driver.get(config['join_url'])

    print("Waiting two seconds for page to load.")

    time.sleep(2)

    code_input_box = driver.find_element_by_class_name(elements['input-box'])
    code_input_box.send_keys(config['pin'])

    time.sleep(0.1)

    join_btn = driver.find_element_by_class_name(elements['join-btn'])
    join_btn.click()

    print("Waiting for joining session to Load.")

    time.sleep(3)

    username_field = driver.find_element_by_class_name(elements['username-input'])

    username_field.send_keys( "%s" % (username) )

    start_btn = driver.find_element_by_class_name(elements['start-btn'])

    start_btn.click()

    def find_existing_username_override():
        time.sleep(3)
        try:
            override_username_element = driver.find_element(By.XPATH, 
                                            f"//*[text()='Resume game as {username}']")
            print("[ERROR MESSAGE] Username: %s already exists! Attemping different username." % username)
            driver.close()
        except:
            print("[LOG MESSAGE] Username: %s is not taken." % username)

    find_existing_username_override()

    time.sleep(config['maximum-minutes'] * 60) # Convert into minutes.

    print('[SUCCESS MESSAGE] Added bot to game.')

    time.sleep()

    driver.close()

def join_bots(amount):
    x = 1
    threads = []

    for i in range(1, amount+1):
        username = config['username-prefix'] + str(i)
        t = threading.Thread(
            target = join_bot,
            kwargs={
                "username": username,
                "t_no": x
            }
        )     
        t.daemon = True
        threads.append(t)
        x += 1
    
    for i in range(len(threads)):
        threads[i].start()
    
    for i in range(len(threads)):
        threads[i].join()

join_bots(config['amount_of_bots'])

