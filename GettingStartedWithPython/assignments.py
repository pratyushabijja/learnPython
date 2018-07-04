print('HelloWorld!')

# getting input from the user
name = input('Who are you?')
print('Welcome', name)

# Calculate the pay

hrs = 10
rate = 2.4
pay = float(hrs) * float(rate)
print("Pay:", pay)

# if-else condition

hrs = 10
h = 45
rate = 2.5
r = float(rate)
if h <= 40:
    pay = r * h
else:
    pay = (40 * r) + ((h - 40) * r * 1.5)
print(pay)

# if elif condition

s = 0.85
score = float(s)
if (score >= 0.9) and (score <= 1):
    print("A")
elif (score >= 0.8) and (score < 0.9):
    print("B")
elif (score >= 0.7) and (score < 0.8):
    print("C")
elif (score >= 0.6) and (score < 0.7):
    print("D")
elif (score < 0.6) and (score > 0):
    print("F")
else:
    print("Error")


# defining functions

def computepay(h, r):
    if h >= 40:
        return (40 * r) + (h - 40) * r * 1.5
    else:
        return h * r

hrs = 45
rate = 10.50
h = float(hrs)
r = float(rate)
p = computepay(h, r)
print(p)

# looping and try except block

largest = 0
smallest = 0
while True:
    number = input("Enter a number:")
    if number == 'done':
        break
    try:
        n = int(number)
    except:
        print("Invalid input")
        continue
    if n > largest:
        largest = n

    if smallest == 0:
        smallest = n
    elif n < smallest:
        smallest = n

print("Maximum is", largest)
print("Minimum is", smallest)
