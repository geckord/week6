def average(total):
    return float(total / 4)


summation = 0
for i in range(0, 4):
    summation += int(input("Enter a mark: "))

if 0.0 <= average(summation) <= 100.0:
    if average(summation) < 60.0:
        print("Fail")
    elif average(summation) >= 60.0:
        print("Pass")
else:
    print("Invalid mark(s) seem(s) to has/have been entered. Please try again.")
