# Interest Rate Calculator.


principal = 200000      # initial amount PKR
interestRate = 12     # in percentage    
time = 10               # in years


totalAmount = principal * pow( (1 + interestRate / 100), time)
interest = totalAmount - principal

print(f"Total Amount: {totalAmount:.2f}")
print(f"Interest: {interest:.2f}") 
