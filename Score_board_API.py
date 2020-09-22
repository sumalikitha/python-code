'''
Created on Sep 15, 2020

@author: 
'''

import requests
import json
from builtins import str

startDate="2020-01-12"
endDate="2020-01-19"
teaamRankingUrl="https://delivery.chalk247.com/team_rankings/NFL.json?api_key="   #  74db8efa2a6db279393b433d97c2bc843f8e32b0
url="https://delivery.chalk247.com/scoreboard/NFL/"+startDate+"/"+endDate+".json?api_key=";
api_key="74db8efa2a6db279393b433d97c2bc843f8e32b0"
scoreboardPayload =requests.get(url+api_key)
scoreboardPayload=scoreboardPayload.json()
teamRankingPayload =requests.get(teaamRankingUrl+api_key)

teamRankingPayload =teamRankingPayload.json()
#print(teamRankingPayload)

displayEventDetails=list()


keys=["event_id","away_team_id","away_nick_name","away_city","home_team_id"]
 
for tmp in scoreboardPayload.keys():
    if tmp !="hash":
       
        for dataKey in scoreboardPayload[tmp].keys():
            for  keydata in scoreboardPayload[tmp][dataKey]:
                #print(keydata+""+ "TOP level")
                for keydataa2 in scoreboardPayload[tmp][dataKey]['data'].keys():
                    print("keyis "+keydataa2)
                    eventDetails={}
                    #print("keydataa2::"+keydataa2)                    #if scoreboardPayload[tmp][dataKey][keydata][keydataa2] is not str():
                    print(scoreboardPayload[tmp][dataKey]['data'][keydataa2])
                    for keylowLevel in scoreboardPayload[tmp][dataKey]['data'][keydataa2].keys():
                        if keylowLevel in keys:
                            
                                eventDetails[keylowLevel]=scoreboardPayload[tmp][dataKey]['data'][keydataa2][keylowLevel]
                        
                    #print(keydataa2)
                    #print(scoreboardPayload[tmp][dataKey][keydata][keydataa2])
                 
                #eventDetails["event_id"]=scoreboardPayload[tmp][dataKey][keydata]["event_id"]
                    displayEventDetails.append(eventDetails)
                
print(displayEventDetails)
for tmp in displayEventDetails:
    print(tmp)
                #for keydataa2 in scoreboardPayload[tmp][dataKey][keydata].keys():
                    
            








