#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 15:42:35 2021

@author: john
"""
import pandas as pd
from astral import LocationInfo
from astral.sun import sun
import datetime

fukuoka = LocationInfo(name='Fukuoka', region='Japan', timezone='Asia/Tokyo', latitude=33.5902, longitude=130.4017)

sets = [(2021,6,23,'Feast of Raḥmat (Mercy)'),
        (2021,7,9,'Martyrdom of the Báb'),
        (2021,7,12,'Feast of Kalimát (Words)'),
        (2021,7,31,'Feast of Kamál (Perfection)'),
        (2021,8,19,'Feast of Asmáʼ (Names)'),
        (2021,9,7,'Feast of ʻIzzat (Might)'),
        (2021,9,26,'Feast of Mas͟híyyat (Will)'),
        (2021,10,15,'Feast of ʻIlm (Knowledge)'),
        (2021,11,3,'Feast of Qudrat (Power)'),
        (2021,11,6,'Birth of the Báb'),
        (2021,11,7,"Birth of Bahá'u'lláh"),
        (2021,11,22,'Feast of Qawl (Speech)'),
        (2021,11,25,'Day of the Covenant'),
        (2021,11,27,"Ascension of ʻAbdu'l-Bahá"),
        (2021,12,11,"Feast of Masáʼil (Questions)"),
        (2021,12,30,"Feast of S͟haraf (Honour)"),
        (2022,1,18,"Feast of Sulṭán (Sovereignty)"),
        (2022,2,6,"Feast of Mulk (Dominion)"),
        (2022,2,25,"First Day of Ayyám-i-Há"),
        (2022,3,2,"Feast of ʻAlá' (Loftiness) - the Fast begins"),        
        (2022,3,21,"Feast of Bahá (Naw-Rúz)"),  
        ]
 
for set_ in sets:

    year = set_[0]   
    month = set_[1]
    day = set_[2]    
    event = set_[3]

    same_day = datetime.date(year,month,day)
    s_same_day = sun(fukuoka.observer, date=same_day, tzinfo=fukuoka.timezone)   
    same_day_week_day = same_day.strftime('%A')   

    day_before = same_day - datetime.timedelta(1)
    s_day_before = sun(fukuoka.observer, date=day_before, tzinfo=fukuoka.timezone)   
    day_before_week_day = day_before.strftime('%A') 


    sunset_day_before_pd = pd.Timestamp(s_day_before['sunset'])
    sunset_day_before_pd = sunset_day_before_pd.ceil('15min').to_pydatetime()

    hour = sunset_day_before_pd.hour
    minute = sunset_day_before_pd.minute 

    sunset_same_day_pd = pd.Timestamp(s_same_day['sunset'])
    sunset_same_day_pd = sunset_same_day_pd.floor('15min').to_pydatetime()

    hour = sunset_same_day_pd.hour
    minute = sunset_same_day_pd.minute 

    print(event,':', str(sunset_day_before_pd.date()) + ' ' +
          str(sunset_day_before_pd.time())[:5] + ' 〜 ' +
          str(sunset_same_day_pd.date())  + ' ' +
          str(sunset_same_day_pd.time())[:5]          )
