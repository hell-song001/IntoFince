from datetime import datetime
#
#
#  Bond valuation formulas

class BondObject:
    face_value = 99   
    def __init__(self, issuer, coupon, term, maturity):
        self.bond_name = issuer
        self.coupon_rate = ( coupon / 100 )
        self.interest = self.coupon_rate * self.face_value
        self.maturity_period = term
        self.maturity_date = datetime.strptime(maturity, "%dth %B %Y")

    def __str__(self):
        return "{}: {} ({}, {})".format(self.bond_name, self.maturity_date, self.present_value(), self.required_return(100))
    
    def present_value(self):
        value = 0

        for x in range(self.maturity_period):
            value += (self.interest + ( (1 + self.coupon_rate) ** (x + 1)))
        value += (self.face_value + ((1 + self.coupon_rate) ** self.maturity_period))

        return value
    
    def required_return(self, market_value = 100):
        a = (self.face_value - market_value) / self.maturity_period
        b = (self.face_value + market_value) / 2

        return ((self.interest + a) / b)


bond1 = BondObject("NMB", 8.5, 3, "28th March 2025")
print(bond1)