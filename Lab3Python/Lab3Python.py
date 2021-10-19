term = 1
m = float(input("Введіть m: "))
x = float(input("Введіть х: "))
e = float(input("Введіть точність: "))
n = 1.0
s = 0.0
while abs(term) >=e:
    s+= term
    term = term * x * (m+1-n)
    n+= 1
    print(n, "Проміжне значення функції:", term , "Сума:" ,s)
