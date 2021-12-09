'''
DES z 128bitowy kluczem
nowe s-boxy jest ich 16scie
pomijam kompresje nowe permutacje
DES-2 przepuszczenie 2 razy przez algorytm tekstu jak w DES-3 ale 2 razy
'''
import textwrap


PC1 = [2, 39, 40, 13, 17, 3, 19, 42, 38, 47, 18, 0, 30, 43, 9, 15, 33, 37, 60, 10, 5, 36, 21, 28, 61, 51, 1, 53, 22, 31, 49, 55, 54, 20, 27, 34, 63, 23, 46, 52, 24, 35, 56, 8, 62, 26, 11, 25, 50, 14, 41, 32, 16, 44, 57, 29, 12, 58, 7, 4, 48, 59, 6, 45]
PC2 = [42, 40, 45, 52, 61, 26, 31, 32, 37, 49, 50, 9, 4, 57, 8, 55, 11, 14, 47, 7, 15, 6, 25, 1, 33, 54, 24, 43, 38, 36, 10, 0, 48, 39, 35, 41, 56, 19, 46, 62, 60, 30, 12, 18, 3, 58, 53, 63, 16, 51, 29, 2, 44, 13, 20, 5, 21, 59, 28, 17, 27, 23, 22, 34]
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
    ],
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
]#po 32 wartości w wierszu 16 boxów bo 128/8=16

EXPANSION_TABLE = [17, 112, 115, 122, 89, 46, 6, 36, 0, 118, 66, 71, 106, 80, 108, 124, 14, 95, 62, 26, 22, 123, 56, 10, 104, 53, 12, 19, 79, 24, 60, 41, 38, 111, 97, 61, 40, 65, 3, 99, 92, 52, 86, 49, 18, 107, 82, 42, 68, 45, 76, 37, 74, 9, 81, 119, 31, 44, 77, 16, 5, 51, 75, 28, 113, 23, 30, 8, 43, 110, 126, 25, 120, 48, 114, 83, 47, 50, 125, 87, 33, 35, 13, 39, 59, 29, 63, 34, 103, 27, 78, 4, 121, 88, 15, 72, 127, 69, 96, 90, 58, 91, 70, 109, 55, 101, 7, 54, 102, 105, 1, 21, 64, 57, 116, 85, 93, 94, 20, 117, 2, 73, 100, 67, 98, 84, 11, 32]
PERMUTATION_TABLE = [44, 14, 79, 54, 84, 32, 81, 50, 91, 33, 11, 64, 74, 88, 16, 1, 62, 27, 39, 28, 19, 73, 45, 70, 59, 47, 53, 13, 94, 87, 15, 57, 55, 3, 85, 29, 56, 83, 52, 72, 9, 60, 20, 18, 49, 41, 36, 30, 2, 40, 26, 61, 37, 77, 17, 71, 24, 67, 34, 4, 65, 93, 38, 35, 75, 22, 82, 66, 48, 21, 86, 80, 12, 31, 92, 8, 76, 95, 63, 69, 43, 42, 78, 6, 46, 0, 5, 89, 90, 58, 10, 68, 7, 51, 23, 25]
#permutacji bedzie 6*16 czyli 96 max - (UWAGA ale używam tylko 5 bitów!)
INITIAL_PERMUTATION_TABLE = [43, 0, 61, 120, 92, 102, 105, 126, 112, 72, 48, 117, 44, 108, 34, 96, 35, 11, 77, 55, 73, 90, 21, 103, 37, 8, 100, 69, 22, 29, 84, 88, 53, 97, 38, 25, 27, 12, 45, 3, 106, 118, 42, 9, 121, 41, 5, 6, 75, 10, 20, 51, 81, 85, 78, 47, 83, 32, 93, 63, 30, 19, 79, 87, 18, 86, 110, 15, 7, 57, 101, 24, 4, 125, 49, 67, 115, 91, 94, 95, 66, 60, 16, 82, 17, 76, 70, 46, 123, 127, 23, 107, 124, 56, 39, 1, 14, 111, 26, 71, 68, 80, 64, 119, 52, 40, 36, 74, 65, 109, 33, 113, 2, 28, 54, 58, 116, 99, 59, 104, 122, 62, 13, 114, 89, 50, 31, 98]


def apply_PC1(pc1_table,keys_64bits):
    keys_128bits = ""
    for index in pc1_table:
        keys_128bits += keys_64bits[index] 
    return keys_128bits

def split128bits_in_half(keys_128bits):
    left_keys, right_keys = keys_128bits[:64],keys_128bits[64:]
    return left_keys, right_keys

