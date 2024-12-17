#This python script is intended to be used to log into voice.google.com
#It will take the username and password as arguments and return the cookies
#required to access the site.

import sys
import requests
import json
from bs4 import BeautifulSoup

def login(username = None, password = None):
    # Create a session
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0', 'content-language': 'en'})
    # we have to start at the welcome page to get the nessisary cookies and magic tokens
    welcome_page = session.get('https://voice.google.com', headers={'User-Agent': 'Mozilla/5.0', 'content-language': 'en'})
    soup = BeautifulSoup(welcome_page.text, 'html.parser')
    # Get the magic token
    magic = soup.find('input', {'name': 'jsh'})
    
    #print(soup.prettify())
    print(magic)

    # simulate clicking the login button
    signup_page = session.get('https://accounts.google.com/v3/signin/identifier?continue=https://', headers={'User-Agent': 'Mozilla/5.0', 'content-language': 'en'})
    #print location
    #soup = BeautifulSoup(signup_page.text.split("<footer")[0] + signup_page.text.split("</footer>")[1], 'html.parser')
    print (signup_page.headers)
    print (session.cookies)
    #print session.cookies
    #print(soup.prettify()[0:1000])
    #enter email
    email = soup.find('input', {'id': 'identifierId'})
    

#make this login runable from the command line
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 login.py <username> <password>")
        login()
    else:
        login(sys.argv[1], sys.argv[2])