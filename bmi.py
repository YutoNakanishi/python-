#BMI判定プログラム
wight = float(input("体重(kg)は？"))
height = float(input("身長(cm)は？"))
#BMIの計算
height = height / 100
bmi = wight / (height * height)

#BMIの値に応じて結果を分岐
result = ""
if bmi < 18.5:
    result = "ヤセ型"
#if(18.5 <= bmi) and (bmi < 25):
if(18.5 <= bmi < 25):
    result = "標準"
if 25 <= bmi:
    result = "でぶ"

#結果を表示
print("BMI :",bmi)
print("判定 :",result)
