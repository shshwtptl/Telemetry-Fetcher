import fastf1

year = int
gp = int
type = str

def start():
    print("This is a development build. Started. \n")
    fetchData()


def fetchData():
    global year, gp, type

    year = int(input("year? "))
    gp = input("gp? ")
    type = input("type? ")

    session = fastf1.get_session(year, gp, f"{type}")
    print(session.name)

start()
