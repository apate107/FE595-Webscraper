import requests
from bs4 import BeautifulSoup


def get_story(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    data = soup.findAll("p")[1].text # The second <p> tag has the sentences
    male = data[data.find("He's"):data.find(" She's")]
    female = data[data.find("She's"):(len(data)-len(" They fight crime!"))]
    return male, female


if __name__ == '__main__':
    URL = 'https://theyfightcrime.org/'
    male, female = None, None
    with open("male.txt", "a") as fMale, open("female.txt", "a") as fFemale:
        for i in range(50):
            male, female = get_story(URL)
            fMale.write(male + '\n')
            fFemale.write(female + '\n')
