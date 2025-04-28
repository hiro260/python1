fruits_colors =  {'apple': 'red', 'peach': 'pink', 'grapes': 'blue', 'banana': 'yellow'}

fruits_colors['kiwii'] = 'gold'

# for fruit in fruits_colors.keys():
#     print(fruit)

# print("\n")

# for color in fruits_colors.values():
#     print(color)

# print("\n")

# for x in fruits_colors:
#     print(x)

# for fruit, color in fruits_colors.items():
#     print(f"color of {fruit} is {color}.")

fruits_colors =  {'apple': 'red', 'peach': 'pink', 'grapes': 'blue', 'banana': 'yellow'}

fruits_colors['kiwii'] = 'gold'

print(fruits_colors.get('piapple', 'Nothing'))

fruits_colors2 =  {'pinapple': 'yellow', 'mango': 'green', 'banana': 'yellow'}

fruits_colors.update(fruits_colors2 )

print(fruits_colors)