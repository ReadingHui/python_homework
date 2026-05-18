import pandas as pd
import csv
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from time import sleep

# Task 3: Write a program to extract this data

'''
- `get_books.py`. The program should import from selenium and webdriver_manager,/
 as shown in your lesson.  You also need pandas and json.
- Add code to load the web page given in task 2.
- Find all the li elements in that page for the search list results. /
You use the class values you stored in task 2 step 3.  /
Also use the tag name when you do the find, /
to make sure you get the right elements.
- Within your program, create an empty list called results.  /
You are going to add dict values to this list, one for each search result.
- Main loop: You iterate through the list of li entries.  /
For each, you find the entry that contains title of the book, /
and get the text for that entry.  /
Then you find the entries that contain the authors of the book, /
and get the text for each.  If you find more than one author, /
you want to join the author names with a semicolon ; between each.  /
Then you find the div that contains the format and the year, /
and then you find the span entry within it that contains this information.  /
You get that text too.  You now have three pieces of text.  /
Create a dict that stores these values, with the keys being Title, Author, /
and Format-Year.  Then append that dict to your results list.
- Create a DataFrame from this list of dicts.  Print the DataFrame.

'''

def main():
    # Loading the webpage
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    next_page_url = 'https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart'
    next_page_bool = True

    # Creating the empty result list
    results = []
    
    while next_page_bool:
        driver.get(next_page_url)

        # Finding all the li elements in that page for the search list results
        body = driver.find_element(By.CSS_SELECTOR,'body') # Find the first body element, typically only one
        if body:
            search_block = body.find_element(By.CSS_SELECTOR, 'div[class="col-md-12 results-list-items"]')
            if search_block:
                search_results = search_block.find_elements(By.CSS_SELECTOR, 'li[data-test-id="searchResultItem"]')
            else:
                raise ValueError('No search block.')
            try:
                page_nav = body.find_element(By.CSS_SELECTOR, 'nav[class="cp-pagination pagination--compact"]')
                next_page = page_nav.find_element(By.CSS_SELECTOR, 'li[class="cp-pagination-item pagination__next-chevron"]')
                next_page_url = next_page.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
                print(f'Next page is: {next_page_url.split('=')[-1]}')
            except NoSuchElementException:
                next_page_bool = False
        else:
            raise ValueError('Body not found.')


        # Main loop
        for entry in search_results:
            # Create the dict
            entry_dict = {
                'Title': None,
                'Author': None,
                'Format-Year': None
            }

            # Get title
            title = entry.find_element(By.CSS_SELECTOR, 'span[class="title-content"]').text

            # Get authors
            try:
                author_block = entry.find_element(By.CSS_SELECTOR, 'span[class="cp-author-link"]')
                author_list = author_block.find_elements(By.CSS_SELECTOR, 'a')
                author_list = [author.text for author in author_list]
            except NoSuchElementException:
                author_list = []
                print(f'There is no author for book {title}.')
            authors = ';'.join(author_list)
            
            # Get Format-Year
            try:
                format_year = entry.find_element(By.CSS_SELECTOR, 'span[class="display-info-primary"]').text
            except NoSuchElementException:
                format_year = None

            # Store info in dict
            entry_dict['Title'] = title
            entry_dict['Author'] = authors
            entry_dict['Format-Year'] = format_year

            # Append to the list
            results.append(entry_dict)

            sleep(2)
    
    driver.quit()
    result_df = pd.DataFrame(results)

    # Task 4: Write Out the Data
    result_df.to_csv('get_all_books.csv', index=False)
    print('CSV file created.')
    result_df.to_json('get_all_books.json', indent=4)
    print('JSON file created.')

if __name__ == '__main__':
    main()