lst_a = [1, 10, 20, 30]

lst_b = lst_a

lst_b[0] = 100

print(lst_b) # 100, 10, 20, 30
print(lst_a) # 100, 10, 20, 30

lst_a[2] = 200

print(lst_a) # 100, 10, 200, 30
print(lst_b) # 100, 10, 200, 30

