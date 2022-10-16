final,tax1,tax2,tax3,tax4 = 0,0,0,0,0
def taxa(valor, tax):
    calc = valor * tax
    return calc
salary = float(input())
if salary <= 2000:
    print("Isento")
    exit()
if salary > 4500:
    tax4 = taxa(salary-4500,0.28)
    tax3 = taxa(1500,0.18)
    tax2 = taxa(1000,0.08)
    tax1 = tax4+tax3+tax2
if salary >= 3000.01 and salary <= 4500:
    tax3 = taxa(salary-3000,0.18)
    tax2 = taxa(1000,0.08)
    tax1 = tax3+tax2
if salary >= 2000.01 and salary <= 3000:
    tax2 = taxa(salary-2000,0.08)
    tax1 = tax2
tax1 = str(round(tax1, 2))
print('R$ '+tax1)
