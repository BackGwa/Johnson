from datetime import datetime
import requests
import json


school_type = 'high'                            # 학교종류 >> [초등] elementary | [중등] : middle | [고등] : high
school_code = 'N100000164'                      # 학교코드 >> [검색] https://schoolmenukr.ml/code/app
today = datetime.today()


def meal_info(add_year, add_month, add_date):   # 날짜에 맞는 급식 정보 가져오기
    year = today.year + add_year
    month = today.month + add_month
    day = today.day + add_date
    allergy = 'hidden'                          # 알레르기 정보 >> [숨기기] : hidden | [표시] : formed

    result = f'https://schoolmenukr.ml/api/{school_type}/{school_code}?year={year}&month={month}&date={day}&allergy={allergy}'
    
    return result


def meal_zone(JSON, usetime, meal_value):       # 시간에 맞는 급식 정보 반환
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


API = meal_info(0, 0, 0)                        # 오늘 급식 정보 가져오기
response = requests.get(API)                    # API로부터 값 가져오기

result = meal_zone(response, True, 'ZoneUse')

for value in result:                            # 일단 급식 정보 출력
    print(value)