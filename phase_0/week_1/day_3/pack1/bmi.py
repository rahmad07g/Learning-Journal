nama = input("Masukkan Nama Anda: ")
berat = eval(input("Berat badan(kg): "))
tinggi = eval(input("Tinggi badan(cm): "))
tinggi = tinggi/100

def bmi_calculator (nama,berat,tinggi):
    bmi = berat/tinggi**2
    if bmi < 18.5:
        print(f"{nama} score bmi anda adalah {bmi} anda underweight")
    elif bmi >= 18.5 and bmi <=24.9:
        print(f"{nama} score bmi anda adalah {bmi} anda normal")
    else:
         print(f"{nama} score bmi anda adalah {bmi} anda overweight")
         
print(bmi_calculator(nama,berat,tinggi))