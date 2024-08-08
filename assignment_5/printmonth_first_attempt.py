start_month = eval(input("Enter the name of the month(January, ..., December):\n"))
start_date = eval(input("Enter the start date (1 for Monday, ... , 7 for Sunday):\n"))

for a in range(0-2, 31, 7):
        for b in range(number, number+7, 1):
                date = a + b 
                if len(str(a+b))< 2:
                        print(" " ,date, end=" ", sep="")
                else:
                        print(date, end=" ")
        print("")