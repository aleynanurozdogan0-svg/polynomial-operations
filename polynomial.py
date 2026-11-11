#polinom işlemleri
def readPoly():
    p = {}
    n = int(input("\n enter degree of polinom:"))
    for i in range(n + 1):                       
        p[i] = int(input(f"enter coefficient for x^{i}: "))
    return p

def print_poly(p):
    terms = []
    for expo in sorted(p.keys()):                # Üsleri küçükten büyüğe sırala
        coeff = p[expo]
        if coeff == 0:                           # 0 katsayılı terimi atla
            continue
        if expo == 0:
            terms.append(str(coeff))             # Sabit terim
        else:
            terms.append(f"{coeff}x^{expo}")
    print(" + ".join(terms) if terms else "0")   # Döngü dışında tek seferde yazdır

def add_poly(p1, p2):
    p3 = dict(p1)                                # p1'in kopyasıyla başla
    for expo, coeff in p2.items():
        p3[expo] = p3.get(expo, 0) + coeff       # Varsa topla, yoksa 0'a ekle
    return p3

def mul_poly(p1, p2):
    p3 = {}
    for e1, c1 in p1.items():
        for e2, c2 in p2.items():
            p3[e1 + e2] = p3.get(e1 + e2, 0) + c1 * c2  
    return p3

p1 = readPoly()
p2 = readPoly()
print_poly(mul_poly(p1, p2))