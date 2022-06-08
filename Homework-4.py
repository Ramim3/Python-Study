a=int(input())
b=int(input())
c=int(input())

print(a and b and c and "Нет нулевых значений!!!")
print(a or b or c or "Введены все нули!")

if a > b+c:
    print("a-b-c")
elif a < b+c:
    print("b+c-a")
if a > 50 and b>a and c>a:
    print("Вася")
if a>5 or b==7 and c==7:
    print("Петя")



