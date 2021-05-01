# @author: Kyle Tracy

import os
import json
import requests
from bs4 import BeautifulSoup
import re

if __name__ == "__main__":
    URLbare = "https://forum.learnnavi.org/beginners/pivangkxo-ninavi-ko!-beginner-navi-chat-thread/"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    englishLines = []
    naviLines = []
    # This is how they make their URLS oddly enough, it increments by 20
    #for i in range(0, 4820, 20):
    for i in range(0, 4840, 20):
        print(i)
        if(i == 0): # page 1
            newURL = URLbare
        else:
            newURL = URLbare + str(i) + "/"
        print(newURL)
        
    
        result = requests.get(newURL, headers=headers)

        soup = BeautifulSoup(result.content, 'html.parser')
        posts = soup.find(id='forumposts')
        elems = posts.find_all('div', class_='post')
        
        for line in elems:
            try:

                msg = line.find(id=re.compile("(msg_)(.*?)"), class_="inner")
                
                sentence = msg.text.split()
                if(sentence[0] == "Quote"): # Lets avoid the mess that is parsing something with a quote
                    continue
                spoiler = msg.find(class_="spoiler")
            except Exception as e:
                print(e)
                continue
            #We've made it past the exception, it's good (enough)
            if(spoiler != None and msg != None):
                naviLines.append(msg.text.split('Spoiler')[0].strip()) # Sometimes the spoiler tag gets included in the navi
                #englishLines.append(spoiler.text.split('Spoiler')[1].strip())
                englishLines.append(spoiler.text.strip()) #Going to leave this to you to figure out the regex
                

    os.remove("englishlines.txt")
    f = open("englishlines.txt", "a")

    for line in englishLines:
        f.write(str(line) + "\n")
    f.close()

    os.remove("navilines.txt")
    n = open("navilines.txt", "a")

    for line in naviLines:
        n.write(str(line) + "\n")
    n.close()

