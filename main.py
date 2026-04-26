import sys
def temp_converter(temp1, unit1):
    if unit1 == "C":
        return (temp1 * 9/5) + 32, "Fahrenheit"
    else:
        return (temp1 - 32) * 5 / 9, "Celsius"

def format_temp(temp2):
    return int(temp2) if temp2.is_integer() else round(temp2, 2)


i = 0
while True:
    try:
        temp = float(input("What is the temperature?: "))
        break
    except ValueError:
        attempts = 4 - i
        if attempts > 1:
            print(f"Please try again. {attempts} attempts remaining")

        elif attempts == 1:
            print(f"Please try again. {attempts} attempt remaining")

        else:
            print("You have been banned! ")
            sys.exit()
        i += 1

for i in range(5):
    if i < 5:
        unit = input("What is the unit? (F/C): ").strip().upper()
        if unit in ["F", "C"]:
            break
        else:
            remaining = 4 - i

            if remaining != 0:
                print("PLEASE ENTER A VALID UNIT! ")
                print(f"{remaining} attempts remaining! ") if remaining != 1 else print(f"{remaining} "
                                                                                        f"attempt remaining!")
else:
    print("You have been banned! ")
    sys.exit()


converted_temp, target_unit = temp_converter(temp, unit)
formatted_temp = format_temp(converted_temp)

print(f"The temperature in {target_unit} is {formatted_temp}")

