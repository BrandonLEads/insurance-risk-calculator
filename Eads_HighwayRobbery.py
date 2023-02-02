# main function to take user inputs
def main():
  # taking user name and age input
  name = input("Enter the name of the customer:")
  age = int(input("Enter the age of the customer:"))
  # checking if user lies under the valid category of age
  if age <16 or age >105: #if age <16 and >105 then invalid age
    print("Invalid Entry")
  else:
    # if age is valid then take further user inputs
    number_of_traffic_violations = int(input("Enter the number of traffic violations:"))
    # calculating risk code and risk Type on the basis of number of traffic tickets of user
    # using the calRisk() function
    riskCode,riskType = calRisk(name,age,number_of_traffic_violations)
    # calculating the insurance Price for each user by calling calinsurancePrice() function
    insurance_Price = calinsurancePrice(name,age,number_of_traffic_violations,riskCode,riskType)
    # displaying the final quote for the user
    display_qoute(name,riskType,insurance_Price)

# function to calculate the risk code and risk type for the user
def calRisk(name,age,number_of_traffic_violations):
  # conditional statements for risk code and risk type
  if number_of_traffic_violations >= 4:
    riskCode = 1
    riskType = 'high'
  elif number_of_traffic_violations == 3:
    riskCode = 2
    riskType = 'moderate'
  elif number_of_traffic_violations == 2:
    riskCode = 2
    riskType = 'moderate'
  elif number_of_traffic_violations == 1:
    riskCode = 3
    riskType = 'low'
  elif number_of_traffic_violations == 0:
    riskCode = 4
    riskType = 'no'
  # returning the riskCode and riskType to main function
  return riskCode , riskType
  
# function to calculate the insurance amount for the user according to number of tickets
def calinsurancePrice(name,age,number_of_traffic_tickets,riskCode,riskType):
  insurancePrice = 0 #variable declaration
  # conditional statements for calculating insurance price according to age
  # number of traffic tickets and risk code of the user
  if age < 25 and number_of_traffic_tickets >= 4 and riskCode == 1:
    insurancePrice = insurancePrice + 480
  elif age >= 25 and number_of_traffic_tickets >= 4 and  riskCode == 1:
    insurancePrice = insurancePrice + 410
  elif age < 25 and number_of_traffic_tickets == 3 and riskCode == 2:
    insurancePrice = insurancePrice + 450
  elif age >= 25 and number_of_traffic_tickets == 3 and riskCode == 2:
    insurancePrice = insurancePrice + 390
  elif age < 25 and number_of_traffic_tickets == 2 and riskCode == 2:
    insurancePrice = insurancePrice + 405
  elif age >= 25 and number_of_traffic_tickets == 2 and riskCode == 2:
    insurancePrice = insurancePrice + 365
  elif age < 25 and number_of_traffic_tickets == 1 and riskCode == 3:
    insurancePrice = insurancePrice + 380
  elif age >= 25 and number_of_traffic_tickets == 1 and riskCode == 3:
    insurancePrice = insurancePrice + 315
  elif age < 25 and number_of_traffic_tickets == 0 and riskCode == 4:
    insurancePrice = insurancePrice + 325
  elif age >= 25 and number_of_traffic_tickets == 0 and riskCode == 4:
    insurancePrice = insurancePrice + 275
# returning insurance amount to the main function
  return insurancePrice

#display output
def display_qoute(name, riskType, insurance_Price):
  # printing the quote for the user as mentioned in question
  print("{0},as a {1} risk driver, your insurance will be ${2:0.2f}".format(name,riskType,insurance_Price))
  
#call main function
main()