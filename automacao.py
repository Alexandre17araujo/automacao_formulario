import pyautogui
import subprocess
from time import sleep
import pandas as pd 

link_formulario = 'https://forms.office.com/r/PwS0k9yyqs?origin=lprLink'
lista_nomes = pd.read_excel('lista_contatos.xlsx')

subprocess.run(['google-chrome', link_formulario])
sleep(5)
for i in range(0, 3):
    sleep(0.5)
    pyautogui.write('.')
    pyautogui.press('tab')
sleep(0.5)
pyautogui.press('enter')
sleep(2)
enviar_outra_resposta = pyautogui.locateCenterOnScreen('imagens/enviar_resposta.png', confidence=0.7)
sleep(2)
pyautogui.click(enviar_outra_resposta)

def executar():
    sleep(1)
    for linha in lista_nomes.index:
        sleep(0.5)
        pyautogui.press('tab')
        sleep(0.5)
        pyautogui.press('tab')
        nome = lista_nomes.loc[linha,'Nome']
        empresa = lista_nomes.loc[linha,'Empresa']
        profissao = lista_nomes.loc[linha,'Profissao']

        sleep(2)
        pyautogui.write(nome)
        pyautogui.press('tab')
        sleep(0.2)
        pyautogui.write(empresa)
        pyautogui.press('tab')
        sleep(0.2)
        pyautogui.write(profissao)
        pyautogui.press('tab')
        sleep(0.2)
        pyautogui.press('enter')
        sleep(2)
        enviar_outra_resposta = pyautogui.locateCenterOnScreen('imagens/enviar_resposta.png', confidence=0.7)
        sleep(1)
        pyautogui.click(enviar_outra_resposta)

if __name__ == '__main__':
    executar()


#    try:
#        subprocess.run(['google-chrome', link_formulario])
#    except FileNotFoundError:
#        print('O software não está instalado ou não foi encontrado!')
#    except subprocess.CalledProcessError as e:
#        print(f'O comando foi executado mas ocorreu um erro {e}')
