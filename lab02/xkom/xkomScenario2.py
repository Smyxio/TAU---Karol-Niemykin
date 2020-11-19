from selenium import webdriver
import logging
'''
Scenariusz testowy zakłada trzy kroki 
1. Wejście na strone xkom
2. Wybrać "Kariera"
3. Sprawdzić oferty dla Programistów
'''
print("Press 1 to Run test in Google Chrome")
print("Press 2 to Run test in Opera")
print("Press 3 to Run test in Firefox")
web = input("Pick your web browser: ")

# Tests for Chrome
if web == "1":

    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    fh = logging.FileHandler('xkomScenario2ChromeLog.log')
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver.exe')
    driver.maximize_window()

    logger.info('1. Go to xkom Site')
    driver.get('https://www.x-kom.pl')

    logger.info('2. Go to Carrera')
    temp = driver.find_element_by_link_text('Kariera')
    temp.click()

    logger.info('3. Put keyword in search window')
    temp = driver.find_element_by_id('xkom_search_opening_text').send_keys('Programista')

    driver.close()

# Tests for Opera
elif web == "2":

    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    fh = logging.FileHandler('xkomScenario2OperaLog.log')
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    driver = webdriver.Chrome(executable_path='C:\Drivers\operadriver.exe')
    driver.maximize_window()

    logger.info('1. Go to xkom Site')
    driver.get('https://www.x-kom.pl')

    logger.info('2. Go to Carrera')
    temp = driver.find_element_by_link_text('Kariera')
    temp.click()

    logger.info('3. Put keyword in search window')
    temp = driver.find_element_by_id('xkom_search_opening_text').send_keys('Programista')

    driver.close()

# Tests for Firefox
elif web == "3":

    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    fh = logging.FileHandler('xkomScenario2FirefoxLog.log')
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    driver = webdriver.Chrome(executable_path='C:\Drivers\geckodriver.exe')
    driver.maximize_window()

    logger.info('1. Go to xkom Site')
    driver.get('https://www.x-kom.pl')

    logger.info('2. Go to Carrera')
    temp = driver.find_element_by_link_text('Kariera')
    temp.click()

    logger.info('3. Put keyword in search window')
    temp = driver.find_element_by_id('xkom_search_opening_text').send_keys('Programista')

    driver.close()
else:
    print("Pick web browser")