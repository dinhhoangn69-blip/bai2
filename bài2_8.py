print("Sinh vien: Nguyen Dinh Hoang")
print("Ma so SV : 245752021610043")
print("###########################")
#################################
a, b = 1, 2
total = 0

print("Fibonacci sequence (less than 4,000,000):")
while a < 4000000:
    print(a, end=" ")
    if a % 2 == 0:
        total += a
    a, b = b, a + b

print("\nSum of even numbers in Fibonacci series:", total)
