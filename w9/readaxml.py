#kelly j 9-26-2020  learn together week 9, step 2.  setting upa virtual enviroment
#I am gong to install into my virtual enviroment 2 libraries. beautifulsoup4 and lxml
# so I can read a xml and print something from it.
#I modifed code from this url  https://www.geeksforgeeks.org/reading-and-writing-xml-files-in-python/
# to demostrate my virtual env.

from bs4 import BeautifulSoup  

with open("h82sl_serviceConfig.xml","r") as myconfig:
    myconfigData = myconfig.read()

    config = BeautifulSoup(myconfigData,"lxml")

    print(" ")
    theurl = config.find("hansen_url")
    thelogpath = config.find("hansen_logpath")
    print(theurl)
    print(thelogpath)
    # print(config.Hansen_URL)
    # print(myconfigData)