import requests
from bs4 import BeautifulSoup
import subprocess

def GetEntirePage(URL):
    r = requests.get(URL)
    soup = BeautifulSoup(r.text,'html.parser')
    print(soup)

def CommandPipe(command):
    proc = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE, )

    return(proc.communicate()[0])

def GetPower():
    return CommandPipe("upower -d")

