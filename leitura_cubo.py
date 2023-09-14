import kociemba

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

#recebendo matriz de cores
face_U = [
    ['R', 'Y', 'O'],
    ['O', 'B', 'O'],
    ['W', 'O', 'O']
]

face_R = [
    ['G', 'G', 'G'],
    ['B', 'W', 'B'],
    ['W', 'W', 'Y']
]

face_F = [
    ['B', 'W', 'Y'],
    ['R', 'O', 'O'],
    ['B', 'Y', 'B']
]

face_D = [
    ['O', 'B', 'O'],
    ['W', 'G', 'B'],
    ['W', 'W', 'R']
]

face_L = [
    ['B', 'Y', 'R'],
    ['R', 'Y', 'Y'],
    ['G', 'R', 'Y']
]

face_B = [
    ['W', 'G', 'Y'],
    ['R', 'R', 'G'],
    ['G', 'G', 'R']
]

F = face_F[1][1]
R = face_R[1][1]
B = cores_opostas[F]
L = cores_opostas[R]

U = None
D = None

FR = f'{F}{R}'

U = UpperFace(FR)

D = cores_opostas[U]

print(f'U : {U} | R : {R} | F : {F} | D : {D} | L : {L} | B : {B}')

conversao = { U:'U', R:'R', F:'F', D:'D', L:'L', B:'B'}

converte_face(face_U, conversao)
converte_face(face_R, conversao)
converte_face(face_F, conversao)
converte_face(face_D, conversao)
converte_face(face_L, conversao)
converte_face(face_B, conversao)

print('------Upper------')
for linha in face_U:
    print(linha)
print('------Right------')
for linha in face_R:
    print(linha)
print('------Front------')
for linha in face_F:
    print(linha)
print('------Down------')
for linha in face_D:
    print(linha)
print('------Left------')
for linha in face_L:
    print(linha)
print('------Back------')
for linha in face_B:
    print(linha)
print('----------------')

cadeia = f'{face_U[0][0]}{face_U[0][1]}{face_U[0][2]}{face_U[1][0]}{face_U[1][1]}{face_U[1][2]}{face_U[2][0]}{face_U[2][1]}{face_U[2][2]}{face_R[0][0]}{face_R[0][1]}{face_R[0][2]}{face_R[1][0]}{face_R[1][1]}{face_R[1][2]}{face_R[2][0]}{face_R[2][1]}{face_R[2][2]}{face_F[0][0]}{face_F[0][1]}{face_F[0][2]}{face_F[1][0]}{face_F[1][1]}{face_F[1][2]}{face_F[2][0]}{face_F[2][1]}{face_F[2][2]}{face_D[0][0]}{face_D[0][1]}{face_D[0][2]}{face_D[1][0]}{face_D[1][1]}{face_D[1][2]}{face_D[2][0]}{face_D[2][1]}{face_D[2][2]}{face_L[0][0]}{face_L[0][1]}{face_L[0][2]}{face_L[1][0]}{face_L[1][1]}{face_L[1][2]}{face_L[2][0]}{face_L[2][1]}{face_L[2][2]}{face_B[0][0]}{face_B[0][1]}{face_B[0][2]}{face_B[1][0]}{face_B[1][1]}{face_B[1][2]}{face_B[2][0]}{face_B[2][1]}{face_B[2][2]}'

print("String para resolver: ", cadeia)

result = kociemba.solve(cadeia)

#result = "R2 R R D D F B F' L"

comandos = []

for i in range(len(result)-1):
    if result[i+1] == ("'"):
        comandos.append(f'{result[i]}{result[i+1]}')
    elif result[i+1] == ("2"):
        comandos.append(f'{result[i]}{result[i]}')
    elif result[i] == "'" or result[i] == "2":
        pass
    elif result[i+1] == ' ':
        comandos.append(result[i])
    else:
        pass

print("Passo a passo: ")

#for e in comandos:
#    print(e)

print(comandos)