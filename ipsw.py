import requests as r

gay = input("Input Device or Model ")
data = r.get("https://api.ipsw.me/v4/devices").json()
for device in data:
    if gay == device["name"] or gay == device["identifier"]:
        print("{}\n---------------\nID: {}\nBoard Config: {}\nPlatform: {}\nCPID: {}\nBDID: {}".format(device['name'], device['identifier'], device["boardconfig"], device["platform"], device["cpid"], device["bdid"]))