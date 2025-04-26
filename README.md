<<<<<<< HEAD
# **Workstudent-Job-Scraper**

## **Project Overview**
This project is a **Python-based web scraper** that uses **Selenium** to extract **Workstudent job listings** from **Indeed**, filtered for **Erlangen**. The extracted data is saved and then sent to a **Power Automate flow** for further processing and automation.

## **Features**
- **Automated Job Scraping:** Uses Selenium to navigate Indeed and extract job postings.
- **Filtering:** Only retrieves **Workstudent** positions in **Erlangen**.
- **Data Storage:** Saves extracted job data in a structured JSON format.
- **Integration with Power Automate:** Sends the extracted data to a Power Automate flow for further automation (e.g., notifications, reports, or database updates).
- **Docker Compatibility:** Supports execution in a Docker environment for consistent deployment.

## **Project Structure**
```
📂 Workstudent-Job-Scraper
│── 📂 data                   # Folder for storing extracted job data
│    ├── jobs.json            # Extracted job listings (saved here)
│── 📂 scripts                # Python scripts for scraping and automation
│    ├── Scraper.py           # Main Python script for Selenium web scraping
│── 📄 config.py              # Configuration file (URLs, API keys, settings)
│── 📄 requirements.txt       # Dependencies for the project
│── 📄 dockerfile             # Docker container setup
│── 📄 README.md              # Project documentation
```

## **Setup & Installation**
### **Prerequisites**
Ensure you have the following installed:
- Python 3.9
- Google Chrome / Edge
- ChromeDriver / EdgeDriver
- Selenium (`pip install selenium`)
- Docker (if running inside a container)

### **Installation Steps**
1. **Clone the repository:**
   ```sh
   git clone https://MMS51610353@dev.azure.com/MMS51610353/Workstudent-Job-Scraper/_git/Workstudent-Job-Scraper
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up your environment:**
   - Update `config.py` with the correct Indeed search URL, Power Automate webhook, and WebDriver settings.
   - Ensure the appropriate WebDriver is placed in your system PATH or project directory.

## **Usage**
### **Running the Scraper**
Run the script to start scraping job listings:
```sh
python scripts/Scraper.py
```

### **Sending Data to Power Automate**
- The script automatically formats and sends extracted data to a Power Automate flow.
- Ensure the Power Automate flow URL is correctly set in `config.py`.

## **Docker Setup**
To run the scraper inside a Docker container:
1. **Build the Docker image:**
   ```sh
   docker build -t Workstudent-Job-Scraper.
   ```
2. **Run the container:**
   ```sh
   docker run --rm Workstudent-Job-Scraper
   ```

## **Automation & Scheduling**
To run this scraper periodically, you can:
- Use **Windows Task Scheduler** (Windows) or **cron jobs** (Linux/Mac).
- Example cron job (runs daily at 8 AM):
  ```sh
  0 8 * * * python /path/to/Workstudent-Job-Scraper/scripts/Scraper.py
  ```

## **Contributing**
- Feel free to submit issues and pull requests!
- Follow best practices for **Python coding**, **Selenium usage**, and **API integration**.

## **License**
This project is licensed under the MIT License.

---
