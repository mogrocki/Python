from math import sqrt;


a = int(input("Podaj pierwsza liczbe: "));
b = int(input("Podaj druga liczbe: "));
c = int(input("Podaj trzecia liczbe: "));

if a<=0:
    print("Nie można policzyc delty");
else:
        delta = b*b-4*a*c;
        d = sqrt(delta);
        print("delta wynosi:",d);

if (d <= 0):
    print("Nie obliczymy miejsca zerowe");
elif (d == 0):
        x = -b/(2*a);
        print("Miejsce zerowe wynosi:",x);
elif (d >= 0):
        x1 = ((-b-d)/(2*a));
        x2 = ((-b+d)/(2*a));
        print("Pierwsze miejsce zerowe wynosi:",x1);
        print("Drugie miejsce zerowe:",x2);

input("\n\nPo zakonczeniu programu wciśnij ENTER");
        
    
        
