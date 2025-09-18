import requests
from bs4 import BeautifulSoup

# Function to scrape weather forecast from a weather website
def scrape_weather_forecast(USLA0033):
    url = f'https://www.weather.com/weather/today/l/{USLA0033}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    forecast_element = soup.find('div', class_='today_nowcard-phrase')
    if forecast_element:
        forecast = forecast_element.text.strip()
    else:
        forecast = 'Forecast data not available'
    return forecast

# Example usage of the function
weather_forecast = scrape_weather_forecast('USLA0033')  # Using correct location code for Baton Rouge
print('Weather Forecast:', weather_forecast)


# Function to scrape product prices from an e-commerce website
def scrape_product_prices(product_url):
    response = requests.get(product_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find('span', class_='price').text.strip()
    return price

# Function to scrape job listings from a job portal
def scrape_job_listings(job_portal_url):
    response = requests.get(job_portal_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    job_listings = []
    for job in soup.find_all('div', class_='job-listing'):
        title = job.find('h3', class_='job-title').text.strip()
        company = job.find('span', class_='company-name').text.strip()
        location = job.find('span', class_='job-location').text.strip()
        job_listings.append({'title': title, 'company': company, 'location': location})
    return job_listings

# Example usage of the functions
weather_forecast = scrape_weather_forecast('USLA0033')  # Using correct location code for Baton Rouge
print('Weather Forecast:', weather_forecast)

product_price = scrape_product_prices('https://www.amazon.com/dp/B08R6QN17D')
print('Product Price:', product_price)

job_listings = scrape_job_listings('https://www.indeed.com/jobs?q=software+engineer&l=New+York')
print('Job Listings:')
for job in job_listings:
    print(job)
