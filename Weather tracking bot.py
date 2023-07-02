
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests


OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
my_api = "fc5b526181f341578f988874e63a0db5"

parameters = {
    "lat": 24.860735,
    "lng": 67.001137,
    "appid": my_api,
}


end_point = "https://api.openweathermap.org/data/2.5/onecall?lat=24.860735&lon=67.001137&exclude=current,minutely,daily&appid=fc5b526181f341578f988874e63a0db5"
response = requests.get(end_point)
response.raise_for_status()

weather_data = response.json()
# print(weather_data)
hourly_data = weather_data['hourly']
weather_id = weather_data['hourly'][1]['weather'][0]['id']
print(weather_id)
will_not_rain = True
if weather_id > 700:
    will_not_rain = False
    service = Service("C:Development\chromedriver")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.twitter.com")
    driver.maximize_window()
    time.sleep(5)
    login = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div/div/div/div/div[1]/a/div/span/span')
    login.click()
    time.sleep(5)
    email_entry = driver.find_element(By.CLASS_NAME, 'r-30o5oe')
    email_entry.send_keys("YOUR USER NAME")
    email_entry.send_keys(Keys.ENTER)
    time.sleep(5)
    password_entry = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password_entry.send_keys("YOUR PASSWORD")
    password_entry.send_keys(Keys.ENTER)
    # time.sleep(5)
    # log_in_button = driver.find_element(By.CLASS_NAME, "css-901oao")
    # log_in_button.click()
    def get_quote():
        quote = "It will rain because, Weather Tomorrow is:\n"\
                "36°C°F\n"\
                "Precipitation: 50%\n"\
                "Humidity: 58%\n"\
                "Wind: 23 km/h\n"
        return quote
    time.sleep(5)
    tweet_text = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
    tweet_text.send_keys(get_quote())
    print(f"Tweet has been written successfully!")
    time.sleep(5)
    tweet_button = driver.find_element(By.XPATH, "//*[text()='Tweet']")
    driver.execute_script("arguments[0].click();", tweet_button)
    print(f"{tweet_button.text} has been sent successfully!")

if will_not_rain:
    print("No rain tommorrow!")
    
