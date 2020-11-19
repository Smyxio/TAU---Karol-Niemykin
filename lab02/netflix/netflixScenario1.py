from selenium import webdriver
import logging
'''
Scenariusz testowy zakłada trzy kroki 
1. Wejście na strone Netflix'a
2. Zaakceptowanie Cookie
3. Sprawdzenie czym jest Netflix
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
    fh = logging.FileHandler('NetflixScenario1ChromeLog.log')
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver.exe')

    logger.info('1. Go to Netflix Site')
    driver.get('https://www.netflix.com/pl/')
    logger.info('2. Accept Cookies')
    temp = driver.find_element_by_class_name('btn-red')
    temp.click()
    logger.info('3. Check what is Netflix')
    temp = driver.find_element_by_class_name('faq-question')
    temp.click()

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
    fh = logging.FileHandler('NetflixScenario1OperaLog.log')
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    driver = webdriver.Chrome(executable_path='C:\Drivers\operadriver.exe')

    logger.info('1. Go to Netflix Site')
    driver.get('https://www.netflix.com/pl/')
    logger.info('2. Accept Cookies')
    temp = driver.find_element_by_class_name('btn-red')
    temp.click()
    logger.info('3. Check what is Netflix')
    temp = driver.find_element_by_class_name('faq-question')
    temp.click()

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
    fh = logging.FileHandler('NetflixScenario1FirefoxLog.log')
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    driver = webdriver.Chrome(executable_path='C:\Drivers\geckodriver.exe')

    logger.info('1. Go to Netflix Site')
    driver.get('https://www.netflix.com/pl/')
    logger.info('2. Accept Cookies')
    temp = driver.find_element_by_class_name('btn-red')
    temp.click()
    logger.info('3. Check what is Netflix')
    temp = driver.find_element_by_class_name('faq-question')
    temp.click()

    driver.close()


else:
    print("Pick web browser")