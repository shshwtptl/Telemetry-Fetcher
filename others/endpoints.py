from dataclasses import dataclass

@dataclass
class dirItem:
    parent: str
    endpoint: str
    func: str
    desc: str


@dataclass
class queryItem:
    endpoint: str
    parent: list[str]
    template: str


direc = [
    dirItem("driver", "drivers?", "driver", "Shows all the endpoints that can be for Drivers."),
    dirItem("session", "session?", "session", "Shows all the endpoints that can be for Sessions."),
    dirItem("car_data", "car_data?", "carData", "Shows all the endpoints that can be for Cars."),
    dirItem("wdc", "championship_drivers?", "wdc", "Shows all the endpoints that can be for Driver's Championships."),
    dirItem("wcc", "championship_teams?", "wcc", "Shows all the endpoints that can be for Constructor's Championships."),
    dirItem("result", "session_result?", "reset", "Shows all the endpoints that can be for Sessions Results."),
]

queryArr = [
    queryItem("session_key", ["car_data", "wdc", "wcc", "driver", "result"], "session_key = {int} or {latest: for most recent session_key}"),
    queryItem("meeting_key", ["car_data", "wdc", "wcc", "driver", "result"], "meeting_key = {int} or {latest: for most recent meeting_key}"),

    queryItem("driver_number", ["car_data", "wdc", "driver", "result"], "driver_number = {int}"),

    queryItem("team_name", ["wcc", "driver"], "team_name = {str}"),

    queryItem("points_current", ["wdc", "wcc"], "points_current = {int}"),
    queryItem("points_start", ["wdc", "wcc"], "points_start = {int}"),
    queryItem("position_start", ["wdc", "wcc"], "position_start = {int}; This can be confusing, please refer to documentation;"),
    queryItem("position_current", ["wdc", "wcc"], "position_current = {int}; This can be confusing, please refer to documentation;"),

    queryItem("brake", ["car_data"], "brake = {int}; brake(%);"),
    queryItem("date", ["car_data"], "date = {int}; ISO 8601; date(YYYY-MM-DD); UTC;"),
    queryItem("drs", ["car_data"], "drs = {int}; This can be confusing, please refer to documentation;"),
    queryItem("n_gear", ["car_data"], "n_gear = {int}"),
    queryItem("rpm", ["car_data"], "rpm = {int}"),
    queryItem("speed", ["car_data"], "speed = {int}"),
    queryItem("throttle", ["car_data"], "throttle = {float}"),

    queryItem("broadcast_name", ["driver"], "broadcast_name = {str}"),
    queryItem("first_name", ["driver"], "first_name = {str}"),
    queryItem("full_name", ["driver"], "full_name = {str}"),
    queryItem("headshot_url", ["driver"], "headshot_url = {str}; This can be confusing, please refer to documentation;"),
    queryItem("last_name", ["driver"], "last_name = {str}"),
    queryItem("name_acronym", ["driver"], "name_acronym = {str}"),
    queryItem("team_colour", ["driver"], "team_colour = {hex}; team_colour(RRGGBB);"),

    queryItem("country_name", ["session"], "country_name = {str}"),
    queryItem("circuit_short_name", ["session"], "circuit_short_name = {str}"),
    queryItem("country_code", ["session"], "country_code = {str}; This can be confusing, please refer to documentation;"),
    queryItem("country_key", ["session"], "country_key = {int}"),
    queryItem("date_end", ["session"], "date_end = {int}"),
    queryItem("date_start", ["session"], "date_start = {int}"),
    queryItem("gmt_offset", ["session"], "gmt_offset = {int}"),
    queryItem("is_cancelled", ["session"], "is_cancelled = {bool}"),
    queryItem("location", ["session"], "location = {str}"),
    queryItem("session_name", ["session"], "session_name = {str}"),
    queryItem("session_type", ["session"], "session_type = {str}"),
    queryItem("year", ["session"], "year = {int}"),

    queryItem("dnf", ["result"], "dnf = {bool}"),
    queryItem("dns", ["result"], "dns = {bool}"),
    queryItem("dsq", ["result"], "dsq = {bool}"),
    queryItem("duration", ["result"], "duration = {int}; This can be confusing, please refer to documentation;"),
    queryItem("gap_to_leader", ["result"], "gap_to_leader = {float}"),
    queryItem("number_of_laps", ["result"], "number_of_laps = {int}"),
    queryItem("position", ["result"], "position = {int}"),

]