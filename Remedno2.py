# Kriteria:

# Diawali dengan angka 4, 5 atau 6.
# Terdiri atas tepat 16 digit angka.
# Hanya mengandung angka 0-9.
# Boleh dituliskan berupa grup 4 digit yang dipisahkan dengan tanda hubung "-"
# Tidak boleh terdapat 1 angka yang diulang >3x & tertulis secara beruntun, misal: 3333.

'''
pseudo code
if "4" in x:
elif "5" in x:
elif "6" in x:
elif x.isdigit() == True:
elif "-" in x:

ccValid = {}
ccInvalid = {}
'''

ccNasabah = [
        {"nama": "Joni", "noCreditCard": "4253625879615781"},
        {"nama": "Andre", "noCreditCard": "5123-4567-8912-3455"},
        {"nama": "Adam", "noCreditCard": "0525362587961578"},
        {"nama": "Chris", "noCreditCard": "42536258796157867"},
        {"nama": "Chandra", "noCreditCard": "4424424424442442"},
        {"nama": "Desi", "noCreditCard": "44244z4424442444"},
        {"nama": "Lady", "noCreditCard": "5122.2368.7954.3214"},
        {"nama": "Mike", "noCreditCard": "4424444424442444"},
        {"nama": "John", "noCreditCard": "5122-2368-7954-3213"},
        {"nama": "Kopi", "noCreditCard": "61234-123-8912-3456"},
        {"nama": "Richard", "noCreditCard": "5199-9967-7912-3457"},
        {"nama": "Rick", "noCreditCard": "1111222233334444"},
        {"nama": "Mira", "noCreditCard": "5123 - 4567 - 8912 - 3456"},
        {"nama": "Dean", "noCreditCard": "4123356789123456"},
        {"nama": "Sam", "noCreditCard": "4123456789123454"}
]

angkaboleh = "4","5","6"

print(angkaboleh)

# for i in ccNasabah[0]["noCreditCard"]:
if angkaboleh in ccNasabah[0]["noCreditCard"]:
    print("boleh")




akses nomer kartu kreditnya
print(str(ccNasabah[0]["noCreditCard"]))
print(str(ccNasabah[1]["noCreditCard"]))
print(str(ccNasabah[2]["noCreditCard"]))
print(str(ccNasabah[3]["noCreditCard"]))
print(str(ccNasabah[4]["noCreditCard"]))
print(str(ccNasabah[5]["noCreditCard"]))
print(str(ccNasabah[6]["noCreditCard"]))
print(str(ccNasabah[7]["noCreditCard"]))
print(str(ccNasabah[8]["noCreditCard"]))
print(str(ccNasabah[9]["noCreditCard"]))
print(str(ccNasabah[10]["noCreditCard"]))
print(str(ccNasabah[11]["noCreditCard"]))
print(str(ccNasabah[12]["noCreditCard"]))
print(str(ccNasabah[13]["noCreditCard"]))
print(str(ccNasabah[14]["noCreditCard"]))

