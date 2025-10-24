a = float(input("Birinci sayı: "))
b = float(input("İkinci sayı: "))
islem = input("İşlem (+, -, *, /): ")

if islem == '+':
    print(a + b)
elif islem == '-':
    print(a - b)
elif islem == '*':
    print(a * b)
elif islem == '/':
    print(a / b)
else:
    print("Geçersiz işlem!")
