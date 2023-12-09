from selenium import webdriver
from selenium.webdriver import ChromeOptions

options = ChromeOptions

driver = webdriver.Chrome(options=options)


driver.get('https://portalservicos.pucrs.br/TraceGP/indexPopup.jsp')

usuário = '80401031'
senha = 'Lindinho9227'

#Irá encontrar os campos de usuario e senha

campo_usuário = driver.find_element_by_name('txtUsuario')
campo_usuário.send_keys(usuário)

campo_senha = driver.find_element_by_name('pwdSenha')
campo_senha.send_keys(senha)

#Irá procurar o botão de login pelo ID

botao_login = driver.find_element_by_id('botaoAcessarLogin')
botao_login.click()