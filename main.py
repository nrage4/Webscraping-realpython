import requests
from bs4 import BeautifulSoup
import sqlite3
import threading

conn = sqlite3.connect('fake_python.db')
cur = conn.cursor()


def scraping():
    url = "https://realpython.github.io/fake-jobs/"
    web_page = requests.get(url)  # scrape HTML content from the web page
    soup = BeautifulSoup(web_page.content, "html.parser")

    # print(soup)

    results = soup.find(id="ResultsContainer")

    job_elements = results.find_all("div", class_="card-content")

    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        print(title_element.text)
        print(company_element.text)
        cur.execute('''INSERT INTO JOBS (JOB_DESC, COMPANY) VALUES(?,?)''', (title_element.text, company_element.text))
        print(title_element.text)
        print(company_element.text)
      


scraping()

threads=[]
thread_connection_1 = threading.Thread(target=scraping, args=[5])
# thread_connection_2 = threading.Thread(target=db_insert, args=[50])

conn.execute(''' SELECT * FROM JOBS''')
results_1 = cur.fetchall()
print(results_1)
conn.commit()
conn.close()
