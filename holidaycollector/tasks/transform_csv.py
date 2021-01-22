from ics import Calendar
import pandas as pd
import os

def transform(filename):
    filepath = "./data/ics/{file}".format(file=filename)
    
    if not (os.path.exists(filepath)): raise FileNotFoundError

    calendar = Calendar(open(filepath, "r").read())
    country = filename.split("_")[1]
    data = [
        {
            "date": e.begin.date(),
            "name": e.name.strip(),
            "description": e.description.split("|")[0].strip(),
            # "description": e.description.replace(
            #     "Information provided by www.officeholidays.com", ""
            # )
            # .replace("\n", " ")
            # .split(' ,')[0]
            # .strip(),
            "location": country
        }
        for e in calendar.timeline
    ]

    csv_file = f"./data/csv/{filename.split('.ics')[0]}.csv"
    pd.DataFrame(data).to_csv(csv_file, index=False)

    return csv_file


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else "202101_argentina"
    transform(filename)