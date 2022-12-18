# Counting

List = [3028, 45, 34, 34, 755, 49, 1.2]
Smallest = None  # As if We said Smallest = List[0]
for value in List:
    if Smallest is None:  # Here only for the 1st loop
        Smallest = value
    elif value < Smallest:
        Smallest = value
    else:
        pass
print(Smallest)
