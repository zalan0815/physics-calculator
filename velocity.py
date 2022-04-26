a1 = input("Első adat: ")
a2 = input("Második adat: ")

d1 = str(a1).split("=")
d2 = str(a2).split("=")

v = None
t = None
s = None


match d1[0]:                
    case "v": 
        v = float(d1[1])
    case "s":
        s = float(d1[1])
    case "t":
        t = float(d1[1]) 

match d2[0]:
    case "v": 
        v = float(d2[1])
    case "s":
        s = float(d2[1])
    case "t":
        t = float(d2[1]) 


# match == None:
#     case v:
#         szam = s / t
#         print(f'v={szam}')
#     case t:
#         szam = s / v
#         print(f't={szam}')
#     case s:
#         szam = v * t
#         print(f's={szam}')

if v != None and s != None:
    szam = s / v
    print(f't={szam}')

elif t != None and s != None:
    szam = s / t
    print(f'v={szam}')

elif v != None and t != None:
    szam = v * t
    print(f's={szam}')