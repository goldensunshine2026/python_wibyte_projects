import random
letters='abcdefghijklmnopqrstuvwxyz'

def extract_spaces(x):
    positions = []
    for i in range(len(x)):
        if x[i] == ' ':
            positions.append(i)
    x_no_space = x.replace(' ','')
    return x_no_space, positions

def restore_spaces(x, positions):
    x_list = list(x)
    for pos in positions:
        x_list.insert(pos,' ')
    return ''.join(x_list)

def group_five(x):
    s = ''
    for i in range(len(x)):
        s = s + x[i]
        if (i+1)%5==0 and i!=len(x)-1:
            s = s + ' '
    return s

def even_odd_swap(x):
    if len(x)%2!=0:
        x = x + ' '

    even_letters = x[0::2]
    odd_letters  = x[1::2]
    s=''

    for i in range(len(even_letters)):
        s = s+odd_letters[i]
        s = s+even_letters[i]
    
    return s

def swap_middle(x):
    if len(x)%2!=0:
        x = x + ' '

    first_half = x[0:int(len(x)/2):1]
    second_half = x[int(len(x)/2)::1]
    
    s = ''
    s = s + second_half 
    s = s + first_half
    return s
    
def reverse(x):
    s = x[::-1]
    return s

def swap_mid_rev(x):
    s_swap = swap_middle(x)
    s = reverse(s_swap)
    return s

def swap_mid_rev_decode(x):
    s_rev = reverse(x)
    s = swap_middle(s_rev)
    return s

def reverse_word(x):
    words = x.split(' ')
    s = ''
    for kk in range(len(words)):
        s = s+reverse(words[kk])+' '
    return s

def caesar_cipher(x, n):   
    s=''
    for i in range(len(x)):
        if x[i] == ' ':
            s = s + ' '
        else:
            idx = letters.find(x[i])
            new_idx = (idx+n)%26
            s = s + letters[new_idx]
    return s        

print()
print()

msg = 'python'
secret_code = ''

for kk in range(10):
    n = random.randint(0, 25)
    secret_code = secret_code + letters[n]

msg = msg + secret_code

msg, space_positions = extract_spaces(msg)

encoder = random.randint(0, 3)
encoder = 0

if encoder == 0:
    msg_enc = msg
elif encoder == 1:
    msg_enc = even_odd_swap(msg)
elif encoder == 2:
    msg_enc = reverse(msg)
else:
    msg_enc = swap_middle(msg)

msg_enemy = caesar_cipher(msg_enc, random.randint(1, 25))

print()
print('I am hearing ...')
print(group_five(msg_enemy))
print()

for kk in range(1, 26):
    msg_dec = caesar_cipher(msg_enemy, kk)
    msg_dec_eo = even_odd_swap(msg_dec)
    msg_dec_r  = reverse(msg_dec)
    msg_dec_ms = swap_middle(msg_dec)

    if msg_dec[0:6:1]=='python':
        print('code cracked ...')
        print('Secret code is ...')
        print(restore_spaces(msg_dec[6::1], space_positions))
        break

    elif msg_dec_eo[0:6:1]=='python':
        print('code cracked ...')
        print('Secret code is ...')
        print(restore_spaces(msg_dec_eo[6::1], space_positions))
        break

    elif msg_dec_r[0:6:1]=='python':
        print('code cracked ...')
        print('Secret code is ...')
        print(restore_spaces(msg_dec_r[6::1], space_positions))
        break

    elif msg_dec_ms[0:6:1]=='python':
        print('code cracked ...')
        print('Secret code is ...')
        print(restore_spaces(msg_dec_ms[6::1], space_positions))
        break