import pyautogui
from time import sleep

# 1 - Forma de clicar no item na tela.
#img = pyautogui.locateCenterOnScreen('tela.png')
#pyautogui.click(img.x, img.y)


# 2 - Forma de clicar no item em loop

#encontrar = 'sim'
#while 'sim' in encontrar:
#    try:
#        img = pyautogui.locateCenterOnScreen('tela.png')
#        pyautogui.click(img.x, img.y)
#        encontrar = 'nao'
#        print('Encontrado')
#    except:
#        
#        print('Não encontrei') 


# 3 - Forma de clicar no item em loop.

#encontrar = 'sim'
#
#while 'sim' in encontrar:
#    try:
#        img = pyautogui.locateCenterOnScreen('imagens/resposta.png')
#        pyautogui.click(img.x, img.y)
#        print('Encontrei')
#        sleep(0.5)
#    except:
#        sleep(0.5)
#        print('Não encontrei')
        

# 4 - Forma dee clicar no item da imagem

## Cria uma lista armazenando os valores para todas as vezes em que achar o mesmo 
## elemento que está dentro da imagem que, está armazenada em nossa máquina. 
posicoes_encontradas = list(pyautogui.locateAllOnScreen('imagens/inserir.png'))

## Calcular os valores para que seja capiturado o centro do item encontrado. "Isso é de apenas um item".
x_center = posicoes_encontradas[0].left + posicoes_encontradas[0].width / 2
y_center = posicoes_encontradas[0].top + posicoes_encontradas[0].height / 2
resultado = f'x={x_center}, y={y_center}' 
pyautogui.click(x=532.0, y=389.5)    

