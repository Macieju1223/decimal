# decimal to hexadecimal

tab = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

dec = int(input('gimmie number: '))
hex: str = ''

while(dec>0):
    rem = dec%16
    hex = tab[rem] + hex
    dec = dec//16

print(f"HEX: {hex}")