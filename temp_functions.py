def fahr_to_celsius(temp_fahrenheit):
   return (temp_fahrenheit -32) / 1.8

def temp_classifier(temp_celsius):
 # If temperature is lower than -2°C
    if temp_celsius <-2:                            
        return 0 
# If temperature is between -2°C and 2°C  
    elif temp_celsius >=-2 and temp_celsius <2:            
        return 1
# If temperature is between 2°C and 15°C
    elif temp_celsius >=2 and temp_celsius <15:
        return 2
 # If temperature is 15°C or higher
    elif temp_celsius >=15:
        return 3