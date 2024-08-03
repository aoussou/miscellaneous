str_ = ""

n = 64 # must be a mutliple of 4

for i in range(1, n, 2):

    n1 = n - i + 1
    n2 = i
    n3 = i + 1
    n4 = n - i

    str_1 = str(n1) + "," + str(n2) + ","
    str_2 = str(n3) + "," + str(n4) + ","

    str_ += str_1
    str_ += str_2

    if n3 == n / 2:
        break

str_ = str_[:-1]
print(str_)
