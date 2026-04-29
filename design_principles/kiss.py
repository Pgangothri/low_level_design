class NumberUtils:
    @staticmethod
    def isEven(number):
        # Using unnecessary logic to determine evenness
        isEven = False

        if number % 2 == 0:
            isEven = True
        else:
            isEven = False

        return isEven


# Refactored version adhering to KISS principle


class NumberUtils:
    @staticmethod
    def isEven(number):
        return number % 2 == 0
