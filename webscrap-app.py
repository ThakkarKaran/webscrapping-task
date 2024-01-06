
from bs4 import BeautifulSoup
import csv

def scrape_flipkart_with_selenium(search_query):
    base_url = "https://www.flipkart.com/search?q="
    driver = None

    try:
       
        driver = webdriver.Chrome()

        
        driver.get(base_url + search_query)

      
        driver.implicitly_wait(10)

       
        page_source = driver.page_source

       
        soup = BeautifulSoup(page_source, 'html.parser')

        
        mobiles = soup.find_all('div', {'class': '_1AtVbE'})

        
        with open('flipkart_mobiles_selenium.csv', mode='w', newline='', encoding='utf-8') as csv_file:
            fieldnames = ['Product Name', 'Price', 'Ratings']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for mobile in mobiles:
                product_name = mobile.find('a', {'class': '_4rR01T'}).text.strip()
                price = mobile.find('div', {'class': '_30jeq3'}).text.strip()
                ratings = mobile.find('div', {'class': '_3LWZlK'}).text.strip()

             
                writer.writerow({'Product Name': product_name, 'Price': price, 'Ratings': ratings})

        print("Data extraction and storage completed successfully.")

    finally:
       
        driver.quit()

if __name__ == "__main__":
    search_query = "iPhone"
    scrape_flipkart_with_selenium(search_query)
