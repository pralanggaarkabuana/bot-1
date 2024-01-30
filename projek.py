import random

def gen_pass():
    elements = "+-/*!&$#?=@<>"
    password = ""
    pass_length = 10

    for i in range(pass_length):
        password += random.choice(elements)

    return password

sampah_organik = ["daun","makanan sisa","kotoran hewan","ranting","cangkang telur","sisa sayuran","buah busuk","tulang"]

sampah_anorganik = ['kresek', 'kertas', 'kardus', 'ban/karet', 'kaca', "melamin", 'kaleng', 'botol plastik', 'baterai', 'kabel']
