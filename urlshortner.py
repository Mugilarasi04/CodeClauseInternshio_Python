import pyshorteners


url=input("enter the url:")

def url_short(url):
    a=pyshorteners.Shortener()
    print(a.tinyurl.short(url))

url_short(url)