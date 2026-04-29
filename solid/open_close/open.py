from abc import ABC, abstractmethod


# Tax strategy Interface
class TaxCalculator(ABC):
    @abstractmethod
    def calculateTax(self, amount):
        pass


# Implementing Region-Specific Tax Calculators
class IndiaTaxCalculator(TaxCalculator):
    def calculateTax(self, amount):
        return amount * 0.18  # GST


class USTaxCalculator(TaxCalculator):
    def calculateTax(self, amount):
        return amount * 0.08  # Sales Tax


class UKTaxCalculator(TaxCalculator):
    def calculateTax(self, amount):
        return amount * 0.12  # VAT


# Invoice class
class Invoice:
    def __init__(self, amount, taxCalculator):
        self.amount = amount
        self.taxCalculator = taxCalculator

    def getTotalAmount(self):
        return self.amount + self.taxCalculator.calculateTax(self.amount)


# Example usage
amount = 1000.0

india_invoice = Invoice(amount, IndiaTaxCalculator())
print(f"Total (India): ₹{india_invoice.getTotalAmount()}")

us_invoice = Invoice(amount, USTaxCalculator())
print(f"Total (US): ${us_invoice.getTotalAmount()}")

uk_invoice = Invoice(amount, UKTaxCalculator())
print(f"Total (UK): £{uk_invoice.getTotalAmount()}")
