class Investment:
    def __init__(self):
        self.monthly_investment = 0
        self.yearly_interest_rate = 0
        self.years = 0

    def calculate_future_value(self):
        monthly_interest_rate = self.yearly_interest_rate / 12 / 100
        months = self.years * 12

        future_value = 0
        for i in range(months):
            future_value += self.monthly_investment
            monthly_interest_amount = future_value * monthly_interest_rate
            future_value += monthly_interest_amount

        return future_value
