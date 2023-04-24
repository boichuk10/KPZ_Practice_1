from bs4 import BeautifulSoup
import requests

def parse_ukd_data():
    u_r_l = "https://ukd.edu.ua/specialnosti-ta-osvitni-programi"

    respons = requests.get(u_r_l)
    htmlpage = respons.content
    soup = BeautifulSoup(htmlpage, 'html.parser')
    specialities = soup.find_all("div", class_="views-field views-field-title")

    for speciality in specialities:
        print(speciality.text.strip())