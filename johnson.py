from datetime import datetime
import requests
import json

today = datetime.today()

def meal_info(school_type, school_code, add_year, add_month, add_date):     # 날짜에 맞는 급식 정보 가져오기
    year = today.year + add_year
    month = today.month + add_month
    day = today.day + add_date
    allergy = 'hidden'                                                      # 알레르기 정보 >> [숨기기] : hidden | [표시] : formed

    result = f'https://schoolmenukr.ml/api/{school_type}/{school_code}?year={year}&month={month}&date={day}&allergy={allergy}'
    
    return result

def meal_zone(JSON, usetime, meal_value):                                   # 시간에 맞는 급식 정보 반환
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

def now(school_type, school_code):                                     # 학교타입 >> [초등] elementary | [중등] : middle | [고등] : high // 학교코드 >> [검색] https://schoolmenukr.ml/code/app
    API = meal_info(school_type, school_code, 0, 0, 0)                      # 오늘 급식 정보 가져오기
    response = requests.get(API)                                            # 값 가져오기

    return meal_zone(response, True, 'ZoneUse')