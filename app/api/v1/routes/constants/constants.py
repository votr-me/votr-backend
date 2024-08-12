# List of valid state FIPS codes
VALID_STATE_FIPS_CODES = [
    "01",
    "02",
    "04",
    "05",
    "06",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "41",
    "42",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "53",
    "54",
    "55",
    "56",
]

VALID_CONGRESSIONAL_DISTRICTS_BY_STATE_FIPS = {
    "01": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 8)
    ],  # Alabama (7 districts)
    "02": ["00"],  # Alaska (At-Large)
    "04": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 10)
    ],  # Arizona (9 districts)
    "05": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 5)
    ],  # Arkansas (4 districts)
    "06": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 53)
    ],  # California (52 districts)
    "08": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 8)
    ],  # Colorado (7 districts)
    "09": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 6)
    ],  # Connecticut (5 districts)
    "10": ["00"],  # Delaware (At-Large)
    "11": ["00"],  # District of Columbia (At-Large, non-voting)
    "12": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 29)
    ],  # Florida (28 districts)
    "13": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 15)
    ],  # Georgia (14 districts)
    "15": ["00"],  # Hawaii (At-Large)
    "16": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 3)
    ],  # Idaho (2 districts)
    "17": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 18)
    ],  # Illinois (17 districts)
    "18": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 10)
    ],  # Indiana (9 districts)
    "19": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 5)
    ],  # Iowa (4 districts)
    "20": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 4)
    ],  # Kansas (4 districts)
    "21": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 7)
    ],  # Kentucky (6 districts)
    "22": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 7)
    ],  # Louisiana (6 districts)
    "23": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 3)
    ],  # Maine (2 districts)
    "24": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 9)
    ],  # Maryland (8 districts)
    "25": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 10)
    ],  # Massachusetts (9 districts)
    "26": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 14)
    ],  # Michigan (13 districts)
    "27": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 9)
    ],  # Minnesota (8 districts)
    "28": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 4)
    ],  # Mississippi (4 districts)
    "29": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 9)
    ],  # Missouri (8 districts)
    "30": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 2)
    ],  # Montana (2 districts)
    "31": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 4)
    ],  # Nebraska (3 districts)
    "32": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 5)
    ],  # Nevada (4 districts)
    "33": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 3)
    ],  # New Hampshire (2 districts)
    "34": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 13)
    ],  # New Jersey (12 districts)
    "35": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 4)
    ],  # New Mexico (3 districts)
    "36": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 27)
    ],  # New York (26 districts)
    "37": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 14)
    ],  # North Carolina (14 districts)
    "38": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 4)
    ],  # North Dakota (1 district, at-large)
    "39": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 4)
    ],  # Ohio (15 districts)
    "40": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 5)
    ],  # Oklahoma (5 districts)
    "41": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 6)
    ],  # Oregon (6 districts)
    "42": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 20)
    ],  # Pennsylvania (17 districts)
    "44": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 2)
    ],  # Rhode Island (2 districts)
    "45": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 8)
    ],  # South Carolina (7 districts)
    "46": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 2)
    ],  # South Dakota (At-Large)
    "47": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 10)
    ],  # Tennessee (9 districts)
    "48": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 39)
    ],  # Texas (38 districts)
    "49": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 5)
    ],  # Utah (4 districts)
    "50": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 12)
    ],  # Vermont (At-Large)
    "51": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 12)
    ],  # Virginia (11 districts)
    "53": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 11)
    ],  # Washington (10 districts)
    "54": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 3)
    ],  # West Virginia (2 districts)
    "55": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 9)
    ],  # Wisconsin (8 districts)
    "56": [
        f"0{str(i)}" if i < 10 else str(i) for i in range(1, 2)
    ],  # Wyoming (At-Large)
}
