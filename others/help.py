from dataclasses import dataclass


@dataclass
class command:
    name: str
    desc: str

commands = [
    command("help", "Shows all the useful commands."),
    command("link", "Shows the concurrent link."),
    command("curl", "Curls the link to fetch the data and saves to a json file."),
    command("reset", "Resets all the data, and restarts the program."),
    command("dir", "Shows all the directories."),
    command("exit", "Exits the program.")
]

def lsCommands():
    for i in commands:
        print(i.name + ": " + i.desc)
    print("\n")