def circular_left_shift(bits,numberofbits):
     shiftedbits = bits[numberofbits:] + bits[:numberofbits]
     return shiftedbits

def apply_PC2(pc2_table,keys_56bits):
    keys_128bits = ""
    for index in pc2_table:
        keys_128bits += keys_56bits[index]
    return keys_128bits

def generate_keys(key_64bits):
    round_keys = list() 
    keys_62bits=''
    keys_56bits= apply_PC1(PC1, key_64bits)
    left56, right56 = split128bits_in_half(keys_56bits)
    for i in round_shifts:
        left56 = circular_left_shift(left56, i)
        right56 = circular_left_shift(right56, i)
        subkey = apply_PC2(PC2, (left56+right56))
        round_keys.append(subkey)
    return round_keys

#key_64bits = "00010011001101000101011101111001100110111011110011011111111100010001001100110100010101110111100110011011101111001101111111110001"
#subkeys = generate_keys(key_64bits)
#print("Lista 16 podkluczy: ")
#print("\n".join(subkeys))


def apply_Expansion(expansion_table,bits32):
    """Rozszerza i permutuje"""
    bits48 = ""
    for index in expansion_table:
        bits48 += bits32[index-1]
    return bits48

def XOR(bits1,bits2):
    # ciągi muszą być równej długości
    xor_result = ""
    for index in range(len(bits1)):
        if bits1[index] == bits2[index]: 
            xor_result += '0'
        else:
            xor_result += '1'
    return xor_result

#podział wiadomości na 8-bitowe porcje 32/8=4
def split48bits_in_6bits(XOR_48bits):
    """Podział bloku 128-bitowego na 8-bitowe porcje """
    list_of_6bits = textwrap.wrap(XOR_48bits,8)
    return list_of_6bits

def get_first_and_last_bit(bits6):
    """Pobierz pierwszy i ostatni bit z 8-bitowego łańcucha bitów -> 4wiersze"""
    twobits = bits6[0] + bits6[-1] 
    return twobits

def get_middle_four_bit(bits6):
    """Pobierz środkowe 5 bitów z z 8-bitowego łańcucha bitów nie pobieram jednego bitu"""
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
    """ Dostęp do odpowiedniej wartości odpowiedniego sboxa""" 
    d_first_last = binary_to_decimal(first_last)
    d_middle = binary_to_decimal(middle4)
    sbox_value = SBOX[sboxcount][d_first_last][d_middle]
    return decimal_to_binary(sbox_value)

def apply_Permutation(permutation_table,sboxes_output):
    """ Scalony efekt użycia Sboksów poddawany jest zdefiniowanej permutacji"""
    permuted80bits = ""
    for index in permutation_table:
        permuted80bits += sboxes_output[index]
    return permuted80bits

EXP = [19, 17, 6, 30, 25, 2, 31, 42, 43, 28, 14, 34, 8, 13, 24, 16, 23, 5, 22, 0, 44, 38, 39, 36, 12, 40, 10, 18, 15, 37, 20, 4, 35, 41, 11, 29, 46, 3, 33, 47, 9, 27, 45, 21, 26, 32, 1, 7, 11, 2, 12, 13, 4, 7, 15, 5, 10, 9, 0, 8, 3, 6, 14, 1]

def functionF(pre32bits, key48bits):
    final96bits = ''
    #pre32bits = apply_Expansion(EXPANSION_TABLE,pre32bits)
    pre_XOR = XOR(pre32bits,key48bits)
    list1 = list()
    list1 = split48bits_in_6bits(pre_XOR)
    sbox = 0
    for chunk in list1:
        row = get_first_and_last_bit(chunk)
        column = get_middle_four_bit(chunk)
        result = sbox_lookup(sbox, row, column)
        sbox += 1
        final96bits += result
    finalbits = apply_Expansion(EXP, final96bits)
    return finalbits


#bits32 =    '1111000010101010111100001010101011110000101010101111000010101010'
#key48bits = '1100101100111101100010110000111000010111111101011111110101111111'
#print("Wynik aplikowania F(): ", functionF(bits32, key48bits))



INITIAL_PERMUTATION_TABLE = [111, 1, 92, 116, 40, 51, 126, 65, 59, 48, 29, 13, 90, 28, 76, 115, 34, 39, 87, 114, 58, 43, 12, 10, 98, 67, 105, 21, 110, 31, 69, 123, 4, 72, 91, 107, 95, 22, 64, 30, 56, 68, 88, 27, 53, 52, 37, 18, 46, 89, 78, 93, 100, 86, 5, 26, 25, 3, 122, 63, 60, 75, 36, 32, 57, 8, 9, 35, 103, 61, 119, 118, 47, 99, 112, 104, 81, 42, 121, 16, 101, 79, 62, 7, 97, 17, 127, 109, 80, 66, 83, 74, 15, 108, 77, 0, 94, 113, 124, 24, 2, 23, 45, 125, 33, 120, 82, 50, 14, 6, 106, 55, 11, 54, 44, 19, 71, 49, 117, 41, 38, 96, 20, 73, 85, 102, 70, 84]

