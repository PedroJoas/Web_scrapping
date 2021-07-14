import requests
from bs4 import BeautifulSoup
import pandas as pd

#url do site
url = 'https://tecnoblog.net/387680/10-melhores-animes-segundo-a-critica-crunchyroll-netflix/'

# Solicitando informações da fonte do site 
site = requests.get(url)

##pegando o codigo html do site
soup = BeautifulSoup(site.text, 'html.parser')

#Vendo o codigo html do site, pude perceber que todos os nome de anime estao dentro de h4
# E por sorte, a plataforma e a nota estão juntos com o titulo
#ex:<h4>Fullmetal Alchemist Brotherhood (Crunchyroll e Netflix) – Nota 9.22</h4>
# Porém tinha mais coisa dentro de h4, então eu peguei somente as 10 primeiras ocorrências
titulos = []
for titulo in soup.find_all('h4')[:10]:
	titulos.append(titulo.text)
#Resultado:['Fullmetal Alchemist Brotherhood (Crunchyroll Netflix ) – Nota 9.22']	

# Agora quero dividir as informações em nome,plataforma e nota
#Primeiro vou deixar nome e plataforma junto e dividir somente a nota

divisao = []
for info in titulos:
	divisao.append(info.split(' – Nota ')) #Como eu queria somente o valor real da nota, eu separei dessa forma
#Resultado:['Fullmetal Alchemist Brotherhood (Crunchyroll e Netflix)', '9.22']

# Agora vamos armazenar os valores de nota dentro de uam variavel
nota = []
informacoes = []
for n in divisao:
	nota.append(n[-1])
	n.pop(-1)
	#Ainda dentro do loop, vamos dividir as informações nome e plataforma
	#Percebi que o que estava dividindo era um parênteses abrindo
	informacoes.append(n[0].split('('))
	#Resultado: ['Fullmetal Alchemist Brotherhood','Crunchyroll e Netflix)']

#Agora vamos armazenar as informações restantes em listas
anime = []
plataforma = []
for i in informacoes:
	anime.append(i[0])
	#Aqui tivemos que usar o replace, pois ainda restava um ')' no final
	#E isso poderia atrapalhar caso fossemos usar esse dataframe para análises
	plataforma.append(i[-1].replace(')', ''))

#Por fim colocamos as informações dentro de um dicionario e depois salvamos como arquivo .csv
animes = {'animes':anime, 'plataforma':plataforma,'nota':nota}

data = pd.DataFrame(animes)
data.to_csv('animes.csv')






