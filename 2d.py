'''
program napisany w pythonie
DES-bardzo zmodyfikowany z 128bitowy blokiem wiadomosci, 64bitowym kluczem zmieniona funkcjaF
tutaj link do wizualizacji tego co zmieniłam https://i.imgur.com/xngkGiY.png
nowe s-boxy jest ich 8 po 4 wiersze i 32 kolumny - używam 7 bitów klucza ->2 na wiersz, 5 na kolumny, jeden pomijam(gdybym uzyla 6 SBOX wygladalby mniej czytelnie )
zmiana dzialania funkcjiF bo mamy do obslugi 8 bitow^(tak jak napisano wyzej)
pomijam kompresje, tylko permutacje
nie uzywam permutacji poczatkowej IP i koncowej FP (w DESie nie byly potrzebne w sensie były żeby to nazwać desem ale nie uzywamy juz 8-bitowych magistrali)
gdyby cos nie dzialalo https://github.com/misss13/Programowanie_Skryptowe/blob/main/2d.py
widze ze wciencia wg się nie przekopiowały
'''
import textwrap


PC1 = [2, 39, 40, 13, 17, 3, 19, 42, 38, 47, 18, 0, 30, 43, 9, 15, 33, 37, 60, 10, 5, 36, 21, 28, 61, 51, 1, 53, 22, 31, 49, 55, 54, 20, 27, 34, 63, 23, 46, 52, 24, 35, 56, 8, 62, 26, 11, 25, 50, 14, 41, 32, 16, 44, 57, 29, 12, 58, 7, 4, 48, 59, 6, 45]
PC2 = [42, 40, 45, 52, 61, 26, 31, 32, 37, 49, 50, 9, 4, 57, 8, 55, 11, 14, 47, 7, 15, 6, 25, 1, 33, 54, 24, 43, 38, 36, 10, 0, 48, 39, 35, 41, 56, 19, 46, 62, 60, 30, 12, 18, 3, 58, 53, 63, 16, 51, 29, 2, 44, 13, 20, 5, 21, 59, 28, 17, 27, 23, 22, 34]
#PC1 i PC2 permutują 64 wartości

