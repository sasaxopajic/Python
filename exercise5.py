money = int(input("Money: "))

bitcoin = int(input("Bitcoin price: "))
ethereum = int(input("Ethereum price: "))
litecoin = int(input("Litecoin price: "))

b = int(money/bitcoin)
e = int(money/ethereum)
l = int(money/litecoin)

print("With", money, "$ you can buy", b, "bitcoins,", e, "ethereum and", l, "litecoins.")