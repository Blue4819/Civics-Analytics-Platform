from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# Path to your ChromeDriver
driver_service = Service(r"chromedriver-mac-x64")  # Update path as needed

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=driver_service, options=chrome_options)

# Open the news website (e.g., Google News with "national sentiment" query)
driver.get("https://news.google.com/search?q=national+sentiment")

# Allow some time for the page to load
time.sleep(2)

# Find headline elements (adjust the CSS selector to match the website's structure)
headlines = driver.find_elements(By.CSS_SELECTOR, 'article h3')  # Headline selector
newspapers = driver.find_elements(By.CSS_SELECTOR, 'article .SVJrMe')  # Newspaper name selector
descriptions = driver.find_elements(By.CSS_SELECTOR, 'article .xBbh9')  # Description selector (adjust if needed)

# Check if all lists are of equal length, otherwise print a warning
if len(headlines) != len(newspapers) or len(headlines) != len(descriptions):
    print("Warning: The number of headlines, newspaper names, and descriptions do not match!")

# Loop through and print headline with corresponding newspaper and description
for i in range(min(len(headlines), len(newspapers), len(descriptions))):  # Use the shortest list length
    headline_text = headlines[i].text
    newspaper_name = newspapers[i].text
    article_about = descriptions[i].text  # Extract description/snippet
    
    print(f"{i + 1}. Headline: {headline_text}\n   Newspaper: {newspaper_name}\n   Article About: {article_about}\n")

# Close the browser
driver.quit()
