import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
# driver.get('https://farmrpg.com/')
driver.get('https://farmrpg.com/index.php#!/login.php')
# driver.get('https://farmrpg.com/index.php#!/fish.php')

USERNAME = 'GoCheeto'
PASSWORD = 'letbin64'
FISHING_IDS = [4]
FISHING_LENGTH = 60 # seconds


time.sleep(5) 

"""
<a href="fish.php" data-view=".view-main" class="item-link close-panel">
    <div class="item-content">
        <div class="item-media"><img src="/img/items/pond_sm.png" class="itemimg">/div>
        <div class="item-inner">
            <div class="item-title">Go Fishing<br><span style="font-size: 11px">See what you can catch</span></div>
        </div>
    </div>
</a>
"""
# login_link = driver.find_element(By.XPATH, f'//a[@href="login.php"]')
# login_link.click()

username_box = driver.find_element(By.NAME, 'username')
username_box.clear()
username_box.send_keys(USERNAME)

pw_box = driver.find_element(By.NAME, 'password')
pw_box.clear()
pw_box.send_keys(PASSWORD)

pw_box.send_keys(Keys.RETURN)

time.sleep(1)

fishing_link = driver.find_element(By.XPATH, f'//a[@href="fish.php"]')
fishing_link.click()

time.sleep(1)

for fishing_id in FISHING_IDS:
    fishing_link = driver.find_element(By.XPATH, f'//a[@href="fishing.php?id={fishing_id}"]')
    fishing_link.click()

    time.sleep(1)

    start_time = time.time()
    while time.time() - start_time < FISHING_LENGTH:
        try:
            fish = driver.find_element(By.CLASS_NAME, f'fish f11 catch')
            print('FOUND FISH')
            fish.click()
            time.sleep(1)
        except NoSuchElementException:
            time.sleep(.2)
            



time.sleep(5) # Let the user actually see something!

driver.quit()

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