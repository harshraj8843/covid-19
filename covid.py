import json
import os
import ssl
import urllib.request
import urllib.parse
import urllib.error
from time import sleep

# screen clear function
def sclear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# api url
url = "https://api.covid19india.org/state_district_wise.json"

# load data
html = urllib.request.urlopen(url, context=ctx)
data = html.read()
info = json.loads(data)

# main function
while True:
    activecount = 0
    confirmedcount = 0
    decreasedcount = 0
    recoveredcount = 0
    states = list()
    for state in info:
        states.append(state)
    for state in states:
        districts = list()
        info1 = info[state]
        info2 = info1['districtData']
        for district in info2:
            districts.append(district)
        for district in districts:
            info3 = info2[district]
            active = info3['active']
            activecount += active
            confirmed = info3['confirmed']
            confirmedcount += confirmed
            decreased = info3['deceased']
            decreasedcount += decreased
            recovered = info3['recovered']
            recoveredcount += recovered
    sclear()
    print()
    print('========== REAL TIME DATA ==============\n')
    print('Country : INDIA')
    print('\tTotal Confirmed : ', confirmedcount)
    print('\tTotal Active : ', activecount)
    print('\tTotal Recovered : ', recoveredcount)
    print('\tTotal Decreased : ', decreasedcount)
    print('=========================================\n')
    states1 = list()
    for state in info:
        state = state.strip()
        state = state.lower()
        states1.append(state)
    s = input('Enter State Name : ')
    s = s.strip()
    s = s.lower()
    if s in states1:
        sactivecount = 0
        sconfirmedcount = 0
        sdecreasedcount = 0
        srecoveredcount = 0
        for state in states:
            if(s == state.lower().strip()):
                districts = list()
                districts1 = list()
                info1 = info[state]
                info2 = info1['districtData']
                for district in info2:
                    districts.append(district)
                    districts1.append(district.strip().lower())
                for district in districts:
                    info3 = info2[district]
                    sactive = info3['active']
                    sactivecount += sactive
                    sconfirmed = info3['confirmed']
                    sconfirmedcount += sconfirmed
                    sdecreased = info3['deceased']
                    sdecreasedcount += sdecreased
                    srecovered = info3['recovered']
                    srecoveredcount += srecovered
                sclear()
                print('\n==========================================\n')
                print('\tState : ', s.upper(), '\n')
                print('\t\tTotal Confirmed : ', sconfirmedcount)
                print('\t\tTotal Active : ', sactivecount)
                print('\t\tTotal Recovered : ', srecoveredcount)
                print('\t\tTotal Decreased : ', sdecreasedcount)
                print('\n==========================================\n')
                d = input('Enter District : ')
                d = d.strip().lower()
                if d in districts1:
                    dactivecount = 0
                    dconfirmedcount = 0
                    ddecreasedcount = 0
                    drecoveredcount = 0
                    for district in districts:
                        if(d == district.strip().lower()):
                            info1 = info[state]
                            info2 = info1['districtData']
                            info3 = info2[district]
                            dactive = info3['active']
                            dactivecount += dactive
                            dconfirmed = info3['confirmed']
                            dconfirmedcount += dconfirmed
                            ddecreased = info3['deceased']
                            ddecreasedcount += ddecreased
                            drecovered = info3['recovered']
                            drecoveredcount += drecovered
                    sclear()
                    print('\n==========================================\n')
                    print('\tDistrict : ', d.upper(), '\n')
                    print('\t\tTotal Confirmed : ', dconfirmedcount)
                    print('\t\tTotal Active : ', dactivecount)
                    print('\t\tTotal Recovered : ', drecoveredcount)
                    print('\t\tTotal Decreased : ', ddecreasedcount)
                    print('\n==========================================\n')
                    sleep(3)
                else:
                    print('No record found found')
                    sleep(1)
    else:
        print('No record found in database')
        ##################   Thank You    ##############################
