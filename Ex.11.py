x=int(input("Introduceti numarul de elemante din vector="))
z=[]
print("Introduceti ",x," elemente pentru vector")
for i in range(0,x):
    w=int(input('Introduceti elementul='))
    z.extend([w])
print("a)	 afişează pe ecran componentele tabloului la un interval de 5 poziţii;")
print(z)
print("b)	 afişează pe ecran numerele în ordinea inversă a introducerii în calculator;")
b=z
print(b[::-1])
print("c)	 sortează componentele tabloului în ordine descrescătoare;")
c=sorted(z)
c.sort(reverse=True)
print(c)
print("d)	 afişează pe ecran doar componentele pare;")
d=[]
for i in range(0, len(z)):
    if z[i]%2==0:
        y=z[i]
        d.extend([y])
print(d)
print("e)	 afişează pe ecran media aritmetică a componentelor pare;")
e=sum(d)/len(d)
print(e)
print("f)	 afişează pe ecran doar componentele impare;")
f=[]
for i in range(0, len(z)):
    if z[i]%2==1:
        y=z[i]
        f.extend([y])
print(f)
print("g)	 afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură);")
x1=int(input("Introduceti un numar "))
y1=int(input("Introduceti un numar "))
g=[]
for i in range(0, len(z)):
    if z[i]>x1 and z[i]/y1!=0:
        r=z[i]
        g.extend([r])
print(g)
print("h)	 afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură);")
x2=int(input("Introduceti un numar "))
y2=int(input("Introduceti un numar "))
h=[]
for i in range(0, len(z)):
    if z[i]>x2 and z[i]<y2:
        t=z[i]
        h.extend([t])
print(h)
print("i)	 afişează pe ecran poziţiile (indicii) componentelor impare negative;")
print("j)	 afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative;")
print("k)	 înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv;")
print("l)	 înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia;")
print("m)	creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură;")
x2=int(input("Introduceti numarul de elemante din vector="))
m1=[]
m=[]
print("Introduceti ",x2," elemente pentru vector")
for i in range(0,x2):
    w=int(input('Introduceti elementul='))
    m1.extend([w])
    if m1[i]%2==0:
        r2=m1[i]
        m.extend([r2])
print(m)   
print("n)	 creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură;")
x1=int(input("Introduceti numarul de elemante din vector="))
n1=[]
n=[]
print("Introduceti ",x1," elemente pentru vector")
for i in range(0,x1):
    w=int(input('Introduceti elementul='))
    n1.extend([w])
    if n1[i]%3==0 and n1[i]!=0:
        r1=n1[i]
        n.extend([r1])
print(n)   
print("o)	 creează un tablou nou, format doar din acele componente ale tabloului in- trodus de la tastatură care au cel mult patru divizori.")
x3=int(input("Introduceti numarul de elemante din vector="))
o1=[]
o=[]
print("Introduceti ",x3," elemente pentru vector")
for i in range(0,x3):
    w=int(input('Introduceti elementul='))
    o1.extend([w])
    if o1[i]%1==0 and o1[i]%2==0 and o1[i]%4==0 and o1[i]-o1[i]==0 and o1[i]!=0 or o1[i]%1==0 and o1[i]%5==0 and o1[i]%25==0 and o1[i]!=0:
        r3=o1[i]
        o.extend([r3])
print(o)   