from bs4 import BeautifulSoup
import requests
import time
import os

esa_titles_list = []
esa_data_article_list = []
esa_data_title = ''

def get_esa_site_informations():
    global esa_data_title
    esa_site = requests.get('https://www.esa.int/Space_in_Member_States/Italy').text
    soup = BeautifulSoup(esa_site, 'lxml')
    esa_posts = soup.find_all('span', class_='ll_440579')
    for esa_post in esa_posts:
        esa_post_titles = esa_post.find_all('h3', class_='heading')
        for esa_post_title in esa_post_titles:
            each_esa_post_title = esa_post_title.text
            print(each_esa_post_title)
            esa_titles_list.append(each_esa_post_title)

    esa_data_info = requests.get('https://www.esa.int/Space_in_Member_States/Italy/ESA_-_dati_e_cifre').text
    esa_data_soup = BeautifulSoup(esa_data_info, 'lxml')
    esa_data_title_tag = esa_data_soup.find('h1', class_='heading heading--main article__item')
    esa_data_title = esa_data_title_tag.text 

    esa_data_contents = esa_data_soup.find_all('p')
    folder_path = 'esa_post_articles'  # Specify the folder path
    os.makedirs(folder_path, exist_ok=True)  # Create the folder if it doesn't exist

    with open(os.path.join(folder_path, 'esa_data_article_list.txt'), 'a') as f_writer:
        for esa_data_content in esa_data_contents:
            esa_data_article = esa_data_content.text
            esa_data_article_list.append(esa_data_article)
            f_writer.write(esa_data_article + '\n')

if __name__ == '__main__':
    while True:
        get_esa_site_informations()
        time.sleep(100)