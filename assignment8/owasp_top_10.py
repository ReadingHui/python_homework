import csv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Task 6: Scraping Structured Data
def main():
    # Loading the webpage
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    start_url = 'https://owasp.org/www-project-top-ten/'
    driver.get(start_url)

    # Getting the most update link
    body = driver.find_element(by=By.CSS_SELECTOR, value='body[class="base-grid col-sidebar"]')
    if body:
        current_sec = body.find_element(by=By.CSS_SELECTOR, value='section[id="sec-main"]')
    if current_sec:
        current_p = current_sec.find_element(by=By.CSS_SELECTOR, value='p')
    if current_p:
        current_link = current_p.find_element(by=By.CSS_SELECTOR, value='a').get_attribute('href')
    if current_link:
        print(f'Most updated link is: {current_link}')
        driver.get(current_link)

    # Getting the list in the new link
    links = []
    body = driver.find_element(by=By.CSS_SELECTOR, value='body[dir="ltr"]')
    if body:
        list_header_div = body.find_element(by=By.CSS_SELECTOR, value='div[class="md-content"]')
        list_header = list_header_div.find_element(by=By.CSS_SELECTOR, value='h3[id="top-102025-list"]')
        if list_header:
            top_ten_list = list_header.find_element(By.XPATH, 'following-sibling::ol' )
            link_elements = top_ten_list.find_elements(By.CSS_SELECTOR, 'li')
            for link in link_elements:
                name = link.text.strip()
                url = link.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
                links.append({'name': name, 'url': url})
    
    # Print the list to check
    print(links)

    # Writing to csv
    with open('python_homework/assignment8/owasp_top_10.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Link'])
        for link in links:
            writer.writerow([link['name'], link['url']])

    # Kill the session
    driver.quit()

if __name__ == "__main__":
    main()