#Importando as bibliotecas
from selenium.webdriver import Chrome
from time import sleep
import pandas as pd

#Armazanando a url do site numa variavel
url = 'https://www.todamateria.com.br/tabela-periodica/'

#inicializando o chrome driver
driver = Chrome('C:/Users/user/Drivers_Browsers/Driver_Chrome/chromedriver.exe')

#Abrindo o navegador e acessando o site
driver.get(url)

#Variaveis
elementos = []
simbolos = []
massas = []
n_atomicos = []

#Aqui vamos começar a interagir com a tabela do site
i = 1 
while i <= 118: #A tabela periódica contém 118 elementos, então vamos percorrer por cada um deles
	
	#Aqui nós vamos simular um click no elemento procurado
	#Vendo o código html da pagina, vi que todos os elementos tinham um id bem parecido
	#A estrutura era "element_(numero atomico)"
	#Por conta disso usei o valor da variavel i para percorrer por cada um
	#Exemplo:Quando o valor dentro de i for 3, ele va click no elemento que tem id "element_3"
	elemento = driver.find_element_by_id(f'element_{i}')
	elemento.click()
	#Um sleep para dar tempo de carregar os outros elementos da pagina
	sleep(2)

	#Aqui vamos pegar cada informação, como nome do elemento, simbolo, massa atomica e numero atomico
	#Cada informação está dentro de uma div com nomes de classes diferentes
	#Então eu pego cada coisa separadamente
	elemento = driver.find_element_by_class_name('symbol_name')
	simbolo = driver.find_element_by_class_name('element_symbol')
	massa = driver.find_element_by_class_name('element_hover_details_3')
	n_atomico = driver.find_element_by_class_name('element_hover_details_1')
	sleep(1)

	#Aqui a gente coloca cada informação pega a acima e coloca em uma determinada lista
	#Para ficar bem dividido
	elementos.append(elemento.text)
	simbolos.append(simbolo.text)
	massas.append(massa.text)
	n_atomicos.append(n_atomico.text)

	#Incremento no valor de i
	i+=1
	
	

#Juntar todos as listas
juncao = {'elementos':elementos,'simbolos':simbolos,'massas':massas,'numero atomico':n_atomicos}

#Passando o dicionario para um DataFrame pandas 
data = pd.DataFrame(juncao)

#Salvando com arquivo csv
data.to_csv('tabela-periodica.csv')

#Fechando o navegador
driver.close()