# Importando bibliotecas
import requests
from bs4 import BeautifulSoup
import pandas as pd

# url do site
url = 'https://pokemondb.net/pokedex/game/firered-leafgreen'

# Solicitando informações da fonte do site 
site = requests.get(url)

#pegando o codigo html do site
soup = BeautifulSoup(site.text, 'html.parser')


# pegando todas as strings dentro das div com a classe 'infocard'
# essas são as divs que armazenam as informações dos pokemons
strings = []
for pokemon in soup.find_all('div', attrs={'class':'infocard'}):
	strings.append(pokemon.text)
# resultado:['#001 Bulbasaur Grass · Poison', '#002 Ivysaur Grass · Poison']

informations = []
# Agora queremos dividir cada informação dentro de cada elemento de strings
# ex:['#001', 'Bulbasaur', 'Grass', '·', 'Poison'], ['#002', 'Ivysaur', 'Grass', '·', 'Poison']]
for info in strings:
	informations.append(info.split(' '))


# Com tudo separado, temos somente um problema, o '·' está contando com um valor dentro da lista
# Pra resolver isso eu pensei na seguinte solução:
# Só tinha '·' os pokemons que tem dois tipos, pois o ponto era o divisor dos tipos
# Com essa conclusão, percebi que só teria o ponto as listas com o tamanho maior de 3
# E sempre o  '·' estaria ocupando a posição de índice 3
# E aproveitando, eu juntei os tipos do pokemon para ser somente uma string  
for i in informations:
	if len(i) > 3:
		i.pop(3)
		i[2] = f'{i[2]} & {i[-1]}'
		i.pop(-1)
# Resultado: ['#001', 'Bulbasaur', 'Grass & Poison'], ['#002', 'Ivysaur', 'Grass & Poison']]


# Depois de ajeitar tudo, agora vamos colocar todas as informações dentro de um DataFrame Pandas

# Fiz três listas para armazenar as informações
numero = []
pokemons = []
tipo = []
for c in informations:
	numero.append(c[0])
	pokemons.append(c[1])
	tipo.append(c[-1])

# e fiz um dicionário para armazenar tudo organizado
pokedex = { 'No':numero, 
			'pokemons':pokemons,
			'tipo':tipo}

# Por fim fiz DataFrame e salvei como um arquivo .csv
data = pd.DataFrame(pokedex)

data.to_csv('pokedex.csv')
