import requests
from bs4 import BeautifulSoup
import os

url1 = "https://en.wikipedia.org/wiki/YouTube_Creator_Awards"
url2 = "https://www.fastcompany.com/90776050/who-exactly-benefits-from-renewable-energy-subsidies-the-answer-will-surprise-you"  # Replace with the desired URL



import json

# Read the JSON file
with open('intrinsic_halls.json') as file:
    data = json.load(file)

# Extract the "link_target" values
link_targets = [citation['link_target'] for item in data for citation in item['citations']]

# Print the list of "link_target" values
# print(link_targets)

import requests
from bs4 import BeautifulSoup
import signal

def timeout_handler(signum, frame):
    raise TimeoutError("Function execution timed out")

MAX_FILENAME_LENGTH = 50  # Maximum allowed filename length
def truncate_filename(filename):
    if len(filename) <= MAX_FILENAME_LENGTH:
        return filename
    else:
        return filename[:MAX_FILENAME_LENGTH - 4] + ".txt"
    
num = 0
succ = 0
fail = 0
crawled_url = set()
def static_crawling_and_save(url, timeout=25):
    if url in crawled_url:
        return None
    # Register the timeout handler
    global num, succ, fail
    num += 1
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)

    try:
        response = requests.get(url)
        content = response.content

        soup = BeautifulSoup(content, "html.parser")

        # paragraphs = soup.find_all("p")
        # for p in paragraphs:
        #     print(p.get_text())

        # Extract all text from the webpage
        all_text = soup.get_text()

        # print(all_text)

        # Create a file name based on the URL
        filename = url.split("//")[1].replace("/", "_") + ".txt"

        filename = truncate_filename("crawled_websites/"+filename)
        print(url)
        success = len(all_text) > 500
        # Save the text content into a file
        all_text = url + '\n\n\n' + f"Success: {success}" + '\n\n\n' + all_text
        with open(filename, "w", encoding="utf-8") as file:
            file.write(all_text)
        
        if success:
            succ += 1
        else:
            fail += 1
        print(f"Num:{num}  Succ:{succ}  Fail:{fail}")
        print(len(all_text))
        print()
        print()
    except TimeoutError:
        print("Crawling and saving failed due to timeout.")
        fail += 1
    except requests.RequestException as e:
        print("Crawling and saving failed:", str(e))
        fail += 1
    finally:
        # Reset the alarm
        crawled_url.add(url)
        signal.alarm(0)

# print(len(link_targets))
for i, link in enumerate(link_targets):
    filename = link .split("//")[1].replace("/", "_") + ".txt"

    filename = truncate_filename("crawled_websites/"+filename)
    if os.path.exists(filename):
        # print(f"The file '{filename}' exists.")
        pass
    else:
        print(f"The file '{link}' does not exist.")
    # if link != url1 and link != url2:
    #     static_crawling_and_save(link)



# from requests_html import HTMLSession

# session = HTMLSession()

# r = session.get(url)

# r.html.render()  # this call executes the js in the page

# 




# import time 
 
# import pandas as pd 
# from selenium import webdriver 
# from selenium.webdriver import Chrome 
# from selenium.webdriver.chrome.service import Service 
# from selenium.webdriver.common.by import By 
# from webdriver_manager.chrome import ChromeDriverManager
# # start by defining the options 
# options = webdriver.ChromeOptions() 
# options.headless = True # it's more scalable to work in headless mode 
# # normally, selenium waits for all resources to download 
# # we don't need it as the page also populated with the running javascript code. 
# options.page_load_strategy = 'none' 
# # this returns the path web driver downloaded 
# chrome_path = ChromeDriverManager().install() 
# chrome_service = Service(chrome_path) 
# # pass the defined options and service objects to initialize the web driver 
# driver = Chrome(options=options, service=chrome_service) 
# driver.implicitly_wait(5)

 
# driver.get(url) 



# import time
# from selenium import webdriver
# import json

# chrome_options = webdriver.ChromeOptions()
# settings = {
#        "recentDestinations": [{
#             "id": "Save as PDF",
#             "origin": "local",
#             "account": "",
#         }],
#         "selectedDestinationId": "Save as PDF",
#         "version": 2
#     }
# prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings)}
# chrome_options.add_experimental_option('prefs', prefs)
# chrome_options.add_argument("--enable-javascript")
# chrome_options.add_argument('--kiosk-printing')
# CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
# driver = webdriver.Chrome(options=chrome_options)
# time.sleep(3.7)
# driver.get(url)
# import time 
# time.sleep(3.2)
# driver.execute_script('window.print();')
# driver.quit()
# from IPython import embed; embed()
