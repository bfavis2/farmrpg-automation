import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FarmRpgFisher():

    def __init__(self, sleep_spacer=.5):
        self.driver = webdriver.Chrome()
        self.sleep_spacer = sleep_spacer

        self.CATCH_FISH_LENGTH = 2.2
        self.FISHING_SPOT_COORDS = (11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34)

    def quit(self):
        self.driver.quit()

    def login(self, username: str, password: str):
        self.driver.get('https://farmrpg.com/index.php#!/login.php')

        username_box = self.driver.find_element(By.NAME, 'username')
        username_box.clear()
        username_box.send_keys(username)

        pw_box = self.driver.find_element(By.NAME, 'password')
        pw_box.clear()
        pw_box.send_keys(password)

        pw_box.send_keys(Keys.RETURN)

        time.sleep(self.sleep_spacer)

    def navigate_to_fishing_spot_from_home(self, fishing_spot_id: int):
        general_fishing_link = self.driver.find_element(By.XPATH, f'//a[@href="fish.php"]')
        general_fishing_link.click()

        time.sleep(self.sleep_spacer)

        fishing_spot_link = self.driver.find_element(By.XPATH, f'//a[@href="fishing.php?id={fishing_spot_id}"]')
        fishing_spot_link.click()

    def fish(self, final_bait_count:int = 0):
        fishing_start_time = time.time()
        while True:
            for coord in self.FISHING_SPOT_COORDS:
                try:
                    print(f'Searching f{coord}')
                    fish = self.driver.find_element(By.XPATH, f'//img[@class="fish f{coord} catch"]')
                    print(f'FOUND FISH at f{coord}')
                    fish.click()

                    self.click_on_moving_blue_dot()

                except (NoSuchElementException, ElementClickInterceptedException):
                    continue
                    
            time.sleep(self.sleep_spacer)
            

    def click_on_moving_blue_dot(self):
        # blue dot is 50x50 div and it lives on the very left
        # surrounding box is 300x50
        catch_start_time = time.time()
        blue_dot = self.driver.find_element(By.XPATH, f'//div[@class="fc"]')
        while time.time() - catch_start_time < self.CATCH_FISH_LENGTH:
            
            try:
                # blue_dot = driver.find_element(By.XPATH, f'//div[@class="fishcaught finalcatch2b"]')
                blue_dot.click()
            except (NoSuchElementException, ElementNotInteractableException) as e:
                pass

            time.sleep(.1)

if __name__ == '__main__':
    USERNAME = 'GoCheeto'
    PASSWORD = 'letbin64'

    fisher = FarmRpgFisher()
    fisher.login(USERNAME, PASSWORD)
    fisher.navigate_to_fishing_spot_from_home(4)
    fisher.fish()
    
'''
Changes to when a fish is ready to catch:
<img src="/img/items/fish.png" class="fish f21 catch" style="display: inline; opacity: 0.383787;">


<div id="fishinwater" style="position:relative;">
    <div class="row no-gutter">
        <div class="col-25 fishcell"><img src="/img/items/fish.png" class="fish f11" style="display: none;"></div>
        <div class="col-25 fishcell"><img src="/img/items/fish.png" class="fish f12" style="display: none;"></div>
        <div class="col-25 fishcell"><img src="/img/items/fish.png" class="fish f13" style="display: none;"></div>
        <div class="col-25 fishcell"><img src="/img/items/fish.png" class="fish f14 "></div>
    </div>
    <div class="row no-gutter">
        <div class="col-25 fishcell"><img src="/img/items/fish.png" class="fish f21 "></div>
        <div class="col-25 fishcell"><img src="/img/items/fish.png" class="fish f22" style="display: none;"></div>
        <div class="col-25 fishcell"><img src="/img/items/fish.png" class="fish f23" style="display: none;"></div>
        <div class="col-25 fishcell"><img src="/img/items/fish.png" class="fish f24" style="display: none;"></div>
    </div>
    <div class="row no-gutter">
        <div class="col-25 fishcell"><img src="/img/items/fish.png" class="fish f31" style="display: none;"></div>
        <div class="col-25 fishcell"><img src="/img/items/fish.png" class="fish f32" style="display: none;"></div>
        <div class="col-25 fishcell"><img src="/img/items/fish.png" class="fish f33" style="display: none;"></div>
        <div class="col-25 fishcell"><img src="/img/items/fish.png" class="fish f34" style="display: none;"></div>
    </div>
</div>
'''

'''
<div class="picker-modal picker-catch modal-in" style="display: block;">
    <div class="toolbar">
        <div class="toolbar-inner">
            <div class="left">Tap to catch the fish!</div>
            <div class="right">Hurry!</div>
        </div>
    </div>
    <div class="picker-modal-inner">
        <div class="content-block fishing-block" style="padding:0; margin:0; overflow-y:scroll; height:280px;">
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <div class="fc" style="max-width: 300px; margin: 0px auto; background-color: rgb(0, 0, 0); border-radius: 40px; --darkreader-inline-bgcolor:#000000;" data-darkreader-inline-bgcolor="">
                <div class="fishcaught finalcatch2b" data-speed="2" data-id="4"></div>
            </div>
        </div>
    </div>
</div>
'''