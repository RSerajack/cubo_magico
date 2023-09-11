#import kociemba

def UpperFace(FR):
    if FR == ('BW' or 'WG' or 'GY' or 'YB'): return 'R'
    if FR == ('BO' or 'OG' or 'GR' or 'RB'): return 'W'
    if FR == ('WB' or 'BY' or 'YG' or 'GW'): return 'O'
    if FR == ('RW' or 'WO' or 'OY' or 'YR'): return 'G'
    if FR == ('BR' or 'RG' or 'GO' or 'OB'): return 'Y'
    else: return 'B'

def converte_face(face, conversao):
    for i in range(3):
        for j in range(3):
            face[i][j] = conversao[face[i][j]]


cores = ['W', 'R', 'Y', 'O', 'B', 'G']
cores_opostas = { 'W':'Y', 'R':'O', 'B':'G', 'Y':'W', 'O':'R', 'G':'B'}
#cores_ad = {'W':['G', 'R', 'B', 'O'], 'R':['G', 'Y', 'B', 'W'], 'B':['Y', 'R', 'W', 'O'], 'Y':['G', 'R', 'B', 'O'], 'O':['G', 'Y', 'B', 'W'], 'G':['Y', 'R', 'W', 'O']}

#recebendo matriz de cores
face_U = [
    ['Y', 'G', 'O'],
    ['R', 'G', 'W'],
    ['G', 'R', 'R']
]

face_R = [
    ['B', 'B', 'B'],
    ['Y', 'W', 'W'],
    ['O', 'Y', 'G']
]

face_F = [
    ['Y', 'B', 'Y'],
    ['O', 'R', 'G'],
    ['G', 'W', 'W']
]

face_D = [
    ['O', 'O', 'B'],
    ['B', 'B', 'R'],
    ['R', 'O', 'R']
]

face_L = [
    ['G', 'W', 'O'],
    ['G', 'Y', 'B'],
    ['B', 'Y', 'W']
]

face_B = [
    ['Y', 'O', 'R'],
    ['G', 'O', 'R'],
    ['W', 'Y', 'W']
]

F = face_F[1][1]
R = face_R[1][1]
B = cores_opostas[F]
L = cores_opostas[R]

#cores_conhecidas = [F, R, B, L]

U = None
D = None

FR = f'{F}{R}'

U = UpperFace(FR)

D = cores_opostas[U]

print(f'U : {U} | R : {R} | F : {F} | D : {D} | L : {L} | B : {B}')

conversao = { U:'U', R:'R', F:'F', D:'D', L:'L', B:'B'}

converte_face(face_R, conversao)
converte_face(face_F, conversao)

for linha in face_F:
    print(linha)



