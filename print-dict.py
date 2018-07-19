fruits = {
"バナナ": 300,
"オレンジ": 240,
"いちご": 350,
"マンゴー": 400
}

for name in fruits.keys():
    price = fruits[name]
    s = "{0}は、{1}円です。".format(name,price)
    print(s)
