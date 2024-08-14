import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountKey.json")


ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "009":
        {
            "name": "Shraddha Kapoor",
            "major": "Physics",
            "starting_year": 2021-22,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-01-01 08:15:00"
        },
    "32301":
        {
            "name": "Leonel Messi",
            "major": "Football",
            "starting_year": 2021-22,
            "total_attendance": 0,
            "standing": "A",
            "year": 4,
            "last_attendance_time": "2022-01-01 08:15:00"
        },
    "32302":
        {
            "name": "Omkar Patil",
            "major": "Chutiyappa",
            "starting_year": 2021-22,
            "total_attendance": 0,
            "standing": "O",
            "year": 4,
            "last_attendance_time": "2022-01-01 08:15:00"
        },
    "32303":
        {
            "name": "Shreyas patil",
            "major": "python",
            "starting_year": 2021-22,
            "total_attendance": 0,
            "standing": "S",
            "year": 4,
            "last_attendance_time": "2022-01-01 08:15:00"
        },
    "32305":
        {
            "name": "Aditya Bandgar",
            "major": "chutiya",
            "starting_year": 2021-22,
            "total_attendance": 0,
            "standing": "S",
            "year": 4,
            "last_attendance_time": "2022-01-01 08:15:00"
        },
    "32304":
        {
            "name": "Pranav Dangare",
            "major": "NSS ",
            "starting_year": 2021-22,
            "total_attendance": 0,
            "standing": "P",
            "year": 4,
            "last_attendance_time": "2022-01-01 08:15:00"


        },
    "32353":
        {
            "name": "Prasad Pawar",
            "major": "Entc",
            "starting_year": 2021-22,
            "total_attendance": 0,
            "standing": "z",
            "year": 4,
            "last_attendance_time": "2022-01-01 08:15:00"

        },
    "32307":
        {
            "name": "Awi kharmate",
            "major": "IT",
            "starting_year": 2021 - 22,
            "total_attendance": 0,
            "standing": "z",
            "year": 4,
            "last_attendance_time": "2022-01-01 08:15:00"

        },
    "31339":
        {
            "name": "Anup Kesarwani",
            "major": "Anup & Grammer",
            "starting_year": 2021 - 22,
            "total_attendance": 0,
            "standing": "z",
            "year": 4,
            "last_attendance_time": "2022-01-01 08:15:00"

        }
}

for key, value in data.items():
    if value is not None:
        ref.child(key).set(value)
    else:
        print(f"Skipping key {key} because value is None.")
