import time
import matplotlib.pyplot as plt

print("Please enter your \"n\" value")
n = int(input())
delayBool = True  # Set this to False if you don't want the artificial delay

# For graphing
xValues = []  # This will now hold the iteration count
yValues = []  # This holds the calculated values of n

# We'll use a counter to simulate iterations 
counter = 0


while n != 1:
    xValues.append(counter)
    yValues.append(n)
    print(n)
    
    if (n % 2) == 0:
        n = n / 2
    else:
        n = (3 * n) + 1
    
    if delayBool:
        time.sleep(0.25)  #delay to see the numbers to show students
    
    counter += 1




plt.plot(xValues, yValues)

plt.show()