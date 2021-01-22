import requests
from datetime import datetime

# URL = "https://www.officeholidays.com/ics-clean/{country}"
# alternative 
URL = "https://dias-festivos.eu/ical/{country}/2021"



def download(country: str) -> str:
    resp = requests.get(URL.format(country=country), allow_redirects=True)
    filename = f'./data/ics/{datetime.now().strftime("%Y%m")}_{country}.ics'

    if resp.status_code == 200:
        open(filename, "wb+").write(resp.content)
    else:
        pass
    return filename


if __name__ == "__main__":
    # testing purpose
    download("colombia")
