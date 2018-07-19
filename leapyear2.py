year = int(input("西暦何年？"))


#うるう年かどうか判定
# is_leap = False
# if year % 400 == 0:
#     is_leap = True
# elif year % 100 == 0:
#     is_leap = False
# elif year % 4 == 0:
#     is_leap = True
# else:
#     is_leap = False

is_leap = (year % 400 == 0)or(year % 100 != 0)and(year % 4 == 0)

if is_leap:
    print("うるうどしやで")
else:
    print("うるうどしちゃう")
