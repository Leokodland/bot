def gen_num():
    num = ["1","2","3","4","5"]
    return random.choice(num)
    import random
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)
def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "TESTA"
    else:
        return "CODA"
def somma():
    a = int(input("Inserisci il primo:"))
    b = int(input("Inserisci il secondo:"))
    c = a + b
    return c
