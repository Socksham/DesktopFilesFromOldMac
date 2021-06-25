num = 1
final = 0

while num < 1000:
    if(num % 3 == 0 or num % 5 == 0):
        final += num
    num += 1

print(final)