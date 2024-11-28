print ("Sinh vien : Nguyen Dinh Hai ")
print ("MSSV 23575202161028")
def get_sum(*num):
    tmp = 0
    for i in num:
        tmp += i
    return tmp
result = get_sum(1, 2, 3, 4, 5)
print(result)
