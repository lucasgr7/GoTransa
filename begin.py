import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
from gochatbot import GoChatBot

reload(sys)
sys.setdefaultencoding('utf8')

#reload(sys)
#sys.setdefaultencoding('utf-8')

browser = webdriver.Firefox(executable_path=r'C:\GoTransa\geckodriver.exe')
browser.get('http://facebook.com')

# Nome de pessoas para adicionar

# peoples = [
#     "Gabriel",
#     "Lucas",
#     "Vinicius"
# ]

def start():
    logar("eoy03770@oalsp.com", "gotransa123")
    chamarPessoa('Moises Mendon')

def logar(usuario, senha):
    txtEmail = browser.find_element_by_id('email')
    txtEmail.send_keys(usuario)

    txtSenha = browser.find_element_by_id('pass')
    txtSenha.send_keys(senha)

    btnEntrar = browser.find_element_by_id('loginbutton')
    btnEntrar.submit()

def chamarPessoa(nome):
    delay = 3 # seconds

    time.sleep(delay)
    pessoa = browser.find_elements_by_class_name('_58al')
    
    # Preenche o nome da pessoa
    pessoa[1].send_keys(nome)
    time.sleep(delay)
    pessoa[1].send_keys(Keys.ENTER)
    time.sleep(delay)

    # Primeira Vez
    # txtChat = browser.find_elements_by_class_name('_1mf')
    # time.sleep(delay)

    # txtChat[0].send_keys('Oi')
    # time.sleep(delay)
    # txtChat[0].send_keys(Keys.ENTER)
    # time.sleep(delay)

    #actions = ActionChains(browser)
    goChatBot = GoChatBot()
    resp = None

    # Conversando com as pessoas
    while(True):
        
        try:
            msgs = browser.find_elements_by_class_name('_4tdt')
            finalMsg = msgs[len(msgs) - 1]
                
            if(resp == None or finalMsg.text != resp.text):
                                
                resp = goChatBot.GetAnswer(finalMsg.text)
                print(resp)
                
                actions = ActionChains(browser)
                actions.send_keys(resp.text.decode('utf-8'))
                time.sleep(delay)
                actions.send_keys(Keys.ENTER)

                actions.perform()
                actions.reset_actions()

        except Exception:
            print(Exception)

    browser.close()

start()

