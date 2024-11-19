from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome options
chrome_options = Options()
#chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# Path to your ChromeDriver (Update path to the correct one)
driver_service = Service(r"chromedriver-mac-x64/chromedriver")  # Ensure the path is correct

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=driver_service, options=chrome_options)

# Open the news website (e.g., Google News with "national sentiment" query)
driver.get("https://news.google.com/search?q=national+sentiment")

# Allow some time for the page to load
wait = WebDriverWait(driver, 20)

# Debugging: Print page title to verify we're on the right page
print("Page title:", driver.title)

try:
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    print("Page loaded successfully.")
except Exception as e:
    print(f"Error waiting for page to load: {e}")

# Try finding headline elements
try:
    # Find headlines using XPath (modify if incorrect)
    headlines = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//h3')))
    print(f"Found {len(headlines)} headlines.")  # Debug: Print number of headlines found
    
    # Extract and print headlines to verify they are correct
    for index, headline in enumerate(headlines):
        print(f"Headline {index + 1}: {headline.text}")
        
except Exception as e:
    print(f"Error finding headlines: {e}")

# Now, let's find the newspaper names and article descriptions (if they exist)
try:
    newspapers = driver.find_elements(By.CSS_SELECTOR, 'article .SVJrMe')  # Update this selector
    descriptions = driver.find_elements(By.CSS_SELECTOR, 'article .xBbh9')  # Update this selector

    # Print the number of newspapers and descriptions found
    print(f"Found {len(newspapers)} newspapers and {len(descriptions)} descriptions.")
    
    # Check if all lists are of equal length
    #if len(headlines) != len(newspapers) or len(headlines) != len(descriptions):
     #   print("Warning: The number of headlines, newspaper names, and descriptions do not match!")

    # Print the details
    for i in range(min(len(headlines), len(newspapers), len(descriptions))):
        headline_text = headlines[i].text
        newspaper_name = newspapers[i].text if i < len(newspapers) else 'N/A'
        article_about = descriptions[i].text if i < len(descriptions) else 'N/A'

        print(f"{i + 1}. Headline: {headline_text}\n   Newspaper: {newspaper_name}\n   Article About: {article_about}\n")
        
except Exception as e:
    print(f"Error finding newspapers or descriptions: {e}")

# Close the browser
driver.quit()
