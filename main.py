# Author : Zer0 | CodeOpen
# Project: Link Shortener
# Language: Python
import pyshorteners

def cut_link(url):
    s = pyshorteners.Shortener()
    cut_link = s.tinyurl.short(url)
    return cut_link

url_original = str(input("Link : "))
link_cut = cut_link(url_original)
print(f"URL Original : {url_original}")
print(f"URL Encurtada : {link_cut}")