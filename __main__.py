#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import johnson as meal

# 학교타입 >> [초등] elementary | [중등] : middle | [고등] : high
# 학교코드 >> [검색] https://schoolmenukr.ml/code/app
# 날짜 >> [년, 월, 일]의 급식 정보
# 알레르기 정보 >> [표시] : True | [숨기기] : False
# 자동_가져오기 >> [활성화] : True | [비활성화] : False
# 급식 시간대 >> [조식] : breakfast | [중식] : lunch | [석식] : dinner

def main():
    try:
        result = meal.get('high', 'N100000164')     # meal.get(학교타입, 학교코드, 날짜, 알레르기_정보_표시, 자동_가져오기, 급식_시간대)

        for value in result:
            print(value)        
        return 0
    
    except:
        return -1

if __name__ == '__main__':
    main()