import requests
from bs4 import BeautifulSoup


def get_story(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    data = soup.findAll("p")[1].text # The second <p> tag has the sentences
    male = data[data.find("He's"):data.find(" She's")]
    female = data[data.find("She's"):(len(data)-len(" They fight crime!"))]
    return male, female


def save_to_file(male, female):
    with open("male.txt", "a") as f:
        f.write(male + "\n")
        f.close()
    with open("female.txt", "a") as f:
        f.write(female + "\n")
        f.close()


if __name__ == '__main__':
    URL = 'https://theyfightcrime.org/'
    male, female = None, None
    for i in range(0, 50):
        male, female = get_story(URL)
        save_to_file(male, female)
