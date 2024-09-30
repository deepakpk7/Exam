import add as c
import sub as s
import div as d
import mul as m
import modu as mo
while True:
    

    print("""
        1.Addition
        2.sub
        3.Mulitiplication
        4.Division
        5.Moduless
        6.exist""")
    cho=int(input("Enter the choices :"))
    a=int(input("enter  the no: "))
    b=int(input("enter  the no: "))
    if cho==1:
        c.add(a,b)
    elif cho==2:
        s.sub(a,b)
    elif cho==3:
        m.mul(a,b)
    elif cho==4:
        d.div(a,b)
    elif cho==5:
        mo.modules(a,b)
    elif cho==6:
        break
    else:
        print("Invalid ")
    
