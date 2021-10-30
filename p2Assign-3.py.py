def GetAvailableMoney():
    AvailableMoneyFunc = int(input("How much is your money?: "))
    return AvailableMoneyFunc

def GetQuantityOfAppleYouWant():
    QuantityOfAppleYouWantFunc= int(input("How much is the apple: "))
    return QuantityOfAppleYouWantFunc

def GetQuantityYouCanBuy(TotalAmountOfMoneyYouCanSpendF, TotalQuantityOfAppleYouWantToPurchaseF):
    GetQuantityYouCanBuyFunc= (TotalAmountOfMoneyYouCanSpendF) // (TotalQuantityOfAppleYouWantToPurchaseF)
    return GetQuantityYouCanBuyFunc


def GetTotalChange(TotalAmountOfMoneyYouCanSpendF, TotalQuantityOfAppleYouWantToPurchaseF):
    GetTotalChangeFunc= float(TotalAmountOfMoneyYouCanSpendF) % (TotalQuantityOfAppleYouWantToPurchaseF)
    return GetTotalChangeFunc

def DisplayOutput(GetQuantityYouCanBuyF, GetTotalChangeF):
    print(f"You can buy {YouCanBuy} apples and your change is {YourChangeIs}")



TotalAmountOfMoneyYouCanSpend = GetAvailableMoney()
TotalQuantityOfAppleYouWantToPurchase = GetQuantityOfAppleYouWant()


YouCanBuy = GetQuantityYouCanBuy(TotalAmountOfMoneyYouCanSpend, TotalQuantityOfAppleYouWantToPurchase)
YourChangeIs = GetTotalChange(TotalAmountOfMoneyYouCanSpend, TotalQuantityOfAppleYouWantToPurchase)


DisplayOutput(YouCanBuy, YourChangeIs)