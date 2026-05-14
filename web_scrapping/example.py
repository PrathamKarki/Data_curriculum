from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/poseidon"

page = urlopen(url)

html = page.read().decode("utf-8")


start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")

title = html[start_index : end_index]

print(html)

print(title)

print(re.findall("ab*c", "abcd"))
print(re.findall("ab*c", "acc"))
print(re.findall("ab*c", "abdc"))