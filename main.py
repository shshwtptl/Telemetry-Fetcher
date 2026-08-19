import os
from urllib.request import urlopen
import json
import others.endpoints as endpoints
import others.help as h
import time
import export.save as save


baseLink = "https://api.openf1.org/v1/"
link = "" 
baseGenerated = False
queryGenerated = False
parent = ""

def selectDir(endpoint):
    global parent

    parent = endpoint.parent
    appendlink(endpoint.endpoint, parent)

def start():
    global link

    link = baseLink
    clear()
    print("Telemetry Helper")
    print(">>> type 'help' for list of commands.")
    print(">>> type 'start' to get the base link.\n")
    checkInput()

def checkInput():
    inp = input(">>> ").lower()
    clear()
    
    found = False
    global queryGenerated
    
    if(inp=='help'):
        help()
        found = True
    if(inp=="link"):
        print(link)
        found = True
        checkInput()
    if(inp=="curl"):
        curl()
        found = True
    if(inp=="reset"):
        reset()
        found = True
    if(inp=="exit"):
        exit()
    if(inp=="dir"):
        lsDirectories()
        found = True

    if(baseGenerated):
        for queryItem in endpoints.queryArr:
            if queryItem.endpoint == inp:
                print(queryItem.template + "\n")
                value = input(f"{queryItem.endpoint} = ")
                clear()
                if(not queryGenerated):
                    queryGenerated = True
                    appendQuery(f"{queryItem.endpoint}={value}")
                else:
                    appendQuery(f"&{queryItem.endpoint}={value}")
                found = True
                break
    else:
        for dirItem in endpoints.direc:
            if dirItem.parent == inp:
                selectDir(dirItem)
                found = True
                break

    if not found:
        print("Unknown Command.")
    del inp

def lsDirectories():
    clear()

    print("These are the all directories you can browse. Every directory has their unique and common endpoints.\n")

    for i in endpoints.direc:
        print(">>> " + i.parent + "   -> " + i.desc)

    print("\n")
    print("Choose a directory to browse by typing it in the console.\n")
    checkInput()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def appendQuery(temp):
    global link
    global parent

    link += temp
    addQuery(parent)
    return link

def help():
    h.lsCommands()
    checkInput()

def appendlink(temp, parent):
    global link
    global baseGenerated

    if(baseGenerated):
        link += temp
    if(not baseGenerated):
        baseGenerated = True
        link = baseLink + temp

    addQuery(parent)
    return link

def addQuery(parent):
    for queryItem in endpoints.queryArr:
        for i in queryItem.parent:
            if(i == parent):
                print(queryItem.endpoint)
                break

    checkInput()

def reset():
    global link
    global baseGenerated
    global queryGenerated

    clear()

    link = ""
    baseGenerated = False
    queryGenerated = False

    print("The link, Identifiers and Queries have been RESET.")
    time.sleep(3)
    start()

def curl():
    global link

    # response = urlopen(link)
    # data = json.loads(response.read().decode('utf-8'))
    # with open("output.json", "w", encoding="utf-8") as f:
    #     json.dump(data, f, indent=4, ensure_ascii=False)

    save.save(link)

    print(f"Your Telemetry data has been saved to {save.filename}")
start()