round_shifts = [2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2]
SBOX = [
    [
        [0, 9, 2, 30, 24, 17, 3, 10, 20, 6, 26, 16, 13, 7, 15, 18, 1, 25, 29, 21, 19, 5, 4, 12, 31, 11, 23, 14, 22, 28, 27, 8],
        [25, 5, 7, 8, 2, 26, 22, 21, 3, 16, 14, 27, 29, 9, 24, 11, 31, 4, 19, 17, 23, 15, 30, 10, 0, 18, 12, 28, 6, 20, 13, 1], 
        [22, 26, 4, 12, 1, 24, 11, 28, 27, 9, 0, 19, 5, 7, 25, 14, 2, 13, 10, 23, 3, 29, 18, 21, 31, 20, 15, 30, 8, 17, 6, 16], 
        [1, 28, 15, 24, 22, 13, 11, 0, 12, 20, 10, 5, 17, 7, 30, 18, 4, 14, 3, 27, 2, 8, 19, 16, 31, 26, 25, 6, 29, 9, 23, 21]
    ], 
    [
        [28, 21, 24, 3, 8, 4, 22, 2, 0, 19, 7, 9, 23, 11, 12, 5, 16, 30, 25, 1, 15, 31, 6, 29, 14, 18, 20, 27, 17, 13, 10, 26], 
        [1, 23, 12, 17, 21, 4, 15, 31, 27, 18, 7, 25, 3, 20, 29, 5, 13, 28, 26, 2, 11, 6, 16, 14, 24, 10, 30, 22, 9, 19, 8, 0], 
        [30, 20, 16, 23, 29, 12, 1, 2, 21, 17, 6, 27, 7, 22, 11, 24, 5, 3, 18, 19, 9, 8, 4, 15, 25, 10, 0, 13, 26, 31, 14, 28], 
        [15, 20, 9, 14, 8, 31, 11, 17, 19, 1, 18, 26, 29, 22, 16, 0, 12, 25, 30, 28, 10, 27, 4, 13, 3, 2, 21, 6, 7, 24, 5, 23]
    ], 
    [
        [3, 27, 31, 29, 22, 14, 2, 23, 10, 28, 5, 9, 18, 30, 16, 15, 12, 0, 7, 6, 21, 1, 26, 24, 20, 25, 13, 17, 19, 8, 4, 11], 
        [17, 1, 16, 14, 9, 30, 23, 31, 12, 5, 4, 8, 7, 19, 25, 0, 28, 27, 3, 20, 18, 11, 26, 10, 2, 13, 21, 29, 6, 24, 22, 15], 
        [12, 23, 10, 15, 27, 14, 18, 3, 22, 13, 7, 8, 30, 5, 20, 17, 9, 19, 24, 0, 21, 1, 16, 2, 11, 6, 25, 4, 31, 26, 29, 28], 
        [20, 17, 16, 4, 22, 15, 7, 14, 0, 1, 5, 18, 3, 26, 9, 25, 12, 19, 27, 11, 29, 13, 23, 2, 28, 8, 21, 31, 30, 10, 6, 24]
    ], 
    [
        [5, 0, 21, 4, 12, 1, 29, 14, 25, 10, 2, 16, 31, 27, 22, 11, 26, 6, 9, 30, 8, 15, 18, 20, 23, 28, 7, 24, 19, 3, 17, 13],
        [7, 10, 18, 3, 30, 24, 5, 25, 13, 12, 26, 23, 28, 8, 31, 0, 20, 16, 6, 2, 9, 15, 29, 1, 21, 27, 14, 4, 22, 11, 19, 17], 
        [26, 28, 23, 15, 5, 10, 3, 22, 30, 14, 29, 31, 16, 12, 20, 24, 13, 27, 17, 2, 21, 6, 11, 8, 18, 9, 19, 25, 1, 7, 0, 4], 
        [23, 28, 17, 21, 22, 14, 9, 2, 11, 0, 10, 5, 25, 7, 8, 19, 30, 6, 16, 27, 15, 26, 12, 20, 24, 31, 3, 4, 18, 1, 29, 13]
    ], 
    [
        [26, 30, 9, 1, 19, 6, 23, 21, 3, 25, 18, 28, 11, 31, 2, 14, 24, 20, 17, 0, 29, 10, 7, 15, 27, 8, 12, 22, 13, 4, 16, 5],
        [31, 19, 18, 7, 12, 13, 15, 4, 28, 2, 29, 11, 20, 1, 6, 26, 5, 16, 24, 9, 0, 30, 21, 14, 3, 17, 22, 8, 27, 25, 10, 23],
        [10, 21, 9, 8, 27, 1, 25, 5, 11, 13, 18, 22, 6, 24, 12, 3, 19, 4, 26, 23, 7, 15, 30, 17, 28, 16, 14, 20, 2, 0, 31, 29], 
        [31, 25, 7, 22, 23, 0, 15, 30, 8, 18, 9, 2, 28, 19, 13, 12, 21, 5, 17, 14, 10, 24, 26, 27, 3, 4, 29, 1, 6, 20, 16, 11]
    ], 
    [
        [16, 2, 21, 11, 14, 8, 29, 19, 20, 26, 18, 10, 27, 31, 28, 5, 7, 15, 0, 3, 22, 9, 17, 24, 30, 1, 6, 4, 23, 12, 13, 25], 
        [17, 14, 12, 6, 25, 8, 19, 22, 31, 9, 30, 7, 13, 5, 18, 0, 4, 24, 29, 11, 26, 1, 28, 2, 15, 10, 27, 20, 23, 21, 3, 16], 
        [25, 29, 27, 30, 28, 13, 2, 5, 31, 17, 9, 8, 16, 15, 4, 12, 19, 21, 20, 18, 0, 24, 10, 14, 1, 7, 22, 6, 23, 3, 26, 11], 
        [26, 1, 24, 7, 19, 10, 30, 9, 27, 5, 17, 25, 28, 4, 0, 15, 31, 3, 21, 20, 29, 14, 8, 2, 11, 22, 12, 23, 16, 6, 18, 13]
    ], 
    [
        [21, 6, 16, 19, 14, 9, 1, 31, 12, 3, 18, 8, 26, 22, 20, 4, 13, 28, 0, 17, 24, 10, 5, 29, 30, 25, 2, 15, 27, 23, 11, 7],
        [23, 21, 5, 29, 13, 25, 1, 2, 31, 4, 11, 0, 7, 28, 19, 9, 30, 3, 27, 24, 26, 8, 14, 20, 16, 10, 15, 17, 12, 18, 22, 6],
        [14, 13, 5, 31, 27, 24, 3, 26, 29, 25, 30, 11, 12, 15, 2, 21, 16, 1, 7, 9, 0, 28, 20, 23, 10, 4, 6, 22, 18, 8, 19, 17], 
        [2, 14, 28, 25, 8, 4, 10, 23, 26, 29, 24, 13, 17, 0, 7, 27, 3, 22, 1, 31, 20, 5, 16, 9, 6, 15, 12, 18, 11, 30, 21, 19]
    ], 
    [
        [18, 3, 4, 28, 23, 5, 22, 7, 21, 1, 6, 8, 19, 31, 16, 30, 20, 29, 24, 0, 9, 27, 12, 15, 25, 14, 11, 26, 17, 2, 13, 10], 
        [25, 3, 5, 13, 18, 6, 27, 15, 21, 11, 1, 12, 0, 24, 23, 22, 31, 10, 20, 9, 26, 30, 4, 8, 14, 7, 2, 17, 19, 29, 28, 16], 
        [1, 26, 15, 31, 11, 17, 25, 2, 10, 5, 29, 19, 22, 23, 0, 3, 9, 16, 20, 8, 4, 6, 13, 21, 27, 28, 14, 7, 30, 12, 18, 24], 
        [6, 17, 15, 5, 25, 4, 21, 0, 10, 18, 3, 7, 29, 22, 27, 11, 16, 30, 28, 2, 24, 12, 1, 26, 20, 19, 14, 13, 23, 31, 9, 8]
    ]
]
#4 wiersze po 32 wartości w jednym wierszu, ogolem 8 boxów w sboxie


