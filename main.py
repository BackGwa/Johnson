import johnson as meal

# 학교타입 >> [초등] elementary | [중등] : middle | [고등] : high
# 학교코드 >> [검색] https://schoolmenukr.ml/code/app
result = meal.now('high', 'N100000164')

for value in result:
    print(value)