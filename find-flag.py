foodstuff = ["Banana","Mango","Fish","Carrot","Cabbage"]

flag_found = False
for food in foodstuff:
    if food == "Mango":
        flag_found = True
        break

if flag_found:
    print("マンゴーが入ってます")
else:
    print("マンゴーは入っていません")
