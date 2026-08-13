
# Telemetry Fetch

A tool for fetching Formula One telemetry data using OpenF1's API tool. It simplifies the data fetching process significantly and can be used by a normal user.

## Features

- Fetches all the telemetry data from every team/car at any date and session.
- Simplifies the workflow, instead of looking for endpoints, it helps you choose from a drop-list.
- Supports Query Endpoint values and directories.
- Formats the data into Json files. (soon CSV)

## Functions

- help

Shows all the directories that can be used the by the user to fetch the data.

- link

Shows the current link, which can also be customized later.

- curl

Fetches the data using the created link.

- reset

Resets all the parameters and links.

## Installation

Clone the repository:

```bash
git clone https://github.com/shshwtptl/Telemetry-Fetcher.git
cd Telemetry-Fetcher

python main.py
```

# NOTE

Many Endpoints and Directories are still missing, because OpenF1's doesn't let anyone fetch the data and show the directories.
