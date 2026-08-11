class RomanConverter:
    def int_to_roman(self, number):
    
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        numerals = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        result = ""
        i = 0

        while number > 0:
            while number >= values[i]:
                result += numerals[i]
                number -= values[i]
            i += 1

        return result

num = int(input("Enter an integer: "))
converter = RomanConverter()
print("Roman numeral:", converter.int_to_roman(num))
