# crie uma funcao que calcule a nota a media de 3 notas em seguida
# verifique se ele esta aprovado ou reprovado para notas acima de 7

def nota():
    n1 = float(input("Digite a primeira nota :"))
    n2 = float(input("Digite a segunda nota :"))
    n3 = float(input("Digite a terceira nota :"))
    media = (n1 + n2 + n3)/3
    print(media)
    if media <= 7:
        print('Aprovado')
    else:
        print('Reprovado')
nota()
    
