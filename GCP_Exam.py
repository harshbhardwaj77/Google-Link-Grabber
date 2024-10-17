from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import csv
import time

# Path to your ChromeDriver
CHROME_DRIVER_PATH = 'C:/Program Files/WebDriver/chromedriver.exe'

# Function to search Google using Selenium and extract the first link
def google_search_selenium(query):
    # Create a Service object to specify the ChromeDriver path
    service = Service(CHROME_DRIVER_PATH)
    
    # Initialize the Chrome WebDriver with the service object
    driver = webdriver.Chrome(service=service)
    
    driver.get('https://www.google.com')
    
    # Find the search box
    search_box = driver.find_element("name", "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    
    time.sleep(3)  # Wait for search results to load
    
    # Find all search result links
    search_results = driver.find_elements("xpath", "//a[@href]")
    
    for result in search_results:
        link = result.get_attribute('href')
        if 'examtopics.com' in link:
            driver.quit()
            return link
    
    driver.quit()
    return None

# Function to save the results to a CSV file
def save_to_csv(data, filename="gcp_network_exam_questions_selenium.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Question Number", "Link"])
        for row in data:
            writer.writerow(row)

# Main function to perform search for questions 66 to 172
def main():
    search_results = []
    
    for question_num in range(1, 173):  # Start from question 66 to 172
        query = f"examtopics gcp network engineer question {question_num}"
        print(f"Searching for question {question_num}...")
        link = google_search_selenium(query)
        if link:
            search_results.append((question_num, link))
            print(f"Found: {link}")
        else:
            print(f"No link found for question {question_num}")
        time.sleep(3)  # Slight delay between searches
    
    # Save results to CSV
    save_to_csv(search_results)

if __name__ == "__main__":
    main()
