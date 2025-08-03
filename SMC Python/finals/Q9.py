def swapInitals(first_name, last_name):
    updated_first_name = last_name[0] + first_name[1:]
    updated_last_name = first_name[0] + last_name[1:]
    return f"{updated_first_name} {updated_last_name}"


print(swapInitals("Patti", "Koenig"))
print(swapInitals("John", "Doe"))
print(swapInitals("Cat", "Dog")) 