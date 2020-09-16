import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time

# - -
# References
# https://medium.com/@msalmon00/web-scraping-job-postings-from-indeed-96bd588dcb4b
# https://www.youtube.com/watch?v=XQgXKtPSzUI
# - -

URL = "https://www.indeed.co.uk/jobs?q=delivery+driver&l=United+Kingdom"
#conducting a request of the stated URL above:
page = requests.get(URL)
#specifying a desired format of “page” using the html parser - this allows python to read the various components of the page, rather than treating it as one long string.
soup = BeautifulSoup(page.text, "html.parser")
#printing soup in a more structured tree format that makes for easier reading
print(soup.prettify())

def extract_job_title_from_result(soup):
    jobs = []
    for div in soup.find_all(name="div", attrs={"class":"row"}):
        for a in div.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
            jobs.append(a["title"])

    return jobs

extract_job_title_from_result(soup)

def extract_job_title_from_result(soup):
    jobs = []
    for span in soup.find_all(name = "span", attrs={"class":"date"}):
    #for a in span.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
    #jobs.append(a["title"])
        print(span)

    return

