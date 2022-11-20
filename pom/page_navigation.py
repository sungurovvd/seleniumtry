import os
import time

from base.selenium_base import SeleniumBase
from selenium.common.exceptions import TimeoutException

class PageNavigation(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        #base = SeleniumBase(self.driver)

    def login(self):

        login_xpath = '//*[@id="user"]'
        password_xpath = '//*[@id="password"]'
        button_xpath = '//*[@id="submit-form"]'
        login_txt = 'Victor'
        wrong = '//*[@id="body-login"]/div[1]/div/main/div/div/form/fieldset/p[3]'

        do_it_again = 1

        while do_it_again == 1:
            do_it_again = 1
            print('Пароль: ')
            password_txt = input()

            login = self.is_present('xpath', login_xpath, 'Login')
            password = self.is_present('xpath', password_xpath, 'Password')
            button = self.is_present('xpath', button_xpath, 'button')

            self.print(login, login_txt)
            self.print(password, password_txt)
            button.click()
            self.driver.refresh()

            try:
                self.is_visible('xpath', wrong, '')
                print('intry')
            except:
                do_it_again = 0
                print('inexeption')

    def to_files(self):
        files_button_xpath = '//*[@id="appmenu"]/li[2]'
        files_button = self.is_present('xpath', files_button_xpath, 'files')
        files_button.click()

    def create_folder(self, find_folder, folder_name_xpath):
        add_button_xpath = '//*[@id="controls"]/div[2]/a'
        add_button = self.is_present('xpath',add_button_xpath,'Add Button')
        add_button.click()
        add_new_folder_xpath = '//*[@id="controls"]/div[2]/div[2]/ul/li[2]/a'
        add_new_folder = self.is_present('xpath',add_new_folder_xpath, 'Add new folder')
        add_new_folder.click()
        new_folder_name_xpath = '//*[@id="view11-input-folder"]'
        new_folder_name = self.is_present('xpath', new_folder_name_xpath,'input for new folder')
        self.print(new_folder_name,find_folder)
        confirm_button_xpath = '//*[@id="controls"]/div[2]/div[2]/ul/li[2]/a/form/input[2]'
        confirm_button = self.is_present('xpath', confirm_button_xpath,'confirm new folder')
        confirm_button.click()
        self.driver.refresh()
        folders_name = self.are_present('xpath', folder_name_xpath, 'List of folders')
        index = self.find_element_from_list(folders_name, find_folder)
        print( str(folders_name[0]) +'/////'+ str(index))
        folders_name[index].click()
        return index

    def find_folder(self, find_folder):

        folder_name_xpath = '//*[@id="fileList"]/tr/td[2]/a/span[1]'
        folders_name = self.are_present('xpath', folder_name_xpath, 'List of folders')
        index = self.find_element_from_list(folders_name, find_folder)

        if index != -1:
            folders_name[index].click()
        else:
            print('Are you want to create \"' + find_folder + '\"? y/n')
            answer = input()
            if answer == 'y' or answer == "Y":
                index = self.create_folder(find_folder, folder_name_xpath)
        return index

    def upload_file(self, file):
        file_name_xpath = '//*[@id="fileList"]/tr/td[2]/a/span[1]'
        file_name = self.are_present('xpath', file_name_xpath, '')
        print('file name wb: ')
        print(str(file_name))
        index = self.find_element_from_list(file_name, os.path.basename(file))
        print('find '+os.path.basename(file))

        if index != -1:
            print('Файл уже есть в списке')
            file_name[index].click()
        else:
            button_xpath = '//*[@id="controls"]/div[2]/a'
            button = self.is_present('xpath', button_xpath,'+file 1')
            button.click()
            new_file_button_xpath = 'input[type=file]'
            new_file_button = self.is_present('css', new_file_button_xpath, '+file 2')
            new_file_button.send_keys(file)








