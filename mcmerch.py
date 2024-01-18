import sys

def parseArguments():
    arguments = {
        "price": int(sys.argv[1]),
        "quantity": 1,
        "province": "ON"
    }
    return arguments

def taxRate(province):
    tax = {
        "ON": 0.13
    }
    return tax[province]

def mcmerchCalculator():
    arguments = parseArguments()
    tax = taxRate(arguments['province'])
    print(arguments['price'] * arguments['quantity'] * tax + arguments['price'])

mcmerchCalculator()