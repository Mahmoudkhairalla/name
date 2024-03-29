print("Great calcolator")
gread = int(input("what is your great percent?\n"))
if gread >= 90 and gread <= 100:
    print("your gread is A")
elif gread >= 80 and gread < 90:
    print("your gread is B")
elif gread >= 70 and gread < 80:
    print("your gread is C")
elif gread >= 60 and gread < 70:
    print("your gread is D")
elif gread >= 50 and gread < 60:
    print("your gread is E")
elif gread < 50:
    print("your gread is F")
else:
    print("you have to choose from 1 until 100")