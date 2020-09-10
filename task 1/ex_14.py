# 1 feet = 12 inches (')
# 1 inch = 2.54 centimeters ('')

feet = int(input('Feet: '))
inches = int(input('Inches: '))

print('{0}\' {1}\'\' --> {2} cm'.format(feet, inches, ((feet * 12 + inches) * 2.54)))
