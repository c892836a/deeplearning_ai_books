from bs4 import BeautifulSoup

file = open("html\lesson2-week1_new.html", "w", encoding="utf-8")
soup = BeautifulSoup(open("html\lesson2-week1.html", encoding='utf-8'), features="html.parser")
file.write(soup.prettify())
file.close()
