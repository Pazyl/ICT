loaves = int(input("Enter the number of loaves: "))

regPrice = 3.49 * loaves
discount = 0.6 * regPrice
finalPrice = regPrice - discount

print("Regular price: $%5.2f\n"
      "Discount: $%5.2f\n"
      "Final price: $%5.2f" % (regPrice, discount, finalPrice))
