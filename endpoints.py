from dataclasses import dataclass

@dataclass
class dirItem:
    parent: str
    endpoint: str
    func: str


@dataclass
class queryItem:
    endpoint: str
    parent: list[str]


direc = [
    dirItem("driver", "drivers?", "driver"),
    dirItem("session", "session?", "session"),
    dirItem("car_data", "car_data?", "carData"),
    dirItem("wdc", "championship_drivers?", "wdc"),
    dirItem("wcc", "championship_teams?", "wcc"),
    dirItem("result", "session_result?", "reset")
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