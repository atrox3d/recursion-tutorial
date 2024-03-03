total = 5

ingredients = 3
portions = [0 for i in range(ingredients)]

current = 0
left = total
for spoons in range(total+1):
    if (left:=left-1): 
        portions[current] += 1

print(portions) 