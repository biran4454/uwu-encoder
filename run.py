def decode_case(uwu: str):
    return sum(u.isupper() * pow(2, 2-i) for i,u in enumerate(uwu))

def decode(uwu):
    if uwu[0] == '^':
        return 0
    return 2 + (uwu[1] in 'vV') * 24 + 'uoq'.index(uwu[0].lower()) * 8 + decode_case(uwu)

letters = r" abcdefghijklmnopqrstuvwxyz0123456789.,()[]:=+-'"

filename = 'main.uwu'
with open(filename, 'r') as f:
    lines = f.readlines()

code_line = ""
for line in lines:
    line = line.strip()
    for i in range(0, len(line), 3):
        letter = letters[decode(line[i:i+3])]
        code_line += letter
    exec(code_line)