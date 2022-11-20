import os.path
import pytest
import time
from base.selenium_base import SeleniumBase
from pom.page_navigation import PageNavigation


@pytest.mark.usefixtures('setup')
class TestHomepage():

    def test_homepage(self):

        comands = PageNavigation(self.driver)
        base = SeleniumBase(self.driver)

        try:
            comands.login()
        except:
            print('Не удалось авторизироваться')
            return


        try:
            comands.to_files()
        except:
            print('Не удалось зайти в файлы')
            return

        try:
            find_folder = 'Documentsdghszfgj'
            comands.find_folder(find_folder)
            base.driver.refresh()
        except:
            print('Ошибка при поиске/создании папки')
            return







        ##########################################
        # find_folder = 'Documentsdghszfgj'
        # folder_name_xpath = '//*[@id="fileList"]/tr/td[2]/a/span[1]' #/span[1]'
        # folders_name =  base.are_present('xpath', folder_name_xpath, 'List of folders')
        # index = base.find_element_from_list(folders_name, find_folder)
        #
        # if index != -1:
        #     folders_name[index].click()
        # else:
        #     print('Are you want to create \"' + find_folder+'\"? y/n')
        #     answer = input()
        #     if answer == 'y' or answer == "Y":
        #         add_button_xpath = '//*[@id="controls"]/div[2]/a'
        #         add_button = base.is_present('xpath',add_button_xpath,'Add Button')
        #         add_button.click()
        #         add_new_folder_xpath = '//*[@id="controls"]/div[2]/div[2]/ul/li[2]/a'
        #         add_new_folder = base.is_present('xpath',add_new_folder_xpath, 'Add new folder')
        #         add_new_folder.click()
        #         new_folder_name_xpath = '//*[@id="view11-input-folder"]'
        #         new_folder_name = base.is_present('xpath', new_folder_name_xpath,'input for new folder')
        #         base.print(new_folder_name,find_folder)
        #         confirm_button_xpath = '//*[@id="controls"]/div[2]/div[2]/ul/li[2]/a/form/input[2]'
        #         confirm_button = base.is_present('xpath', confirm_button_xpath,'confirm new folder')
        #         confirm_button.click()
        #
        #         base.driver.refresh()
        #
        #         folders_name = base.are_present('xpath', folder_name_xpath, 'List of folders')
        #         index = base.find_element_from_list(folders_name, find_folder)
        #         print( str(folders_name[0]) +'/////'+ str(index))
        #         folders_name[index].click()
        #############################
        # base.driver.refresh()

        try:
            file = r'E:/projects/seleniumtry/tst.txt'
            comands.upload_file(file)
        except:
            print('Ошибка поиска/загрузки файла')
            return

        input()
        #
        # file_name = base.are_present('xpath',file_name_xpath, '')
        # print('file name wb: ')
        # print(str(file_name))
        # index = base.find_element_from_list(file_name,os.path.basename(file))
        # print('find '+os.path.basename(file))
        #
        # if index != -1:
        #     file_name[index].click()
        # else:
        #     button_xpath = '//*[@id="controls"]/div[2]/a'
        #     button = base.is_present('xpath', button_xpath,'+file 1')
        #     button.click()
        #     new_file_button_xpath = 'input[type=file]'#'//*[@id="controls"]/div[2]/div[2]/ul/li[1]/label'
        #     new_file_button = base.is_present('css', new_file_button_xpath, '+file 2')
        #     new_file_button.send_keys(file)
