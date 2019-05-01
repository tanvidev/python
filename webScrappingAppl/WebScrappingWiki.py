import bs4
import requests

res = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)");

print(type(res));

print(res.text.encode("utf-8"));
# print(soup.encode("utf-8"))

soup = bs4.BeautifulSoup(res.text.encode("utf-8"),'lxml');
print(type(soup));

title = soup.select('title');

print("Title is - ");
print(title[0].getText());

arr = soup.select(".mw-headline");

for element in arr:
    print(element);
