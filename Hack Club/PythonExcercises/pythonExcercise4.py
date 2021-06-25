# Find the largest palindrome from the product of two 3-digit numbers

mult1 = 999
mult2 = 999

print(str(mult1)[:2])
print("hi")
palindromes = []


while len(palindromes) < 1:
    number = mult2 * mult1
    first_part = str(number)[:3]
    second_part = abs(number) % 1000

    
    mult1 -= 1

    if mult1 < 100:
        mult2 -= 1
        mult1 = 999
         
    