weigth=float(input("enter weight in kg"))
height=float(input("enter height in meter:"))

bmi=int(weigth)/float(height)**2
if bmi<18.5:
    print(f"your BMI is{bmi} and you are underweight.")
elif bmi<25:
    print(f"your BMI is{bmi} and you are normal weight.")
elif bmi<30:
    print(f"your BMI is{bmi} and you are overweight.")
elif bmi<35:
    print(f"your BMI is{bmi} and you are Obese.")
else:
    print(f"your BMI is{bmi} and you are clinically Obese.")

