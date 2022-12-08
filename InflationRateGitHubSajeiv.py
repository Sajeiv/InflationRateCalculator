# Comp Sci 1026 Assignment 1 by Sajeiv

# The user is asked to input the year they are calculating inflation rate for and is stored in the currentYear variable
currentYear = input("Please enter the year that you want to calculate the personal interest rate for: ")

# The user is asked to input an integer for the amount of expense categories they would like to use
# This integer is stored into the expenditureCategoryNumber variable
expenditureCategoryNumber = int(input("Please enter the amount of expenditure categories: "))

# Before user is asked to input their expenses, previous and current year expenses are defaulted to 0.0 float values
previousYearExpense = 0.0
currentYearExpense = 0.0

# A while loop is used to prompt the user to input two float value for past AND current year expenses respectively
# The number of times the user is prompted to enter these two inputs is equal to expenditureCategoryNumber
loopIteration = 0
while loopIteration != expenditureCategoryNumber:
    x = float(input("Please enter expenses for previous year: "))
    y = float(input("Please enter expenses for year of interest: "))
    previousYearExpense = previousYearExpense + x
    currentYearExpense = currentYearExpense + y
    loopIteration = loopIteration + 1
# Each time the user is prompted and inputs the previous AND current expenses, loopIterations is added by 1
# The while loop will stop asking the user for current and past year expenses
# when the loop iterations reaches the number of expense categories or expenditureCategoryNumber

# We now have all the data needed to calculate the Inflation Rate

# The InflationRate variable is set equal to the float value calculated using the inflation rate formula and user inputs
inflationRate = ((currentYearExpense - previousYearExpense)/currentYearExpense)*100

# if-else statements are used to categorize the output inflation rate into either low, moderate, high, or hyper
# If calculated inflation rate is less than 3.0, it is categorized as "Low"
if inflationRate < 3.0:
    inflationType = "Low"

# If calculated inflation rate is greater than or equal to 3.0 but less than 5.0, it is categorized as "Moderate"
elif 3.0 <= inflationRate < 5.0:
    inflationType = "Moderate"

# If calculated inflation rate is greater than or equal to 5.0 but less than 10.0, it is categorized as "High"
elif 5.0 <= inflationRate < 10.0:
    inflationType = "High"

# If calculated inflation rate does not fall within any of the previous ranges, it is categorized as "Hyper"
else:
    inflationType = "Hyper"

# The round() function was used to round inflation rate output to 1 decimal place
inflationRate1dp = round(inflationRate, 1)

# A print function is used to inform the user of their inflation rate rounded to 1 decimal place for the year
# Another function is used to inform the type of inflation rate the user has
print("Personal inflation rate for " + currentYear + " is " + str(inflationRate1dp) + "%")
print("Type of Inflation: " + inflationType)
