# -*- coding: utf-8 -*-

animal_speed_dict = {
"チーター": 100, "トナカイ": 80, "シマウマ": 60,
"ライオン": 58,"キリン": 50,"ラクダ": 30
}

distance_dict = {
"静岡": 183.7,
"名古屋": 350.6,
"大阪": 507.5
}

def calc_time(dist, speed):
    t = dist / speed
    t = round(t,1)
    return t

def calc_animal(animal, speed):
    res = "|" + animal
    for city in sorted(distance_dict.keys()):
        dist = distance_dict[city]
        t = calc_time(dist, speed)
        res += "{0:>6}".format(t)
    return res + "|"

print("+--------+------+------+------+")
print("|動物名前",end="")
for city in sorted(distance_dict.keys()):
    print("|" + city, end="")
print("|")
print("+--------+------+------+------+")

for animal, speed in sorted(animal_speed_dict.items()):
    s = calc_animal(animal, speed)
    print(s)
print("+--------+------+------+------+")
