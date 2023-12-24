def calculate_bmi(weight, height):
    # Formula to calculate BMI: weight (kg) / (height (m) ^ 2)
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    weight = float(input(" Please Enter your weight in kilograms: "))
    height = float(input("Please Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    interpretation = interpret_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are categorized as: {interpretation}")

if __name__ == "__main__":
    main()
