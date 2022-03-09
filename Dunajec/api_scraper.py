import requests

DUNAJEC_STATIONS = ['149200160','150200170','149200050','149200190','149200280','149200230','149200240']

def get_station_data(station_url):
    req = requests.get(station_url)
    json_response = req.json()

    return [station for station in json_response if station['id_stacji'] in DUNAJEC_STATIONS]
   
    