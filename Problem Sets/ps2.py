def new_balance(unpayedBalance, monthlyInterestRate):
  """
  Computes new monthly balance for a CC bill given the previous outstanding balance (unpayedBalace) and the monthly interest rate (monthlyInterestRate), in decimal form. The returned value is rounded to the nearest cent.
  """
  return round(unpayedBalance + (monthlyInterestRate * unpayedBalance), 2)

def get_monthly_interest_rate(annualInterestRate):
  """
  Computes the monthly interest rate, in decimal form, from the decimal version of the annual interest rate.
  """
  return annualInterestRate / 12.0

def get_min_monthly_payment(balance, monthlyPaymentRate):
  """
  Computes the minimum monthly payment using the current balance and the monthlyPaymentRate,as a decimal. The returned value is rounded to the nearest cent.
  """
  return round(balance * monthlyPaymentRate, 2)

def min_cc_bill_for_a_year(balance,annualInterestRate,monthlyPaymentRate):
  """
  Prints out the month, the monthly minimum payment, the current unpayed balance for a credit card account over a year, assuming only paying the minimum payment. Balance is the outstanding balance on the card, annualInterestRate is the annual interest rate as a decimal, and monthlyPaymentRate is the monthly minimum payment rate as a decimal.
  """
  monthlyInterestRate = get_monthly_interest_rate(annualInterestRate)
  totalPayed = 0
  for month in range(1,13):
    minMonthlyPayment = get_min_monthly_payment(balance, monthlyPaymentRate)
    totalPayed += minMonthlyPayment
    unpayedBalance = round(balance - minMonthlyPayment, 2)
    balance = new_balance(unpayedBalance, monthlyInterestRate)
    print "Month: " + str(month)
    print "Minimum monthly payment: " + str(minMonthlyPayment)
    print "Remaining balance: " + str(balance)

  print "Total paid: " + str(totalPayed)
  print "Remaining balance: " + str(balance)

def cc_balance_after_a_year(balance, monthlyInterestRate, constantPayment):
  """
  Returns the remaining balance on a CC after a year of constant payments.
  """
  totalPayed = 0
  for month in range(1,13):
    unpayedBalance = round(balance - constantPayment, 2)
    balance = new_balance(unpayedBalance, monthlyInterestRate)

  return balance

def find_fixed_min_payment_dumb(balance, annualInterestRate):
  """
  Finds the minimum fixed monthly payment to totally pay off a CC balance in 12 months, to the nearest $10.
  """
  possibleMonthlyPayments = range(0, balance+10, 10)
  length = len(possibleMonthlyPayments)
  lowIndex = 0
  highIndex = length
  midIndex = length/2
  amountFound = False
  amount = 0

  monthlyInterestRate = get_monthly_interest_rate(annualInterestRate)

  while(not amountFound):
    end_of_year_balance = cc_balance_after_a_year(balance, monthlyInterestRate, possibleMonthlyPayments[midIndex])
    if (end_of_year_balance < 0) and (cc_balance_after_a_year(balance, monthlyInterestRate, possibleMonthlyPayments[midIndex-1])>0): #paying next lowest increment won't pay off in time
      amount = possibleMonthlyPayments[midIndex]
      break

    if end_of_year_balance > 0: #need to increase monthly payment
      lowIndex = midIndex
      midIndex = int(0.5*(lowIndex + highIndex))
    elif (end_of_year_balance < 0): #paying more per month than is needed, possibly
      highIndex = midIndex
      midIndex = int(0.5*(lowIndex + highIndex))
    else:
      amountFound = True

  return possibleMonthlyPayments[midIndex]

def average_and_round(num1, num2):
  """
  Averages two floats and rounds to the nearest $0.01
  """
  return round(0.5*(num1 + num2), 2)

def find_fixed_min_payment(balance, annualInterestRate):
  """
  Finds the minimum fixed monthly payment to totally pay off a CC balance in 12 months to the nearest $0.01.
  """
  monthlyInterestRate = get_monthly_interest_rate(annualInterestRate)
  low = balance/12.
  high = (balance * (1 + monthlyInterestRate)**12)/12.0
  mid = average_and_round(low,high)
  amountFound = False


  while(not amountFound):
    end_of_year_balance = cc_balance_after_a_year(balance, monthlyInterestRate, mid)
    if (end_of_year_balance < 0) and (cc_balance_after_a_year(balance, monthlyInterestRate, mid - 0.01)>0): #paying next lowest increment won't pay off in time
      break

    if end_of_year_balance > 0: #need to increase monthly payment
      low = mid
      mid = average_and_round(low,high)
    elif (end_of_year_balance < 0): #paying more per month than is needed, possibly
      high = mid
      mid = average_and_round(low,high)
    else:
      amountFound = True

  return mid

#balance = 999999
#annualInterestRate = 0.18

#min_cc_bill_for_a_year(balance, annualInterestRate, monthlyPaymentRate)
payment = find_fixed_min_payment(balance, annualInterestRate)
print "Lowest Payment: " + str(payment)
