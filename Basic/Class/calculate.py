class Credit:
    def __init__(self, amount, period, rate):
        self.amount = amount
        self.period = period
        self.rate   = rate
    
    def payment(self, type = "annuity" or "differentiated"):
        self.type = type
        if self.type == "annuity":
            amount      = self.amount   # сумма кредита
            period      = self.period   # количество месяцев
            rate        = self.rate     # процентная ставка
            coefficient = None          # коэффициент
            annuity     = None          # аннуитет

            coefficient = (rate / 100 / 12) * ((1 + rate / 100 / 12) ** period) / (((1 + rate / 100 / 12) ** period) - 1)
            annuity = amount * coefficient

            info1 = f"\nMonthly payment:  {round(annuity, 2)}\n"
            info2 = f"Overpayment:      {round(annuity * period - amount, 2)}\n"
            result = info1 + info2

            return result
        
        elif self.type == "differentiated":
            return self.amount / self.period + self.rate * (self.amount - (self.amount * (self.period - 1) / self.period))
