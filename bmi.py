#now you can measure your bmi
w = float(input("weight in Kg:"))
h = float(input("height in m:"))
b = w / (h ** 2)
if b < 15:
   c = "very severely underweight" 
elif 15 <= b <= 16:
   c =  "severely underweight "  
elif 16 <= b <= 18.5:
   c = "underweight"
elif 18.5 <= b <= 25:
   c = "normal"
elif 25 < b <= 30:
   c = "overweight"
elif 30 <= b <= 35:
   c = " moderately obese"
elif 35 < b <= 40:
   c = " severely obese"
elif b > 40:
   c = "very severely obese"
print(" your bmi = " + str(b) + " you are " + c + ".")





















    