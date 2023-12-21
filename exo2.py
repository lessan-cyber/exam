liste =["aziz", "lessan", "mo",1,"mariam",69,"wiskid", "burna Boy"]
for element in liste:
    if type(element) == str:
        print(element)
    else:
        print("not a string")

with open("exo2.json", "x") as f:
    json.dump(liste, f)
    f.seek(0)