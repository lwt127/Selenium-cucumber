from behave import given, when, then
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
'''
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://crypto.com/nft/marketplace")
text = "curated"
xpath = "//button[@data-test-id='marketplace-isCurated-button']"
myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
if driver.find_element_by_xpath(xpath).text.lower() == text.lower():
    driver.find_element_by_xpath(xpath).click()
'''

       
@given("Open the website")
def open_the_website(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://crypto.com/nft/")

    delay = 10 # seconds
    try:
        myElem = WebDriverWait(context.driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[text()="View Drop"]')))
        print("Visited to Crypto.com NFT")
    except TimeoutException:
        print ("Failed to visited to Crypto.com NFT")


@when('I go to "{text}"')
def I_go_to_text(context, text):
    context.driver.find_element_by_xpath("//*[text()='%s']"% str(text)).click()
    print("Click " + text)
    
    
@then('The title is "{text}"')
def The_titl_is_text(context, text):
    xpath = "//div[starts-with(@class, 'App_container')]"
    myElem = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    assert text in context.driver.find_element_by_xpath(xpath).text
    

@when('I click "Sort By"')
def I_click_Sort_By(context):
    xpath = "//*[@class='css-1nnpiam']"
    myElem = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    context.driver.execute_script("arguments[0].scrollIntoView();", context.driver.find_element_by_xpath("//*[text()='Top Collectibles']"))
    context.driver.find_element_by_xpath(xpath).click()
    print("Clicked the sort by dropdown link")


@when('I click "{text}" in the dropdown-list')
def I_click_text_in_the_dropdown_list(context,text):
    xpath = "//*[text()='%s'][@style]"% str(text)
    context.driver.find_element_by_xpath(xpath).click()
    assert context.driver.find_element_by_xpath("//*[@class='css-1nnpiam']").text == text
    print("Clicked " + text + " in the dropdown link")
    
@then('All Collectibles are sorted by "{text}"')
def All_Collectibles_are_sorted_by_text(context,text):
    xpath = "//button[@class='css-1mqtv8s']"
    myElem = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//button[@class='css-1mqtv8s'])[2]")))
    showMorebutton = context.driver.find_element_by_xpath("//*[text()='Show more']/parent::*")
    while True:
        try:
            context.driver.implicitly_wait(10)
            context.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            showMorebutton.click()       
            continue
        except:
            break
    amounts = []
    pure_number = []
    for eleme in context.driver.find_elements_by_xpath(xpath):
        if bool(re.search(r'\d', str(eleme.text).split(":")[-1].strip())):
            amounts.append(str(eleme.text).split(":")[-1].strip())
    for amount in amounts:
        if "K" in amount:
            pure_number.append(float(amount.replace("K", "")) * 1000)
    print(pure_number)
    assert all(earlier >= later for earlier, later in zip(pure_number, pure_number[1:]))


@then('I enter a valid email')
def I_enter_a_valid_address(context):
    email = 'dfsagfag@yahoo.com.hk'
    xpath = "//*[@placeholder='Email']"
    myElem = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    context.driver.find_element_by_xpath(xpath).send_keys(email)
    print("Entered " + email)

@then('I enter an invalid email')
def I_enter_an_invalid_email(context):
    email = '132431243425'
    xpath = "//*[@placeholder='Email']"
    myElem = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    context.driver.find_element_by_xpath(xpath).send_keys(email)
    print("Entered " + email)

@then('I click the subcription box')
def I_click_the_subscription_box(context):
    context.driver.find_element_by_xpath("//*[text()='By entering my email and subscribing I confirm and agree to the above.']/preceding-sibling::*").click()
    print("Clicked the subcription box")

@then('I click Subscribe button')
def I_click_Subscribe_button(context):
    context.driver.find_element_by_xpath("//*[text()='Subscribe']").click()
    print("Clicked subscribe button")
    

@then('It shows "{text}"')
def It_shows_text(context,text):
    time.sleep(1)
    assert context.driver.find_element_by_xpath("//*[text()='%s']"% str(text)).is_displayed()


@then('I scroll down')
def I_scroll_down(context):
    last_height = context.driver.execute_script("return document.body.scrollHeight")
    while True:
        context.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        new_height = context.driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break 
        last_height = new_height
      
@then('I click the cards')
def I_click_the_cards(context):   
    xpath = "//*[@class='NftCard_container__1SuzE']"
    for element in context.driver.find_elements_by_xpath(xpath):
        context.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@data-test-id='nftDetail-title']")))
        assert context.driver.find_element_by_xpath("//*[@data-test-id='nftDetail-img']").is_displayed()
        assert context.driver.find_element_by_xpath("//*[@data-test-id='nftDetail-title']").is_displayed()
        assert context.driver.find_element_by_xpath("//*[starts-with(@class, 'ShortUserProfile_container')]").is_displayed()
        #assert context.driver.find_element_by_xpath("//*[@data-test-id='nftDetail-description']").is_displayed()
        #assert context.driver.find_element_by_xpath("//button[text()='Place a bid']").is_displayed() or context.driver.find_element_by_xpath("//button[contains(text(),'Buy For')]").is_displayed()
        context.driver.find_element_by_xpath("//*[starts-with(@class, 'Cross_crossAnimation')]").click()

@then('I filter "{text}" cards')
def I_filter_text_cards_only(context,text):
    xpath = "//button[@data-test-id='marketplace-isCurated-button']"
    myElem = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    if context.driver.find_element_by_xpath(xpath).text.lower() == text.lower():
        context.driver.find_element_by_xpath(xpath).click()