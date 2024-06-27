def arm(n):
    string=str(n)
    no_ofdigits=len(string)
    digit_sum = sum(int(digit)**no_ofdigits for digit in string)
    return digit_sum
n=int(input("enter no"))
if arm(n):
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")