from selenium import webdriver
import logging
'''
Scenariusz testowy zakłada sześć kroki 
1. Wejście na strone Netflix'a
2. Zaakceptowanie Cookie
3. Kliknięcia przycisku "Zaloguj się"
4. Wpisania zmyślonego adresu email i hasła
5. Wcisnięcia przycisku "Potrzebujesz pomocy?"
6. Wpisania zmyślonego adresu email
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
    fh = logging.FileHandler('NetflixScenario2ChromeLog.log')
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver.exe')

    logger.info('1. Go to Netflix Site')
    driver.get('https://www.netflix.com/pl/')

    logger.info('2. Accept Cookies')
    temp = driver.find_element_by_class_name('btn-red')
    temp.click()

    logger.info('3. Click Log In button')
    temp = driver.find_element_by_link_text('Zaloguj się')
    temp.click()

    logger.info('4. Enter fake email address and password')
    temp = driver.find_element_by_id('id_userLoginId').send_keys('testmail@wp.pl')
    temp = driver.find_element_by_id('id_password').send_keys('password')

    logger.info('5. Click Need help ?')
    temp = driver.find_element_by_link_text('Potrzebujesz pomocy?')
    temp.click()

    logger.info('6. Enter your fake mail')
    temp = driver.find_element_by_id('forgot_password_input').send_keys('testmail@wp.pl')

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

    logger.info('3. Click Log In button')
    temp = driver.find_element_by_link_text('Zaloguj się')
    temp.click()

    logger.info('4. Enter fake email address and password')
    temp = driver.find_element_by_id('id_userLoginId').send_keys('testmail@wp.pl')
    temp = driver.find_element_by_id('id_password').send_keys('password')

    logger.info('5. Click Need help ?')
    temp = driver.find_element_by_link_text('Potrzebujesz pomocy?')
    temp.click()

    logger.info('6. Enter your fake mail')
    temp = driver.find_element_by_id('forgot_password_input').send_keys('testmail@wp.pl')

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

    logger.info('3. Click Log In button')
    temp = driver.find_element_by_link_text('Zaloguj się')
    temp.click()

    logger.info('4. Enter fake email address and password')
    temp = driver.find_element_by_id('id_userLoginId').send_keys('testmail@wp.pl')
    temp = driver.find_element_by_id('id_password').send_keys('password')

    logger.info('5. Click Need help ?')
    temp = driver.find_element_by_link_text('Potrzebujesz pomocy?')
    temp.click()

    logger.info('6. Enter your fake mail')
    temp = driver.find_element_by_id('forgot_password_input').send_keys('testmail@wp.pl')

    driver.close()
else:
    print("Pick 1,2 or 3")