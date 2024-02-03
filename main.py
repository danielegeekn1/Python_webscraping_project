from bs4 import BeautifulSoup
import requests

# with open('home.html', 'r') as html_file:
#     content = html_file.read()
    
#     soup = BeautifulSoup(content, 'lxml')
#     site_sections = soup.find_all('div', class_='section')
#     for site_section in site_sections:
#         site_title = site_section.h1.text
#         site_course_price = site_section.h2.text.split()[-1]
#         print(f'{site_title} costs {site_course_price}')

esa_site = requests.get('https://www.esa.int/Space_in_Member_States/Italy').text
print(esa_site)
soup = BeautifulSoup(esa_site, 'lxml')
esa_stories_title = soup.find_all('h3', class_='heading')
for esa_story_title in esa_stories_title:
    esa_title = esa_story_title.text
    print(esa_title)