costMeal = float(input('The cost of a meal: '))

tax = costMeal * 0.12
tip = costMeal * 0.18

print('The tax amount:', round(tax, 2),
      '$\nThe tip amount:', round(tip, 2),
      '$\nThe grand total for the meal:', round(costMeal, 2) + round(tax, 2) + round(tip, 2), '$')
