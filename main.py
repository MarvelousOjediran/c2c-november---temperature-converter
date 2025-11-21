def converting_temp(c2f, c2k, f2c, f2k, k2c, k2f, scale, convert):
    temp_scale = scale
    temp_convert = convert
    
    if scale == "celsius":
        if convert == "fahrenheit":
            print(f"{temp}° Celsius is {c2f:.2f}° Fahrenheit")
        elif convert == "kelvin":
            print(f"{temp}° Celsius is {c2k:.2f} Kelvin")
    elif scale == "fahrenheit":
        if convert == "celsius":
            print(f"{temp}° Fahrenheit is {f2c:.2f}° Celsius")
        elif convert == "kelvin":
            print(f"{temp}° Fahrenheit is {f2k:.2f} Kelvin")
    elif scale == "kelvin":
        if convert == "celsius":
            print(f"{temp} Kelvin is {k2c:.2f}° Celsius")
        elif convert == "fahrenheit":
            print(f"{temp} Kelvin is {k2f:.2f}° Fahrenheit")

def scale_check(scale):
    temp_scale_check = scale.lower()
    if temp_scale_check == "celsius":
        print("Celsius selected")
    elif temp_scale_check == "fahrenheit":
        print("Fahrenheit selected.")
    elif temp_scale_check == "kelvin":
        print("Kelvin selected.")
    else:
        print("Not a valid option.")

def convert_check(scale, convert):
    temp_scale = scale
    temp_convert = convert

    if temp_scale == "celsius":
        if temp_convert == "celsius":
            print("Already in celsius.")
        elif temp_convert == "fahrenheit":
            print("Converting from celsius to fahrenheit.")
        elif temp_convert == "kelvin":
            print("Converting from celsius to kelvin.")
    elif temp_scale == "fahrenheit": 
        if temp_convert == "fahrenheit":
            print("Already in fahrenheit.")
        elif temp_convert == "celsius":
            print("Converting from fahrenheit to celsius.")
        elif temp_convert == "kelvin":
            print("Converting from fahrenheit to kelvin.")
    elif temp_scale == "kelvin": 
        if temp_convert == "kelvin":
            print("Already in kelvin.")
        elif temp_convert == "celsius":
            print("Converting from kelvin to celsius.")
        elif temp_convert == "fahrenheit":
            print("Converting from kelvin to fahrenheit.")

# Input variable to find out what temperature scale the user wants to use 
temp_scale = str(input("What temperature scale would you like to start off with? (Celsius, Fahrenheit, Kelvin) ")).lower()
scale_check(temp_scale)

temp_convert = str(input("What temperature would you like to convert to? (Celsius, Fahrenheit, Kelvin) ")).lower()
convert_check(temp_scale, temp_convert)

temp = float(input("What temperature is it? "))  

# Calculate all conversions
cel_to_fah = ((temp * 1.8) + 32) 
cel_to_kel = (temp + 273.15) 

fah_to_cel = (temp - 32) * 5/9
fah_to_kel = ((temp - 32) * 5/9) + 273.15

kel_to_ces = (temp - 273.15)
kel_to_fah = ((temp - 273.15) * 9/5) + 32

# Call the conversion function with all the calculated values
converting_temp(cel_to_fah, cel_to_kel, fah_to_cel, fah_to_kel, kel_to_ces, kel_to_fah, temp_scale, temp_convert)