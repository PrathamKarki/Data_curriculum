# Extracting Text from HTML with string method

from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"

# to open web page, pass url to urlopen()
page = urlopen(url)

print(page)


# For extracting the HTML from the page, first use the HTTPResponse object 
# .read() method which returns sequence of bytes and then use .decode

html_bytes = page.read()
html = html_bytes.decode("utf-8")


print(html)
 

# Now extracting text from HTML with string methods

title_index = html.find("<title>")
print(title_index)


start_index = title_index + len("<title>")
print(start_index)


# now to get the index of closing </title> tag by passing the string with find()
end_index = html.find("</title>")
print(end_index)


# finally, extracting the title by slicing the html string
title = html[start_index : end_index]
print(title)


