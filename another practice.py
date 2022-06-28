def get_expected_cost(beds, baths, has_basement):
    value = 80000+(beds*30000)+(baths*10000)+(40000*has_basement)
    return value
print(get_expected_cost(2, 1, True))

def cost_of_project(engraving, solid_gold):
    engraving = len(input("Enter the engraving you want: "))
    if solid_gold == True:
            
        cost = 100+(engraving*10) 
    else:
        cost = 50+(engraving*7)
    return cost

print(cost_of_project(3, True))