def month_to_season(month):
    if 3 <= month <= 5:
        return "весна"
    elif 6 <= month <= 8:
        return "лето"
    elif 9 <= month <= 11:
        return "осень"
    elif month in [12,1,2]:
        return "зима"
    else:
        return "Неверный номер месяца"

try:
    month = int(input("Введите номер месяца (1-12): "))
    print(month_to_season(month)) 
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")