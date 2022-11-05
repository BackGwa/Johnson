#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from datetime import datetime
import requests
import json

today = datetime.today()


# [함수] : API로 급식 정보 JSON 반환하기
def meal_info(school_type, school_code, add_year, add_month, add_date, aleg):
    
    year = today.year + add_year
    month = today.month + add_month
    day = today.day + add_date
    allergy = 'formed' if (aleg == True) else 'hidden'                                                       

    return f'https://schoolmenukr.ml/api/{school_type}/{school_code}?year={year}&month={month}&date={day}&allergy={allergy}'


# [함수] : 필요한 정보만 반환하기
def meal_zone(JSON, usetime, meal_value):
    
    mealzone = meal_value
    data = json.loads(JSON.text)
    result = ''
    
    if(usetime):
        hour = today.hour
        isbf = False if ((data['menu'][0]['breakfast']) == []) else True
        islc = False if ((data['menu'][0]['lunch']) == []) else True
        isdr = False if ((data['menu'][0]['dinner']) == []) else True
      
        if(isbf and islc and isdr):
            if(hour > 0 and hour < 8):
                mealzone = 'breakfast'
            elif(hour > 8 and hour < 14):
                mealzone = 'lunch'
            else:
                mealzone = 'dinner'
                
        elif(isbf and islc):
            mealzone = 'breakfast' if (hour > 0 and hour < 8) else 'lunch'
         
        elif(islc and isdr):     
            mealzone = 'lunch' if (hour > 0 and hour < 14) else 'dinner'
          
        elif(islc):
            mealzone = 'lunch'
            
        else:
            mealzone = 'None'
            
    if(usetime):
        result = ([mealzone] + data['menu'][0][f'{mealzone}']) if (mealzone != 'None') else ['급식 정보가 존재하지 않습니다.']
        
    elif((data['menu'][0][mealzone]) != []):
        result = [mealzone] + data['menu'][0][f'{mealzone}']
        
    else:
        result = ['급식 정보가 존재하지 않습니다.']
            
    return result


# [함수] : 알레르기 정보 변환
def aleg_info(mealinfo):
    
    if('{' in str(mealinfo)):
        result = (str(mealinfo['name']) + str(mealinfo['allergy']))
        return result
    else:
        return mealinfo


# [함수] : 급식 정보 가져오기
def now(school_type, school_code, add_value, aleg, usetime, zonevalue = 'NoneValue'):
    
    API = meal_info(school_type, school_code, add_value[0], add_value[1], add_value[2], aleg)
    response = requests.get(API)                                                                

    result = meal_zone(response, usetime, zonevalue)
    aleg_result = []

    if(aleg):
        for rtaleg in result:
            aleg_result += [aleg_info(rtaleg)]
        return aleg_result
    else:
        return result