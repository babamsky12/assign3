print("The price of apple is 20 pesos")
print("The price of orange is 25 pesos")

ApplePrice = 20
OrangePrice = 25

def GetTotalBoughtApple():
    QuantityOfAppleFunc= int(input("How many apples would you like to purchase?: "))
    return QuantityOfAppleFunc

def GetTotalBoughtOrange():
    QuantityOfOrangeFunc= int(input("How many orange would you like to purchase?: "))
    return QuantityOfOrangeFunc


def GetTotalAmountOfPurchase(ApplePriceF, OrangePriceF, AppleAmount, OrangeAmount):
    AmountOfPurchaseFunc= (AppleAmount*ApplePriceF) + (OrangeAmount*OrangePriceF)
    return AmountOfPurchaseFunc

def DisplayOutput(AmountFunc):
    print(f"The total amount is {amount}.")


AppleBought =  GetTotalBoughtApple()
OrangeBought = GetTotalBoughtOrange()

amount = GetTotalAmountOfPurchase (ApplePrice, OrangePrice, AppleBought, OrangeBought)

DisplayOutput(amount)