def apply_PC1(pc1_table,keys_64bits):
    """Tylko permutuje dlugosc - 64 wszystko"""
    keys_64sbits = ""
    for index in pc1_table:
        keys_64sbits += keys_64bits[index] 
    return keys_64sbits

def split128bits_in_half(keys_128bits):
    left_keys, right_keys = keys_128bits[:64],keys_128bits[64:]
    return left_keys, right_keys

def split64bits_in_half(keys_64bits):
    left_keys, right_keys = keys_64bits[:32],keys_64bits[32:]
    return left_keys, right_keys

def circular_left_shift(bits,numberofbits):
     shiftedbits = bits[numberofbits:] + bits[:numberofbits]
     return shiftedbits

def apply_PC2(pc2_table,keys_64bits):
    """Tylko permutuje  dlugosc - 64 wszystko"""
    keys_64sbits = ""
    for index in pc2_table:
        keys_64sbits += keys_64bits[index]
    return keys_64sbits

def generate_keys(key_64bits):
    """generuje klucze 64bitowe po 16 rund"""
    round_keys = list() 
    keys_64sbits= apply_PC1(PC1, key_64bits)
    left32, right32 = split64bits_in_half(keys_64sbits)
    for i in round_shifts:
        left32 = circular_left_shift(left32, i)
        right32 = circular_left_shift(right32, i)
        subkey = apply_PC2(PC2, (left32+right32))
        round_keys.append(subkey)
    return round_keys

def apply_Expansion(expansion_table,bits48):
    """Rozszerza uzywam do 48na64 bity i permutuje"""
    bits64 = ""
    for index in expansion_table:
        bits64 += bits48[index]
    return bits64

def XOR(bits1,bits2):
    xor_result = ""
    for index in range(len(bits1)):
        if bits1[index] == bits2[index]: 
            xor_result += '0'
        else:
            xor_result += '1'
    return xor_result

#podział wiadomości na 8-bitowe porcje 64/8=8
def split64bits_in_8bits(XOR_48bits):
    """Podział bloku 64-bitowego na 8-bitowe porcje """
    list_of_6bits = textwrap.wrap(XOR_48bits,8)
    return list_of_6bits

def get_first_and_last_bit(bits6):
    """Pobierz pierwszy i ostatni bit z 8-bitowego łańcucha bitów -> 4wiersze"""
    twobits = bits6[0] + bits6[-1] 
    return twobits

def get_middle_four_bit(bits6):
    """Pobierz środkowe 5 bitów z z 8-bitowego łańcucha bitów nie pobieram jednego bitu -> żeby były 32 kolumny"""
    fourbits = bits6[1:6]
    return fourbits

