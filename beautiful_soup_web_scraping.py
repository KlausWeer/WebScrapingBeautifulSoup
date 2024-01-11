from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.topjobs.lk/applicant/vacancybyfunctionalarea.jsp?FA=SDQ')
soup = BeautifulSoup(html_text.text,'lxml')

job_id_list=[]
for number in range(50):
    job_id_list.append('tr'+str(number))

for job_id in job_id_list:
    job= soup.find_all('tr',id=job_id)
    for item in job:
        company=item.find('h1')
        if company:
            print(company.text.strip())
