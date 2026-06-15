class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        Fahrenheit = celsius * 1.80 + 32.00
        kelvin = celsius + 273.15
        return(kelvin,Fahrenheit)
#Celsius = float(input("Enter a number: "))
#Fahrenheit = Celsius * 1.80 + 32.00
#kelvin = Celsius + 273.15
#print(Fahrenheit,kelvin)
