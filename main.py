import johnson as meal

# 학교타입 >> [초등] elementary | [중등] : middle | [고등] : high
# 학교코드 >> [검색] https://schoolmenukr.ml/code/app
# 알레르기 정보 >> [표시] : True | [숨기기] : False
# 급식 시간대 >> [조식] : breakfast | [중식] : lunch | [석식] : dinner

date = [0, 0, 0]                                                                # 날짜추가 : 현재 날짜에서 추가 할 [년, 월, 일]
result = meal.now('high', 'N100000164', date, False, True)                      # meal.now(학교코드, 학교코드, 날짜추가, 알레르기 정보 표시, 자동 가져오기, 급식 시간대)

for value in result:
    print(value)