n1, n2, n3, n4 = input().split(" ")

N1 = float(n1)
N2 = float(n2)
N3 = float(n3)
N4 = float(n4)

nota_exame = 0.0
MEDIA = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10

print('Media: %.1f' %MEDIA)

if(MEDIA >= 7.0):
    print("Aluno aprovado.")

if(MEDIA < 5.0):
    print("Aluno reprovado.")

if(MEDIA >= 5.0 and MEDIA <= 6.9):
    print("Aluno em exame.")
    nota_exame = float(input())
    print("Nota do exame: %.1f" %nota_exame)
    MEDIA = (MEDIA + nota_exame)/2
    
    if(MEDIA >= 5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print('Media final: %.1f' %MEDIA)