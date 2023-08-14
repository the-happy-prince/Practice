intro = "Hey, my name is {} and I am from {}"

name = "Prince"
country = "India"
print(intro.format(name, country)) # if the sequence of the args is correct, the intro will give the correct output
print(intro.format(country, name)) # but for this, the output will be incorrect

# To avoid this situation, let's modify the intro

intro2 = "Hey, my name is {1} and I am from {0}"
print(intro2.format(country, name)) # but this is bewildering

# So, let's use f-string

print(f"Hey, my name is {name} and I am from {country}")

# Formating float
price = 100.289
print(f"The price of this product is {price: .2f}")

# If you want to display the curly braces in your string
print(f"The price of this product is {{price: .2f}}")