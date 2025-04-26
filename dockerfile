FROM python:3.9-slim

# Install required dependencies before Chrome
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    --no-install-recommends

# Install Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb || apt-get install -fy && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install ChromeDriver
RUN wget https://storage.googleapis.com/chrome-for-testing-public/133.0.6943.126/linux64/chromedriver-linux64.zip && \
    unzip chromedriver-linux64.zip && \
    mv chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf chromedriver-linux64.zip chromedriver-linux64

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies first (optimizes caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy necessary project files (excluding data/)
COPY config.py .
COPY scripts/Scraper.py scripts/

# Command to run the script
CMD ["python", "scripts/Scraper.py"]