def binary_to_decimal(binarybits):
    """ Konwersja łańcucha bitów do wartości dzięsiętnej """
    decimal = int(binarybits,2)
    return decimal

def decimal_to_binary(decimal):
    """ Konwersja wartości dziesiętnej do 6-bitowego łańcucha bitów """
    binary4bits = bin(decimal)[2:].zfill(6)
    return binary4bits

def sbox_lookup(sboxcount,first_last,middle4):
    """ Dostęp do odpowiedniej wartości odpowiedniego sboxa [nr boxa][wiersz][kolumna]""" 
    d_first_last = binary_to_decimal(first_last)
    d_middle = binary_to_decimal(middle4)
    sbox_value = SBOX[sboxcount][d_first_last][d_middle]
    return decimal_to_binary(sbox_value)

EXP = [19, 17, 6, 30, 25, 2, 31, 42, 43, 28, 14, 34, 8, 13, 24, 16, 23, 5, 22, 0, 44, 38, 39, 36, 12, 40, 10, 18, 15, 37, 20, 4, 35, 41, 11, 29, 46, 3, 33, 47, 9, 27, 45, 21, 26, 32, 1, 7, 11, 2, 12, 13, 4, 7, 15, 5, 10, 9, 0, 8, 3, 6, 14, 1]
#tablica rozszerzalna na 64 bity

def functionF(pre64bits, key64bits):
    """bierze 64bit klucz 64bit blok wiad zwraca 48bitowy blok ale dopelnia do 64bit wiec zwraca finalnie 64bit"""
    final96bits = ''
    pre_XOR = XOR(pre64bits,key64bits)
    list1 = list()
    list1 = split64bits_in_8bits(pre_XOR)
    sbox = 0
    for chunk in list1:
        row = get_first_and_last_bit(chunk)
        column = get_middle_four_bit(chunk)
        #kolumna ma 5 miejsc 2^5+2^4+2^3+2^2+2^1+1 = 31 -> dlatego sboxy maja dl 32bity
        result = sbox_lookup(sbox, row, column)
        sbox += 1
        final96bits += result
    finalbits = apply_Expansion(EXP, final96bits)
    return finalbits

get_bin = lambda x, n: format(x, 'b').zfill(n)
#t_znaki na t_inty
def intoIntArray(message: str):
    int_array = []
    mesg_array = list(message) 
    for i in mesg_array:
        int_array.append(ord(i))
    return int_array

#t_kodow na t_znakow 
def intoCharArray(message: list):
    mesg_char = []
    for i in message:
        mesg_char.append(chr(i))
    return mesg_char

def intListToBinStr(message_list):
    binary = []
    for x in message_list: 
        binary.append(get_bin(x, 8))
    binary_str = ""
    for x in binary:
        binary_str+=x 
    return binary_str

def Siec_Feistela(L, R, roundkeys, index):
    L1 = R
    R1 = XOR(L, functionF(R, roundkeys[index]))
    return L1, R1

def Siec_Feistela_reverse(L, R, roundkeys, index):
    R1 = L
    L1 = XOR(R, functionF(L, roundkeys[index]))
    return L1, R1

#########################
M = "Attack!!Attack!!"
#wiad
key = "jaksiecieszezedziala!!!!!!!" 
#klucz
#########################

plaintext = intListToBinStr(intoIntArray(M)) 
print("Plaintext(128 bits):", plaintext[:128])
binary_key = intListToBinStr(intoIntArray(key)) 
print("Key (only 64 bits) :", binary_key[:64])
roundKeys = generate_keys(binary_key[:64])

def DES_encrypt(message,key):
    cipher = ""
    L, R = split128bits_in_half(message)
    for i in range(16):
        L, R = Siec_Feistela(L, R, roundKeys, i)
    cipher = R + L
    return cipher
    
def DES_decrypt(message,key):
    cipher = ""
    R, L = split128bits_in_half(message)
    for i in range(15, -1, -1):
        L, R = Siec_Feistela_reverse(L, R, roundKeys, i)
    cipher = L + R
    return cipher    

ciphertext = DES_encrypt(plaintext, binary_key)
print("Ciphertext:         ", ciphertext)
encrypted = DES_decrypt(ciphertext, binary_key)
print("Encrypted message:  ", encrypted)
print(XOR(plaintext, encrypted))