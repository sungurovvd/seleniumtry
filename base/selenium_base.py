from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def __get_selenium_by(self, find_by: str):
        find_by = find_by.lower()
        locating = {'css': By.CSS_SELECTOR,
                    'xpath': By.XPATH,
                    'class_name': By.CLASS_NAME,
                    'id': By.ID,
                    'link_text': By.LINK_TEXT,
                    'name': By.NAME,
                    'partial_link_text': By.PARTIAL_LINK_TEXT,
                    'tag_name': By.TAG_NAME
            }
        return locating[find_by]

    def is_visible(self, find_by, locator: str, locator_name = None) -> WebElement:
        return self.wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def is_present(self, find_by, locator: str, locator_name = None) -> WebElement:
        return self.wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def is_not_present(self, find_by, locator: str, locator_name = None) -> WebElement:
        return self.wait.until(ec.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def are_visible(self, find_by, locator: str, locator_name = None) -> List[WebElement]:
        return self.wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def are_present(self, find_by, locator: str, locator_name = None) -> List[WebElement]:
        return self.wait.until(ec.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def print(self, element, txt: str):
        element.send_keys(txt)

    def find_element_from_list(self, list, search):

        print('in: ')
        print(str(list))
        links_text_before = [link.text for link in list]
        links_text = [link.replace('\n','') for link in links_text_before]

        print('aftr: ')
        print(links_text)
        try:
            index = links_text.index(search)
            #print('im in')
        except:
            index = -1
        links_text_before.clear()
        links_text.clear()
        return index





