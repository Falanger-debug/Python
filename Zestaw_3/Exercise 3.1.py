# x = 2; y = 3;
# if (x > y):
#     result = x;
# else:
#     result = y;
# W tym przypadku kod jest poprawny, ale nie jest zalecane używanie średników do zakończenia instrukcji w Pythonie.
# Średniki są opcjonalne.


# for i in "axby": if ord(i) < 100: print (i)
# ta iteracja po stringu nie zadziała, ponieważ warunek if powinien się znaleźć w nowej linii
# tak samo jak print w jeszcze kolejnej linii


# for i in "axby": print (ord(i) if ord(i) < 100 else i)
# W tym przypadku wszystko jest ok, ponieważ warunek if jest zapisany w jednej linii