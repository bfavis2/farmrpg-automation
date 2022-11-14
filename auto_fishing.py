import time
import secrets
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

    def quit(self) -> None:
        self.driver.quit()

    def login(self, username: str, password: str) -> None:
        self.driver.get('https://farmrpg.com/index.php#!/login.php')

        username_box = self.driver.find_element(By.NAME, 'username')
        username_box.clear()
        username_box.send_keys(username)

        pw_box = self.driver.find_element(By.NAME, 'password')
        pw_box.clear()
        pw_box.send_keys(password)

        pw_box.send_keys(Keys.RETURN)

        time.sleep(self.sleep_spacer)

    def navigate_to_fishing_spot_from_home(self, fishing_spot_id: int) -> None:
        general_fishing_link = self.driver.find_element(By.XPATH, f'//a[@href="fish.php"]')
        general_fishing_link.click()

        time.sleep(self.sleep_spacer)

        fishing_spot_link = self.driver.find_element(By.XPATH, f'//a[@href="fishing.php?id={fishing_spot_id}"]')
        fishing_spot_link.click()

        time.sleep(self.sleep_spacer)

    def fish(self, final_bait_count:int = 0) -> None:
        fishing_start_time = time.time()
        while self._get_bait_amount_left > 0:
            try:
                fish = self.driver.find_element(By.XPATH, f'//img[contains(@class, "catch")]')
                fish.click()

                self._click_on_moving_blue_dot()

            except (NoSuchElementException, ElementClickInterceptedException):
                continue
                    
            time.sleep(.1)
            

    def _click_on_moving_blue_dot(self) -> None:
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

    def _get_bait_amount_left(self) -> int:
        return int(self.driver.find_element(By.XPATH, '//*[@id="baitarea"]/div[1]/div[1]/strong').text)

if __name__ == '__main__':
    USERNAME = secrets.username
    PASSWORD = secrets.password

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

'''
<div class="card-content-inner" style="padding:5px" id="baitarea"> 
    <div class="row" style="margin-bottom: 0">
        <div class="col-45" style="font-size:13px">
            Worms: <strong>299</strong>
            <a href="changebait.php?from=fishing&amp;id=4" style="font-size:11px">Swap</a>
        </div>
        <div class="col-55" style="font-size:13px">Streak: <strong>0</strong> &nbsp; Best: <strong>160</strong></div>
    </div>
    <div id="last_bait" style="display:none">Worms</div>
</div>
'''

'''
//*[@id="baitarea"]
'''

'''
/html/body/div[3]/div[3]/div[2]/div[2]/div/div[1]/div[3]/div/div/div[1]/div[1]/strong

//*[@id="baitarea"]/div[1]/div[1]/strong
'''