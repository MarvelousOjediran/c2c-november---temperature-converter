#Create a program that first asks the user which temperature scale they would like to convert from (e.g., Celsius, Fahrenheit, Kelvin). Then, ask which temperature scale they would like to convert to. Afterward, prompt the user for the temperature value and perform the conversion.


def scale_check(scale):
    temp_scale_check = scale.lower()
    if temp_scale_check == "celsius":
        print("Celsius selected")
    elif temp_scale_check == "fahrenheit":
        print("Fahrenheit selected.")
    elif temp_scale_check == "kelvin":
        print("Kelvin selected. ")
    else:
        print("not a valid option.")



def convert_check(scale, convert):
    temp_scale = scale; 
    temp_convert = convert; 


    if temp_scale == "celsius":
        if temp_convert == "celsius":
            print("Already in celsius.")
        elif temp_convert == "fahrenheit":
            print("Converting from celsius to fahrenheit.")
        elif temp_convert == "kelvin":
            print("Converting from celsius to kelvin.")


    if temp_scale == "fahrenheit": 
        if temp_convert == "fahrenheit":
            print("Already in fahrenheit.")
        elif temp_convert == "celsius":
            print("Converting from fahrenheit  to celsius.")
        elif temp_convert == "kelvin":
            print("Converting from fahrenheit to kelvin.")

    if temp_scale == "kelvin": 
       if temp_convert == "kelvin":
            print("Already in kelvin.")
    elif temp_convert == "celsius":
            print("Converting from kelvin  to celsius.")
    elif temp_convert == "fahrenheit":
            print("Converting from kelvin to fahrenheit.") 
#input variable to find out what temperate scale the user wants to use 
temp_scale = str(input("What temperature scale would you like to start off with? (Celsius, Fahrenheit, Kelvin) "))
scale_check(temp_scale)



temp_convert = str(input("What temperature would you like to convert to? (Celsius, Fahrenheit, Kelvin) "))
convert_check(temp_scale,temp_convert)
temp = int(input("What temperature is it? ")) 