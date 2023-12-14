money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
survival_months = 0

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while spend < (money_capital + salary):
    survival_months += 1
    money_capital -= spend - salary
    spend += spend * increase


print("Количество месяцев, которое можно протянуть без долгов:", survival_months)