def apply_permutation(P_TABLE, PLAINTEXT):
    permutated_M = ""
    for index in P_TABLE:
        permutated_M += PLAINTEXT[int(index)]
    return permutated_M

INVERSE_PERMUTATION_TABLE = [88, 40, 66, 50, 122, 13, 48, 64, 17, 7, 37, 54, 70, 109, 3, 123, 94, 8, 68, 89, 100, 25, 120, 22, 103, 93, 126, 104, 86, 95, 45, 18, 69, 105, 26, 98, 107, 16, 36, 19, 51, 41, 27, 125, 30, 57, 58, 24, 28, 97, 21, 80, 110, 61, 72, 12, 32, 52, 116, 75, 82, 77, 108, 102, 83, 33, 55, 0, 29, 106, 121, 71, 14, 96, 63, 10, 47, 113, 46, 39, 43, 56, 87, 42, 90, 67, 79, 65, 2, 6, 31, 5, 44, 118, 112, 85, 1, 20, 15, 84, 76, 117, 91, 127, 111, 114, 115, 78, 101, 81, 73, 9, 35, 99, 62, 4, 92, 11, 124, 74, 60, 23, 38, 34, 59, 49, 119, 53]


'''key_64bits = "0001001100110100010101110111100110011011101111001101111111110001"
roundkeys = generate_keys(key_64bits)
# Testowa wartości bloków  
R = '1100110000000000110011001111111111001100000000001100110011111111'  
L = '1111000010101010111100001010101011110000101010101111000010101010'

print("Blok wejściowy", L+R)
# Sieć Feistela - uzupełnij kod wg schematu powyżej, użyj podklucza z dowolnej rundy 
def Siec_Feistela_pojedyncza(Left, Right):
    dowolna_runda = 4
    l1 = Right
    r1 = XOR(Left, functionF(Right, roundkeys[dowolna_runda]))
    return l1, r1

def Siec_Feistela_naodwrot(Left, Right):
    dowolna_runda = 4
    r1 = Left
    l1 = XOR(Right, functionF(Left, roundkeys[dowolna_runda]))
    return l1, r1

L, R = Siec_Feistela_pojedyncza(L, R)
print("Blok wyjściowy (szyfrogram)", L+R)
# Wykonaj operacje odwrotne w sieci Feistela - sprawdź czy szyfrowanie się odwróci
L, R = Siec_Feistela_naodwrot(L, R)
print("Blok wyjściowy", L+R)'''


get_bin = lambda x, n: format(x, 'b').zfill(n)

#tablica znaków w tablicę kodów int
def intoIntArray(message: str):
    int_array = []
    mesg_array = list(message) 
    for i in mesg_array:
        int_array.append(ord(i))
    return int_array

#tablica kodów int w tablice znaków 
def intoCharArray(message: []):
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

M = "Attack!!Attack!!"
key = "EagleHasLanded!!!!!" 

plaintext = intListToBinStr(intoIntArray(M)) 
print("Plaintext(128 bits):", plaintext[:128])
binary_key = intListToBinStr(intoIntArray(key)) 
print("Key (only 128 bits):", binary_key[:128])
roundKeys = generate_keys(binary_key)

def DES_encrypt(message,key):
    cipher = ""
    IP = apply_permutation(INITIAL_PERMUTATION_TABLE, message)
    L, R = split128bits_in_half(IP)
    for i in range(16):
        L, R = Siec_Feistela(L, R, roundKeys, i)
    both = R + L
    cipher = apply_permutation(INVERSE_PERMUTATION_TABLE, both)
    return cipher
    
def DES_decrypt(message,key):
    cipher = ""
    FP = apply_permutation(INITIAL_PERMUTATION_TABLE, message)
    R, L = split128bits_in_half(FP)
    for i in range(15, -1, -1):
        L, R = Siec_Feistela_reverse(L, R, roundKeys, i)
    both_r = L + R
    cipher = apply_permutation(INVERSE_PERMUTATION_TABLE, both_r)
    return cipher    
    

ciphertext = DES_encrypt(plaintext, binary_key[:128])
print("Ciphertext:         ", ciphertext)
encrypted = DES_decrypt(ciphertext, binary_key[:128])
print("Encrypted message:  ", encrypted)
print(XOR(plaintext, encrypted))