import datetime as dt

class Record:
    def __init__(self, amount, comment, date='today'):
        self.amount = amount
        self.comment = comment
        self.date_format = '%d.%m.%Y'
        if date == 'today':
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(str(date), self.date_format).date()

    def __str__(self):
        return self.amount


class Calculator:

    today = dt.datetime.now().date()
    delta = dt.timedelta(days=7)

    def __init__(self, limit):
        self.limit=limit
        self.records=[]

    def add_record(self, new_record):
        return self.records.append(new_record)
        
    
    def get_today_stats(self):
        today_stats = 0
        for i in self.records:
            if i.date == self.today:
                today_stats += i.amount
        return today_stats
        
    def get_week_stats(self):
        week_stats = 0
        date_today = dt.date.today()
        delta = dt.timedelta(days=7)
        start_date = date_today - delta
        for record in self.records:
            if start_date < record.date <= date_today:
                week_stats += record.amount
                return week_stats



class CashCalculator(Calculator):
    
    USD_RATE = 60.00
    EURO_RATE = 70.00

    def get_today_cash_remained(self, currency):
        remainder= self.limit-self.get_today_stats()
        if remainder > 0:
            if currency == 'usd':
                return f'На сегодня осталось {round(remainder/self.USD_RATE, 2)} {currency}'
            elif currency == 'eur':
                return f'На сегодня осталось {round(remainder/self.EURO_RATE, 2)} {currency}'
            elif currency == 'rub':
                return f'На сегодня осталось {round(remainder)} {currency}'
        elif remainder == 0:
            return f'Денег нет, держись'
        elif remainder < 0:
            if currency == 'usd':
                return f'Денег нет, держись: твой долг - {abs(round(remainder/self.USD_RATE, 2))} {currency}'
            elif currency == 'eur':
                return f'Денег нет, держись: твой долг - {abs(round(remainder/self.EURO_RATE, 2))} {currency}'
            elif currency == 'rub':
                return f'Денег нет, держись: твой долг - {abs(remainder)} {currency}'


        


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        limit_calories = self.limit - self.get_today_stats()
        message1 = (f'Сегодня можно съесть что-нибудь ещё, но с общей '
                       f'калорийностью не более {limit_calories} кКал')
        message2 = 'Хватит есть!'
        if limit_calories > 0:
            return message1
        else:
            return message2
    


r1 = Record(amount=145, comment="Безудержный шопинг", date="08.03.2020")
r2 = Record(amount=1568, comment="Наполнение потребительской корзины", date="09.03.2020")
r3 = Record(amount=691, comment="Катание на такси", date="08.03.2020")
r4 = Record(amount=1186, comment="Кусок тортика. И ещё один.", date="24.02.2020")
r5 = Record(amount=84, comment="Йогурт.", date="23.02.2020")
r6 = Record(amount=1140, comment="Баночка чипсов.", date="24.02.2020")

calo_calculator=CaloriesCalculator(3000)
calo_calculator.add_record(r4)
print(calo_calculator.get_calories_remained())

cash=CashCalculator(1000)
cash.add_record(r3)
print(cash.get_today_cash_remained("rub"))





    



