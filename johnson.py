from datetime import datetime
import requests
import json

today = datetime.today()

def meal_info(school_type, school_code, add_year, add_month, add_date, aleg):                   # 날짜로 급식 정보 가져오기
    year = today.year + add_year
    month = today.month + add_month
    day = today.day + add_date
    
    if(aleg == True):
        allergy = 'formed'
    elif(aleg == False):
        allergy = 'hidden'                                                         

    result = f'https://schoolmenukr.ml/api/{school_type}/{school_code}?year={year}&month={month}&date={day}&allergy={allergy}'
    
    return result

def meal_zone(JSON, usetime, meal_value):                                                       # 급식 정보 반환
    mealzone = meal_value
    data = json.loads(JSON.text)
    result = ''
    
    if(usetime):
        hour = today.hour
        
        isbf = True
        islc = True
        isdr = True
        
        if((data['menu'][0]['breakfast']) == []):
            isbf = False
        if((data['menu'][0]['lunch']) == []):
            islc = False
        if((data['menu'][0]['dinner']) == []):
            isdr = False
        
        if(isbf and islc and isdr):
            if(hour > 0 and hour < 8):
                mealzone = 'breakfast'
            elif(hour > 8 and hour < 14):
                mealzone = 'lunch'
            elif(hour > 14):
                mealzone = 'dinner'
                
        elif(isbf and islc):
            if(hour > 0 and hour < 8):
                mealzone = 'breakfast'
            elif(hour > 8):
                mealzone = 'lunch'
                
        elif(islc and isdr):
            if(hour > 0 and hour < 14):
                mealzone = 'lunch'
            elif(hour > 14):
                mealzone = 'dinner'
                
        elif(islc):
            mealzone = 'lunch'
            
        else:
            mealzone = 'None'
            
    if(usetime):
        if(mealzone != 'None'):        
            result = [mealzone] + data['menu'][0][f'{mealzone}']
        else:
            result = ['급식 정보가 존재하지 않습니다.']
        
    elif((data['menu'][0][mealzone]) != []):
        result = [mealzone] + data['menu'][0][f'{mealzone}']
        
    else:
        result = ['급식 정보가 존재하지 않습니다.']
            
    return result

def now(school_type, school_code, add_value, aleg, usetime, zonevalue = 'NoneValue'):
    
    API = meal_info(school_type, school_code, add_value[0], add_value[1], add_value[2], aleg)
    response = requests.get(API)                                                                

    return meal_zone(response, usetime, zonevalue)