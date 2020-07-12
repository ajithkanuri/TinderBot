from selenium import webdriver
from time import sleep

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def login(self):
        self.driver.get('https://tinder.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        sleep(10)       
        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_btn.click()
        #storing so with to popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        # email_in.send_keys('siddhu18.vaghela@gmail.com')
        email_in.send_keys('sritha_koneru@yahoo.com')
        email_pass = self.driver.find_element_by_xpath('//*[@id="pass"]')
        # email_pass.send_keys('Vijay2749')
        email_pass.send_keys('ClarkKent2!28')
        submit = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        submit.click()
        self.driver.switch_to_window(base_window)
        poplocation = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        poplocation.click()
        popnoti =self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popnoti.click()
        cookiepopup = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        cookiepopup.click()
    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')        
        like_btn.click()
    def dislike(self):
        dislike = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike.click()
    def close_popup(self):
        pop = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        pop.click()
    def close_match(self):
        popmatch = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        popmatch.click()
    def auto_swipe(self):
        while True:
            sleep(2)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    