#print("a5".isidentifier())
print("Identyfikatory:\n",
      "Dodawanie:\n"
      "Odejmowanie:\n"
      "Mnożenie\n"
      "Dzielenie\n"
      "Liczba całkowita\n"
      "Nawias\n\n")


wzor=input("Podaj wzór:")
wzor=wzor.replace(" ", "")
#print(wzor)

blad=False
ilosc_otwarc_nawiasow=0
s=""
tab=[]


if wzor[0] in "+*/":
    print("Wyrazenie nie moze sie zaczynac od znaku: ", wzor[0], " pozycja: ", 0)
    blad=True
elif wzor[0]==')':
    print("Nawias zamykajacy na pozycji:", 0)
    blad = True
elif wzor[0]=='(':
    ilosc_otwarc_nawiasow+=1
elif wzor[0].isdigit() or wzor[0].isalpha():
    s+=wzor[0]
elif not wzor[0] in "+-*/()":
    print("Invalid symbol: ", wzor[0], "pozycja: ", 0)
    blad = True


for i in range(1, len(wzor)):

    if not s=="" and not s.isdigit() and not s.isidentifier():
        print ("Niepoprawny symbol pozycjax: ", i-1)
        blad=True
    if not wzor[i].isdigit() and not wzor[i].isalpha():
        s=""
    if wzor[i]==')':

        if ilosc_otwarc_nawiasow<1:
            print("Bład, zły nawias, pozycja: ", i)
            blad = True
            continue
        if wzor[i-1]=='(':
            print("Pusty nawias,pozycja: ", i-1)
            blad = True
            continue
        if wzor[i-1] in "+-*/":
            print("Znak przed konczacym nawiasem, pozycja:",i-1)
            blad = True
            continue
        ilosc_otwarc_nawiasow-=1
        continue

    if wzor[i]=='(':
        ilosc_otwarc_nawiasow+=1
        if wzor[i-1].isdigit() :
            print("Nawias tuż po liczbie, pozycja: ", i)
            blad = True
            continue
        if wzor[i - 1].isalpha():
            print("Nawias tuż po identyfikatorze, pozycja: ", i)
            blad = True
        if wzor[i-1]==')':
            print("Nawias sie konczy i nowy zaczyna, pozycja: ", i)
            blad = True
            continue
        continue
    if wzor[i] in "+*/":
        if wzor[i-1]=='(':
            print("Niepoprawny pierwszy znak w nawiasie, pozycja:", i)
            blad = True
            continue

    if wzor[i] in "+-*/":

        if wzor[i-1] in "+-*/":
            print("Dwa znaki obok siebie, pozycja:", i)
            blad = True
            continue
        continue


    if wzor[i]=='0' and not wzor[i-1].isdigit() and not wzor[i-1].isalpha():
        if i!=len(wzor)-1:
            if wzor[i+1].isdigit():
                print("Liczba wielocyfrowa nie moze zaczynac sie od 0, pozycja:", i)
                blad = True
    if wzor[i].isdigit():
        s += wzor[i]
        if wzor[i-1]==')':
            print("Liczba za nawiasem zamykajacym, pozycja: ", i)
            blad = True
            continue
        continue
    if wzor[i].isalpha():
        s+=wzor[i]
        if wzor[i-1]==')':
            print("Identyfikator za nawiasem zamykajacym, pozycja: ", i)
            blad = True
            continue
        continue
    print("Invalid symbol: ", wzor[i], "pozycja: ", i)
    blad = True

if wzor[-1] in "+-*/":
    print("Wyrazenie, nie moze konczyc sie znakiem",wzor[-1],", pozycja: ", len(wzor)-1)
    blad = True

if ilosc_otwarc_nawiasow !=0:
    print("Brakuje zamkniecia ", ilosc_otwarc_nawiasow, "nawiasow, pozycja:", len(wzor))
    blad = True
if not s=="" and not s.isdigit() and not s.isidentifier():
    print ("Niepoprawny symbol pozycja: ", len(wzor)-1)
    blad=True

if blad:
    exit(1)

liczba=False
liczby=""

przedujemna=True

id={
    '+':"Dodawanie: ",
    '-':"Odejmowanie: ",
    '*':"Mnozenie: ",
    '/':"Dzielenie: ",
    '(':"Nawias: ",
    ')': "Nawias"
}

for i in wzor:

    if liczba and not i.isdigit() and not i.isalpha():
        if(liczby.isidentifier()):
            print("identyfikator", liczby)
        else:
            print("liczba calkowita, ", liczby)
        liczba=False
        liczby=""

    if i=='-':
        if przedujemna:
            liczby+='-'
            przedujemna=False
            continue
        else:
            przedujemna=False
            print("Odejmowanie, -")
        continue
    przedujemna=False
    if i in id.keys():
        print(id[i], i)
        continue
    if i.isdigit() or i.isalpha():
        liczba=True
        liczby+=i
        continue

    print("blad, niepoprawny znak: ", i)
    exit(1)

if not liczby=="":
    if (liczby.isidentifier()):
        print("identyfikator", liczby)
    else:
        print("liczba calkowita, ", liczby)

