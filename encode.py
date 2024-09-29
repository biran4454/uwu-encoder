'''
^w^ # 1 [space]
uwu # 9 a-h
owo # 17 i-p
qwq # 25 q-x
uvu # 33
ovo # 41
qvq
'''

def encode_case(text, num):
    return [t.upper() if num & (4 >> i) else t for i,t in enumerate(text)] # thanks chatgpt for the bitshift, me is dum

def encode(num):
    if num == 0:
        return '^w^'
    text = ['']*3
    text[1] = 'vw'[num <= 25]
    num -= 2
    text[0] = 'uoquoq'[num // 8]
    text[2] = text[0]
    text = encode_case(text, num % 8)
    return ''.join(text)
    
letters = r" abcdefghijklmnopqrstuvwxyz0123456789.,()[]:=+-'"

filename = 'main.uwu'
open(filename, 'w').close()

print('Enter your code, and an empty line to stop. Indentation not supported.\n')
code = '0'
while code:
    code = input('>>>').strip()
    out = ''
    valid = True
    for letter in code:
        letter = letter.lower()
        if letter not in letters:
            print(f'Sorry, you can\'t use the character {letter}! Try that line again.')
            valid = False
            break
        uwu = encode(letters.index(letter))
        out += uwu
    if code and valid:
        with open(filename, 'a') as f:
            f.write(out + '\n')
        print('Encoded as', out[:60])