import os
from dataclasses import dataclass
from urllib.request import urlopen
import json
import csv
import time


baseLink = "https://api.openf1.org/v1/"
link = "" 
baseGenerated = False
queryGenerated = False
parent = ""


def driver():
    global parent
    a = "drivers?"
    parent = "driver"
    appendlink(a, parent)
def session():
    global parent
    a = "sessions?"
    parent = "session"
    appendlink(a, parent)
def carData():
    global parent
    a = "car_data?"
    parent = "car_data"
    appendlink(a, parent)
def wdc():
    global parent
    a = "championship_drivers?"
    parent = "wdc"
    appendlink(a, parent)
def wcc():
    global parent
    a = "championship_teams?"
    parent = "wcc"
    appendlink(a, parent)
def result():
    global parent
    a = "session_result?"
    parent = "result"
    appendlink(a, parent)

def start():
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
        lsDirectories()
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

    if(baseGenerated):
        for queryItem in queryArr:
            if queryItem.endpoint == inp:
                value = input(f"{queryItem.endpoint} = ")
                if(not queryGenerated):
                    queryGenerated = True
                    appendQuery(f"{queryItem.endpoint}={value}")
                else:
                    appendQuery(f"&{queryItem.endpoint}={value}")
                found = True
                break
    else:
        for dirItem in direc:
            if dirItem.name == inp:
                dirItem.func()
                found = True
                break

    if not found:
        print("Unknown Command.")
    del inp

def lsDirectories():
    clear()
    for i in direc:
        print(">>> " + i.name)
    checkInput()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def appendQuery(temp):
    global link
    global parent

    link += temp
    addQuery(parent)
    return link
    print(link)


def appendlink(temp, parent):
    global link
    global baseGenerated

    if(baseGenerated):
        link += temp
    if(not baseGenerated):
        baseGenerated = True
        link = baseLink + temp

    addQuery(parent)
    print(link)
    return link

def addQuery(parent):
    for queryItem in queryArr:
        for i in queryItem.parent:
            if(i == parent):
                print(queryItem.endpoint)
                break

    checkInput()

def reset():
    clear()
    del link
    baseGenerated = False
    queryGenerated = False

    print("The link, Identifiers and Queries have been RESET.")
    time.sleep(3)
    start()

@dataclass
class dirItem:
    name: ""
    func: ""

@dataclass
class queryItem:
    endpoint: ""
    parent: list[str]

direc = [
    dirItem("driver", driver),
    dirItem("session", session),
    dirItem("car_data", carData),
    dirItem("wdc", wdc),
    dirItem("wcc", wcc),
    dirItem("result", result)
]

queryArr = [
    queryItem("session_key", ["car_data", "wdc", "wcc", "driver", "result"]),
    queryItem("meeting_key", ["car_data", "wdc", "wcc", "driver", "result"]),

    queryItem("driver_number", ["car_data", "wdc", "driver", "result"]),
    
    queryItem("team_name", ["wcc", "driver"]),

    queryItem("points_current", ["wdc", "wcc"]),
    queryItem("points_start", ["wdc", "wcc"]),
    queryItem("position_start", ["wdc", "wcc"]),
    queryItem("position_current", ["wdc", "wcc"]),

    queryItem("brake", ["car_data"]),
    queryItem("date", ["car_data"]),
    queryItem("drs", ["car_data"]),
    queryItem("n_gear", ["car_data"]),
    queryItem("rpm", ["car_data"]),
    queryItem("speed", ["car_data"]),
    queryItem("throttle", ["car_data"]),


    queryItem("broadcast_name", ["driver"]),
    queryItem("first_name", ["driver"]),
    queryItem("full_name", ["driver"]),
    queryItem("headshot_url", ["driver"]),
    queryItem("last_name", ["driver"]),
    queryItem("name_acronym", ["driver"]),
    queryItem("team_colour", ["driver"]),

    queryItem("country_name", ["session"]),
    queryItem("circuit_short_name", ["session"]),
    queryItem("country_code", ["session"]),
    queryItem("country_key", ["session"]),
    queryItem("date_end", ["session"]),
    queryItem("date_start", ["session"]),
    queryItem("gmt_offset", ["session"]),
    queryItem("is_cancelled", ["session"]),
    queryItem("location", ["session"]),
    queryItem("session_name", ["session"]),
    queryItem("session_type", ["session"]),
    queryItem("year", ["session"]),

    queryItem("dnf", ["result"]),
    queryItem("dns", ["result"]),
    queryItem("dsq", ["result"]),
    queryItem("duration", ["result"]),
    queryItem("gap_to_leader", ["result"]),
    queryItem("number_of_laps", ["result"]),
    queryItem("position", ["result"]),


]

def curl():
    response = urlopen(link)
    data = json.loads(response.read().decode('utf-8'))
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
start()