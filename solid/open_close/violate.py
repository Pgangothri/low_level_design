class InvoiceProcessor:
    def calculateTotal(self, region, amount):
        if region.lower() == "india":
            return amount + amount * 0.18
        elif region.lower() == "us":
            return amount + amount * 0.08
        elif region.lower() == "uk":
            return amount + amount * 0.12
        else:
            return amount  # No tax for unknown region
