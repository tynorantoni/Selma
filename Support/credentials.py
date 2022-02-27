
def read_credentials():
    dicConfigData={}

    with open("Etc\credentials.txt",'r') as creds:
        list_of_values = creds.readlines()
    for element in list_of_values:
        element = element.split(',')
        dicConfigData[element[0]]=element[1].rstrip("\n")
    return dicConfigData

