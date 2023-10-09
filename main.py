import requests
import time
from bs4 import BeautifulSoup
import pygame

# Initialize Pygame
pygame.mixer.init()

# URL of the webpage
url = "https://www.flipkart.com/apple-2022-macbook-air-m2-8-gb-256-gb-ssd-mac-os-monterey-mly33hn-a/p/itm0946c05e6335c?pid=COMGFB2GMCRXZG85&lid=LSTCOMGFB2GMCRXZG859PGKWX&marketplace=FLIPKART&q=macbook+air+m2&store=6bo%2Fb5g&spotlightTagId=FkPickId_6bo%2Fb5g&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_ps&fm=search-autosuggest&iid=f5462bf3-59f9-4872-9895-18b38783a47b.COMGFB2GMCRXZG85.SEARCH&ppt=sp&ppn=sp&ssid=l2czlrrzgg0000001696831624039&qH=5be12f29ec3566a2"

# Set headers to mimic a web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
}

session = requests.Session()

default_price = '₹91,990'
alarm_location = '/Users/username/Downloads/alarm.mp3';

# Attempt to access the URL with retries
for _ in range(3):  # You can adjust the number of retries
    response = session.get(url, headers=headers)
    
    if response.status_code == 200:
        break
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)
        print("Retrying...")
        time.sleep(5)  # Wait for a few seconds before retrying

while True:
    # Check if the request was successful
    if response.status_code == 200:
        print("Request to the URL was successful.")

        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Use the provided XPath to locate the element with the price
        price_element = soup.select_one("#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div:nth-child(2) > div > div.dyC4hf > div.CEmiEU > div > div._30jeq3._16Jk6d")

        if price_element:
            print("Price element found in the HTML.")
            
            # Extract the text from the element
            price = price_element.get_text(strip=True)
            print("Price:", price)
            
            # Check if the price is not equal to the default price
            if price != default_price:
                print("Price has changed! Sounding the alarm.")
                
                # Play an alarm sound
                pygame.mixer.music.load(alarm_location)  # Replace "alarm.mp3" with the path to your alarm sound file
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pass  # Wait for the alarm to finish playing
        else:
            print("Price element not found. Check your selector.")
            # Play an alarm sound
            pygame.mixer.music.load(alarm_location)  # Replace "alarm.mp3" with the path to your alarm sound file
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pass  # Wait for the alarm to finish playing
    else:
        print("Failed to retrieve the webpage after retries. Please check the URL and try again later.")

    time.sleep(10)
