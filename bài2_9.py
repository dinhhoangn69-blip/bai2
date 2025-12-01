print("Sinh vien: Nguyen Dinh Hoang")
print("Ma so SV : 245752021610043")
print("###########################")
#################################
s = input("Enter a string: ")
d = {}

for ch in s:
    d[ch] = s.count(ch)

print(d)
