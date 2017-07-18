# -*- coding: utf-8 -*-
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from gochatbot import GoChatBot

reload(sys)
sys.setdefaultencoding('utf-8')

#reload(sys)
#sys.setdefaultencoding('utf-8')

browser = webdriver.Firefox(executable_path=r'C:\Users\Lucas\estudos\chatter bot\geckodriver.exe')
browser.get('http://facebook.com')
global resp
resp = ''
goChatBot = GoChatBot()

# Nome de pessoas para adicionar

# peoples = [
#     "Gabriel",
#     "Lucas",
#     "Vinicius"
# ]

def start():
    logar("eoy03770@oalsp.com", "gotransa123")
    chamarPessoa('Rodriguinho Santos')

def logar(usuario, senha):
    txtEmail = browser.find_element_by_id('email')
    txtEmail.send_keys(usuario)

    txtSenha = browser.find_element_by_id('pass')
    txtSenha.send_keys(senha)

    btnEntrar = browser.find_element_by_id('loginbutton')
    btnEntrar.submit()

def chamarPessoa(nome):
    delay = 3 # seconds

    time.sleep(8)
    pessoa = browser.find_elements_by_class_name('_58al')
    
    # Preenche o nome da pessoa
    pessoa[0].send_keys(nome)
    time.sleep(delay)
    pessoa[0].send_keys(Keys.ENTER)
    time.sleep(delay)

start()

# Conversando com as pessoas
while(True):
    try:
        delay = 3
        msgs = browser.find_elements_by_class_name('_4tdt')
        if len(msgs) == 0:
            resp = 'ois.!'
            
            actions = ActionChains(browser)
            actions.send_keys(resp.decode('utf-8'))
            time.sleep(delay)
            actions.send_keys(Keys.ENTER)

            actions.perform()
            actions.reset_actions()
        else:
            finalMsg = msgs[len(msgs) - 1]
                
            if(resp == '' or finalMsg.text != resp or resp in finalMsg.text  and finalMsg.text != ''):
                                
                response_bot = goChatBot.GetAnswer(finalMsg.text)
                resp = response_bot.text
                
                actions = ActionChains(browser)
                actions.send_keys(resp.decode('utf-8'))
                time.sleep(delay)
                actions.send_keys(Keys.ENTER)

                actions.perform()
                actions.reset_actions()
        #time.sleep(30)
    except Exception as e:
        print(e)

browser.close()


