P1, P2 = input().split()
if(P1==P2):
    print("pertandingan seri")
elif((P1=="gunting" and P2=="kertas") or (P1=="kertas" and P2=="batu") or (P1=="batu" and P2=="gunting")):
    print("P1 menang")
else:
    print("P2 menang")