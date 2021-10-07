import requests
import argparse
import os
import sys
from bs4 import BeautifulSoup
parser = argparse.ArgumentParser()
parser.add_argument("-u","--url",help="Enter URL of the 1fichier hosted file you want to download.",required=False)
parser.add_argument("-o","--output",help="Enter Output location of the file, Filename is automatically grabbed.",required=False)
ty = parser.parse_args()


if ty.url == None:
    uri = input("Enter 1fichier URL: ")
else:
    uri = ty.url

if ty.output == None:
    outputLocation = os.path.dirname(__file__)
else:
    if ty.output[-1] == "\\" or ty.output[-1] == "/":
        outputLocation = ty.output[:-1]
    else:
        outputLocation = ty.output


print("1f-dl Tool by Port007")
print("Use -h arguement to get more information.")
print("Files will be dumped to run dir otherwise as specified by arguements.")
getRequest = requests.get(uri)
rawTextGET = getRequest.content
soup = BeautifulSoup(rawTextGET, 'html.parser')
testttt = list(soup.find_all('input'))
sepADZ = str(testttt[0]).replace('<input name="adz" type="hidden" value="',"").replace('"/>','')
ofoff = list(soup.find_all('td',class_="normal"))
filename = ofoff[1]
filename = str(filename).replace('<td class="normal">','').replace('</td>','')
data = {"adz": f"{sepADZ}","did": 0,"dlinline": "on"}
response = requests.post(uri, data)

rawtextPOST = response.content
soup = BeautifulSoup(rawtextPOST,'html.parser')
testttt = list(soup.find_all('a'))
sub = "Click here to download the file"
def neededFunction():
    global seperatedRealURI
    seperatedRealURI = None
    for text in testttt:
        if sub in text:
            seperatedRealURI = text
            seperatedRealURI = str(seperatedRealURI).replace('<a class="ok btn-general btn-orange" href="','').replace('" style="float:none;margin:auto;font-weight:bold;padding: 10px;margin: 10px;font-size:+1.6em;border:2px solid red">Click here to download the file</a>','')
            return seperatedRealURI
try:
    os.system(f'curl -o {outputLocation}\\{filename} "{neededFunction()}"')
except KeyboardInterrupt:
    print("Received Keyboard Interrupt, Terminating Process...")
    sys.stdin.read(1)
    sys.exit()
