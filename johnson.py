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
    
    if(usetime):
        hour = today.hour

        if(hour < 7):
            mealzone = 'breakfast'
        elif(hour > 7 and hour < 14):
            mealzone = 'lunch'
        elif(hour > 14 and hour > 23):
            mealzone = 'dinner'
            
    data = json.loads(JSON.text)
    return data['menu'][0][f'{mealzone}']   

def now(school_type, school_code, add_value, aleg, usetime, zonevalue = 'NoneValue'):
    
    API = meal_info(school_type, school_code, add_value[0], add_value[1], add_value[2], aleg)
    response = requests.get(API)                                                                

    return meal_zone(response, usetime, zonevalue)