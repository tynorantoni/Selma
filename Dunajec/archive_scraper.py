import zipfile
import requests


ARCHIVE_URL = 'https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_hydrologiczne/dobowe/'

#url example 'https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_hydrologiczne/dobowe/1951/codz_1951_01.zip'

def download_zip_archive(year,month):
    req = requests.get('{0}{1}/codz_{1}_{2}.zip'.format(ARCHIVE_URL,year,month))
    filename = 'Input\{0}_{1}.zip'.format(year,month)
    with open(filename,'wb') as output_file:
        output_file.write(req.content)

    with zipfile.ZipFile(filename,'r') as zip_extract:
        zip_extract.extractall('Input\extracted')
    

