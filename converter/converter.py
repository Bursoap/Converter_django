import re


class Convert(object):

    def __init__(self, number):
        self.number = number
        self.associative = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
            "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900
        }

    def convert(self):
        if self.number.isdigit():
            return self.arab_to_rome()
        else:
            return self.rome_to_arab()

    def rome_to_arab(self):
        string = ''.join(self.number.split())
        result = 0
        for i in range(len(string)):
            try:
                    if self.associative[string[i]] < self.associative[string[i+1]]:
                        result -= self.associative[string[i]]
                    else:
                        result += self.associative[string[i]]
            except IndexError:
                result += self.associative[string[i]]
        return result

    def arab_to_rome(self):
        count = int(self.number)
        result = ""
        for rome_key, arab_value in sorted(self.associative.items(), key=lambda x: x[1], reverse=True):
            while count >= arab_value:
                result += rome_key
                count -= arab_value
        return result
