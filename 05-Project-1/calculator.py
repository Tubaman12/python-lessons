money = int(input())
partyamount = int(input())
tip1 = round(money * 0.15, 2)
tip2 = round(money * 0.20, 2)
tip3 = round(money * 0.25, 2)
if partyamount > 8:
    print("A 20% tip is automatically added to parties of 8 or more. Your bill is {}".format(tip2))
else:
    print("Your tip options are:\n 15%: {}".format(tip1) + "\n 20%: {}".format(tip2) + "\n 25%: {}".format(tip3))
