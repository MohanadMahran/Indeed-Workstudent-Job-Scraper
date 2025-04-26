# config.py

# Indeed search settings
INDEED_URL = "https://de.indeed.com/Jobs?q=Werkstudent&l=Erlangen&sc=0%3B&radius=25"

# Path to save extracted job data
DATA_FILE = "data/jobs.json"

# WebDriver settings (update path if needed)
CHROME_DRIVER_PATH = "/usr/local/bin/chromedriver"

# Power Automate webhook (replace with your actual URL)
POWER_AUTOMATE_URL = "https://your_power_automate_url.com"

# Selenium settings
SELENIUM_OPTIONS = [
    "--headless",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--disable-gpu",
    "--remote-debugging-port=9222",
    "--disable-blink-features=AutomationControlled",
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
]