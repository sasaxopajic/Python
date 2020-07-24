bitcoin = int(input("Bitcoin value: "))
increase = int(input("Bitcoin increase percentage: "))

total = bitcoin + (bitcoin*increase)/100
increase_value = total - bitcoin

print("Total bitcoin value: ", total)
print("Increase value: ", increase_value)

