# web scrapping using urrlib library

from urllib.request import urlopen

# url of the website where we perform scrapping
url = "http://olympus.realpython.org/profiles/aphrodite"

# to open web page, pass url to urlopen()

page = urlopen(url)

# urlopen() returns us HTTPResponse Object

print(page)

# For extracting the HTML from the page, first use the HTTPResponse object 
# .read() method which returns sequence of bytes and then use .decode() to decode the bytes to a string using UTF-8
html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)