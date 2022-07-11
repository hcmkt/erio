import re
import os
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import functools

class Class1():
    def __init__(self, jnap):
        self.jnap = jnap

    @staticmethod
    def get_joined_netloc_and_path(url):
        parsed_url = urlparse(url)
        return parsed_url.netloc + parsed_url.path

    def get_netloc(self):
        return urlparse('//' + self.jnap).netloc
        
    def get_links(self):
        response = requests.get('http://' + self.jnap)
        soup = BeautifulSoup(response.content, 'html.parser')
        hrefs = set([a.get('href') for a in soup.find_all('a')])
        hrefs.discard(None)
        hrefs = set(map(functools.partial(urljoin, 'http://' + self.get_netloc()), hrefs))
        hrefs = set(map(Class1.get_joined_netloc_and_path, hrefs))
        return hrefs

class Class2():
    def __init__(self):
        self.jnaps = set()
        self.searched_jnaps = set()
        self.netlocs = set()

    def exists_jnaps(self):
        return True if self.jnaps else False

    def add_to_jnaps(self, jnap):
        self.jnaps.add(jnap)
    
    def pop_jnaps(self):
        return self.jnaps.pop()

    def add_to_searched_jnaps(self, jnap):
        self.searched_jnaps.add(jnap)

    def add_to_netlocs(self, jnap):
        self.netlocs.add(jnap)

    def is_searched(self, jnap):
        return True if jnap in self.searched_jnaps else False

if __name__ == '__main__':
    url = 'https://p-hone.info/'
    jnap = Class1.get_joined_netloc_and_path(url)
    c2 = Class2()
    c2.add_to_jnaps(jnap)
    while c2.exists_jnaps():
        jnap = c2.pop_jnaps()
        print(jnap)
        if c2.is_searched(jnap):
            continue
        c1 = Class1(jnap)
        links = c1.get_links()
        while links:
            link = links.pop()
            c2.add_to_jnaps(link)
        c2.add_to_searched_jnaps(jnap)
        c2.add_to_netlocs(c1.get_netloc())
        print(list(map(len, [c2.jnaps, c2.searched_jnaps, c2.netlocs])))