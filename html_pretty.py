import os
from os import walk
from bs4 import BeautifulSoup
f = []
for (dirpath, dirnames, filenames) in walk('html'):
    f.extend(filenames)
    break

for filename in f:
    if ".html" not in filename:
        continue
    soup = BeautifulSoup(open(os.path.join("html", filename), encoding="utf-8"), features="html.parser")
    file = open(os.path.join("html", filename), "w", encoding="utf-8")
    file.write(soup.prettify())
    file.close()
