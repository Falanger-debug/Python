# L = [3, 5, 4] ; L = L.sort()
# funkcja sort zwraca Null

# x, y = 1, 2, 3
# po lewej jest dwie zmienne, a po prawej 3 wartości do przypisania
# to spowoduje ValueError: too many values to unpack (expected 2)

# X = 1, 2, 3 ; X[1] = 4
# przypisanie do zmiennej X krotki, a następnie próba zmienienia jej wartości jest niedozwolona
# TypeError: 'tuple' object does not support item assignment

# X = [1, 2, 3] ; X[3] = 4
# listy są numerowane od 0, więc indeks 3 nie istnieje
# chcąc przypisać wartość 4 na kolejny indeks, należy użyć append

# X = "abc" ; X.append("d")
# stringi są niemutowalne w pythonie, więc nie można użyć metody append
# chcąc dodać literę d do stringa, należy użyć konkatenacji
# czyli X = X + "d"

# L = list(map(pow, range(8)))
# funkcja pow wymaga dwóch argumentów, a nie jeden
