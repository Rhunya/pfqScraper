from pprint import pprint
from bs4 import BeautifulSoup as bs
import time
import re
import requests
from html_table_parser.parser import HTMLTableParser
import urllib.request
# from requests_html import HTMLSession

# html to scrape
html =''''''

def url_get_contents(uri):
    req = urllib.request.Request(url=uri)
    f = urllib.request.urlopen(req)
    return f.read()

# url to scrape
regionList = {'Johto','Hoenn'}
baseurl = "https://pokefarm.wiki/List_of_Pok%C3%A9mon/"
for region in regionList:
    url = baseurl + region
    xhtml = url_get_contents(url).decode('utf-8')

    p = HTMLTableParser()
    p.feed(xhtml)
    pokemonList = p.tables[1]
    list = []

# extract relevant info from html
    for index in range(0, len(pokemonList)):
        pokeInfo = pokemonList[index]
        if (pokeInfo[0] != 'IMG Codes' and pokeInfo[0] != 'Pokémon' and index+1 < len(pokemonList)):
            codes = pokemonList[index + 1]
            eggCode = codes[1]
            normCode = codes[2]
            normCodeF = ''
            if "Female" in normCode:
                temp = normCode
                normCode = temp.split(" Female ")[0]
                normCodeF = temp.split(" Female ")[1]
            shinyCode = codes[3]
            shinyCodeF = ''
            if "Female" in shinyCode:
                temp = shinyCode
                shinyCode = temp.split(" Female ")[0]
                shinyCodeF = temp.split(" Female ")[1]
            albinoCode = codes[4]
            albinoCodeF = ''
            if "Female" in albinoCode:
                temp = albinoCode
                albinoCode = temp.split(" Female ")[0]
                albinoCodeF = temp.split(" Female ")[1]
            melCode = codes[5]
            melCodeF = ''
            if "Female" in melCode:
                temp = melCode
                melCode = temp.split(" Female ")[0]
                melCodeF = temp.split(" Female ")[1]
            poke_string = {"pokemon": pokeInfo[0],
                            "egg_code": eggCode,
                            "normal_code": normCode,
                            "normal_code_F": normCodeF,
                            "shiny_code": shinyCode,
                            "shiny_code_F": shinyCodeF,
                            "albino_code": albinoCode,
                            "albino_code_F": albinoCodeF,
                            "melanistic_code": melCode,
                            "melanistic_code_F": melCodeF
            }
            list.append(poke_string) 
            print(poke_string)
time.sleep(1)