#2. Палиндром строки

x = input().replace(" ","")
if str(x) == str(x)[::-1] :
    print("true")
else:
    print("false")