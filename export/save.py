import os
import json
import csv
from urllib.request import urlopen

inp = str
filename = str

def save(link):
    global inp
    
    inp = input("csv or json?: ").lower()
    name = input("file name: ")
    os.makedirs("output", exist_ok=True)

    response = urlopen(link)
    data = json.loads(response.read().decode('utf-8'))

    if(inp == "csv"):
        saveCSV(data, name)
    if(inp == "json"):
        saveJson(data, name)
        

def saveCSV(data, name):
    global filename

    with open(f"output/{name}.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    filename = f"{name}.csv"

def saveJson(data, name):
    global filename

    with open(f"output/{name}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    filename = f"{name}.json"