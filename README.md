# Google Search with Selenium for Extracting Links from Search Queries

This project uses Selenium to automate Google searches and extract the first relevant link from the search results. By modifying the search query, the script can be used to extract links for any type of search, not limited to GCP Network Engineer exam questions. The results are saved to a CSV file.

## Prerequisites

### 1. Python
Ensure you have Python installed. If not, you can download and install it from [python.org](https://www.python.org/).

### 2. Selenium
Install Selenium, which is used to control the Chrome browser and perform automated web searches.

```bash
pip install selenium

3. ChromeDriver
You need to download the correct version of ChromeDriver that matches your installed version of Google Chrome. Here’s how to do it:

Download ChromeDriver: Go to the ChromeDriver download page and download the version that matches your installed Google Chrome version.

Extract and Move: After downloading, extract the chromedriver executable and move it to a location of your choice (e.g., C:\Program Files\WebDriver).

Set Path: Ensure that the path to the chromedriver.exe file is set correctly in the script:

python
Copy code
CHROME_DRIVER_PATH = 'C:/Program Files/WebDriver/chromedriver.exe'
Alternatively, you can add the directory containing chromedriver.exe to your system's PATH environment variable, so you won't need to specify the path in the script.

4. Google Chrome Browser
Ensure you have Google Chrome installed. The ChromeDriver needs to match the version of your installed Chrome browser.