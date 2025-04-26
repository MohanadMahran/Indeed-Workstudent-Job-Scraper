import os
import time
import logging
import json
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from config import INDEED_URL, DATA_FILE, CHROME_DRIVER_PATH, POWER_AUTOMATE_URL, SELENIUM_OPTIONS

# Configure Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Configure Selenium WebDriver
def get_webdriver():
    service = Service(CHROME_DRIVER_PATH)
    options = Options()
    for opt in SELENIUM_OPTIONS:
        options.add_argument(opt)
    return webdriver.Chrome(service=service, options=options)

# Scrape Web Page and Process Data
def scrape_and_process_data():
    logging.info("Starting job scraping...")
    driver = get_webdriver()
    driver.get(INDEED_URL)
    time.sleep(5)  
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(3)
    page_source = driver.page_source
    driver.quit()

    # Process the page source using BeautifulSoup
    soup = BeautifulSoup(page_source, "html.parser")
    jobs = []

    for job in soup.find_all("li", class_="css-1ac2h1w eu4oa1w0"):
        try:
            job_title = job.find("h2", class_="jobTitle").text.strip() if job.find("h2", class_="jobTitle") else "N/A"
            company = job.find("span", {"data-testid": "company-name"}).text.strip() if job.find("span", {"data-testid": "company-name"}) else "N/A"
            rating = job.find("span", {"data-testid": "holistic-rating"}).text.strip() if job.find("span", {"data-testid": "holistic-rating"}) else "N/A"
            location = job.find("div", {"data-testid": "text-location"}).text.strip() if job.find("div", {"data-testid": "text-location"}) else "N/A"
            job_type = job.find("div", {"data-testid": "attribute_snippet_testid"}).text.strip() if job.find("div", {"data-testid": "attribute_snippet_testid"}) else "N/A"
            responsibilities = " | ".join([li.text.strip() for li in job.find("div", {"data-testid": "jobsnippet_footer"}).find_all("li")]) if job.find("div", {"data-testid": "jobsnippet_footer"}) else "N/A"
            job_link = "https://www.indeed.com" + job.find("a", class_="jcs-JobTitle")["href"] if job.find("a", class_="jcs-JobTitle") else "N/A"

            jobs.append({
                "job_title": job_title,
                "company": company,
                "rating": rating,
                "location": location,
                "job_type": job_type,
                "responsibilities": responsibilities,
                "job_link": job_link
            })

        except Exception as e:
            logging.warning(f"Skipping a job due to error: {e}")

    logging.info(f"Extracted {len(jobs)} jobs.")
    return jobs

# Save Data to JSON
def save_to_json(jobs):
    try:
        os.makedirs("data", exist_ok=True)
        with open(os.path.join("data", "jobs.json"), "w", encoding="utf-8") as file:
            json.dump(jobs, file, ensure_ascii=False, indent=4)
        logging.info("Data successfully saved to data/jobs.json")
    except Exception as e:
        logging.error(f"Error saving to JSON: {e}")

# Send JSON to Power Automate
def send_to_power_automate():
    if not POWER_AUTOMATE_URL:
        logging.error("Power Automate URL is not configured.")
        return
    headers = {"Content-Type": "application/json"}
    with open(os.path.join("data", "jobs.json"), "r", encoding="utf-8") as file:
        data = json.load(file)
    response = requests.post(POWER_AUTOMATE_URL, json=data, headers=headers)
    if response.status_code == 200:
        logging.info("Successfully sent data to Power Automate.")
    else:
        logging.error(f"Failed to send data to Power Automate. Status code: {response.status_code}")

# Main Function
def main():
    logging.info("Job scraping started.")
    job_list = scrape_and_process_data()
    # Uncomment to save data to json file
    #save_to_json(job_list)
    send_to_power_automate()
    logging.info("Job scraping completed.")

# Local Execution
if __name__ == "__main__":
    main()