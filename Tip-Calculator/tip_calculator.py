print(" Welcome to tip calculator")
amount= float(input("Enter the Bill amount:"))
tip_percentage= float(input("Enter the tip percentage you want to give:"))
tip_amount = amount*tip_percentage/100
total_bill = amount + tip_amount
print (f"The bill after tipping {tip_percentage} % of the amount would be {total_bill:.2f}")
while True:
            bill_split = input(" Do you want to split the bill? YES/NO ").lower()
            if bill_split == "yes" or bill_split == "no":
                  break
            else: 
                  print(" Enter YES or NO and try again")
while True:
      try:
            if bill_split == "yes" :
                  no_of_people= int(input("Enter the number of people you would like to split with:"))
                  per_person_amount= total_bill/ no_of_people
                  print(f"Each person would pay {per_person_amount:.2f}")
                  break

            elif bill_split == "no":
                  print(f"The total amount to be paid {total_bill:.2f}")
                  break
      except ZeroDivisionError:
            print("You have entered 0 person to split with, try again!")
      except ValueError:
            print("Enter a valid number (e.g. 1, 4, 5).")
      

print ("Thank you for using, Hope you have a great day :)")