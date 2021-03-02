from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from .Xpath import *
import xlsxwriter
from multiprocessing.dummy import Pool

class Scrape:

    post = []
    follower = []
    following = []

    def __init__(self, username, target, thread_count):
        self.username = username
        self.target = target
        self.thread_count = thread_count

    def grab_data(self, username):
        
        print('Scrape {} Followers From {}'.format(username, self.target))
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)
        webDriverWait = WebDriverWait(driver, 10)
        url = 'https://www.instagram.com/{}/'.format(username)
        driver.get(url)
        self.post.append(webDriverWait.until(EC.presence_of_element_located((By.XPATH, post_all))).text)
        self.follower.append(webDriverWait.until(EC.presence_of_element_located((By.XPATH, followers_all))).text)
        self.following.append(webDriverWait.until(EC.presence_of_element_located((By.XPATH, following_all))).text)
        driver.quit()

    def run(self):

        if len(self.username) == 0:
            print('followers not more than 0')
        else:
            with Pool(self.thread_count) as worker:
                worker.map(self.grab_data, self.username)
                worker.close()
                worker.join()

            self.export(self.username, self.post, self.follower, self.following)

    def export(self, username, post, follower, following):
        current_path = os.getcwd()
        output_path = '{}/result/'.format(current_path)

        file_name = '{}.xlsx'.format(self.target)
        workbook = xlsxwriter.Workbook(file_name)
        sheet = workbook.add_worksheet()

        sheet.write('A1', 'Username')
        sheet.write('B1', 'Post')
        sheet.write('C1', 'Follower')
        sheet.write('D1', 'Following')

        for i in range(len(self.username)):
            sheet.write(i+1, 0, self.username[i])
            sheet.write(i+1, 1, post[i])
            sheet.write(i+1, 2, follower[i])
            sheet.write(i+1, 3, following[i])

        workbook.close()

        print('File tersimpan di {} dengan nama {}'.format(output_path, file_name))