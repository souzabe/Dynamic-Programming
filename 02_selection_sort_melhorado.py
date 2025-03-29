'''
Para relembrar o algoritmo 'selection sort' para ordenar uma lista,
acesse
https://visualgo.net/en/sorting

e escolha 'selection sort'

Essencialmente, o que o algoritmo faz é achar o menor elemento 
da lista e colocar na posição 0. Depois achar o segundo
menor e colocar na posição 1, depois o terceiro menor...

Se você entendeu o espírito da coisa, siga para implementar umas funções parciais 
que depois juntaremos pra produzir o selection sort
'''


'''implemente uma funcao troca, 
que recebe uma lista e duas posicoes,
e troca os valores das duas posicoes. 
Por exemplo, troca(['a','b','c'],0,2) deve retornar ['c','b','a']

Se você der uma engalhada, talvez queira ver um python tutor
pra te ajudar

https://pythontutor.com/render.html#code=lista%20%3D%20%5B%22banana%22,%22abacaxi%22,%22maca%22,%22pera%22%5D%0A%0Alista%5B0%5D%20%3D%20lista%5B1%5D%20%23putz,%20perdi%20um%20elemento%0Alista%5B1%5D%20%3D%20lista%5B0%5D%20%23nao%20adianta%20nada%20%3AP%0A%0A%23essa%20troca%20deu%20errado!!%0A%23tentemos%20de%20novo%0A%0Alista%20%3D%20%5B%22banana%22,%22abacaxi%22,%22maca%22,%22pera%22%5D%0A%0Av1%20%3D%20lista%5B1%5D%0Av0%20%3D%20lista%5B0%5D%0Alista%5B1%5D%20%3D%20v0%0Alista%5B0%5D%20%3D%20v1%0A%0A%23essa%20troca%20deu%20certo!%0A%23agora%20volte%20pro%20codigo%20e%20implemente%20uma%20**funcao**%20pra%20isso.%20Uma%20funcao%20que%20%0A%23%20recebe%20os%20indices%20%28pode%20ser%200%20e%201%20como%20acima,%20mas%20tb%20pode%20ser%202%20e%205%29%20e%20troca%0A%23%20os%20valores%20das%20posicoes&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false


'''

def troca(lista,pos1,pos2):
    trocador = lista[pos1]
    lista[pos1] = lista[pos2]
    lista[pos2] = trocador
    return lista

'''
A primeira coisa que o selection sort faz é achar o menor 
elemento da lista. Na função abaixo, vamos tentar fazer isso,
mas sem usar funções do python como o min.

Vamos percorrer a lista usando um for e devolver o menor valor.

Para isso, implementaremos a seguinte ideia:
menor_atual = primeiro_elemento da lista
for elemento in lista:
    se o elemento for menor do que o menor_atual, trocamos

Implemente abaixo a funcao menor(lista), que recebe uma lista de elementos e 
retorna o menor deles
'''

def menor(lista):
    v_menor = lista[0]
    for v in lista:
        if v < v_menor:
            v_menor = v
    return v_menor

'''
Uma coisa que o selection sort tem que fazer é
gerar uma lista de indices. Pra descobrir 
o menor elemento da lista [100,40,23] ele tem que 'achar' o 23, que está
no indice 2 e trocar com o 100, que está no indice 0.

Então ele tem que poder olhar pra essa lista e dizer 'vou consultar
os índices 0,1 e 2'

>>> lista = [10,20,30,40,50]
>>> len(lista)
5
>>> for x in range(len(lista)): print(x)
0
1
2
3
4

Como podemos ver, esse range(5) gerou uma 'lista' [0,1,2,3,4], que pudemos
percorrer com o for

Infelizmente tem aspas nessa 'lista', porque ele gera um objeto
diferente. Mas dá pra ver como lista se você quiser. Pode ignorar 
totalmente esse detalhe

>>> a = range(len(lista))
>>> list(a)
[0,1,2,3,4]

implemente uma função indices_da_lista, que recebe uma lista
e devolve os indices validos para a lista
'''

def indices_da_lista(lista):
    
    i_menor = 0
    for i in range(len(lista)):
        if lista[i] < lista[i_menor]:
            i_menor = i
    return i_menor



'''implemente uma funcao indice_menor, 
que recebe uma lista e devolve o indice do seu menor elemento. 
Se houver mais de um menor elemento, retorna o indice menor.
por exemplo, a=[20,30,10] indice_menor(a) retorna 2, pois a[2]==10'''
def indice_menor(lista):
    return 0

'''
Na real, o selection sort precisa de varias listas de indices

Pra lista [30,20,10,70], ele vai percorrer os indices 0,1,2 e 3 pra achar o menor
depois de colocar o menor na posicao 0, ele percorre de novo, dessa vez só os 1,2 e 3
Depois, percorre mais uma vez, usando só os indices 2 e 3.

Precisamos, então, saber gerar essas listas de indices. Felizmente é fácil

>>> lista = [10,20,30,40,50]
>>> len(lista)
5
>>> for x in range(2,len(lista)): print(x)
... 
2
3
4
>>> list(range(2,len(lista)))
[2, 3, 4]

É só passar um segundo argumento pro range.

range(5) é a 'lista' 0,1,2,3,4
range(9) é a 'lista' 0,1,2,3,4,5,6,7,8
range(2,5) é a 'lista' 2,3,4
range(3,9) é a 'lista' 3,4,5,6,7,8

perceba: range(3,9) *inclui* o 3, mas não o 9
range(3,len(lista)) *inclui* o 3, mas não o 5 (imaginando ainda a nossa
lista de tamanho 5). O que é muito bom, porque o 5 não é um indice válido mesmo,
se a lista tem 5 elementos, seus indices válidos são 0,1,2,3,4

implemente uma função indices_parciais_da_lista, que recebe uma posicao inicial, uma lista
e devolve os indices validos para a lista, começando da posicao inicial

'''

def indices_parciais_da_lista(inicio,lista):
    pass


'''implemente uma funcao indice_menor_a_partir_de, 
que recebe uma lista e um numero de inicio, 
e devolve o indice do menor elemento do inicio para frente. 
Se houver mais de um menor elemento, retorne o indice menor.
por exemplo, a=[10,40,30] indice_menor_a_partir_de(a,0) retorna 0, pois a[0]==10
por exemplo, a=[10,40,30] indice_menor_a_partir_de(a,1) retorna 2, pois a[2]==30'''
def indice_menor_a_partir_de(lista,posicao):
    return 0

'''implemente uma função selectionSort, 
que recebe uma lista e devolve uma lista ordenada. 

NAO USE O METODO lista.sort(). 
ISSO NAO SERA CONSIDERADO UMA SOLUCAO VALIDA.

Selection sort é o algoritmo que percorre a lista, 
acha o menor elemento e coloca na posicao 0. 
Depois, percorre a lista novamente, partindo da posicao 1, 
acha o menor elemento e o coloca na posicao 1, 
e vai fazendo isso até ordenar a lista

Veja: https://visualgo.net/bn/sorting, opcao SEL ou SELECTION SORT
'''
def selectionSort(lista):
    return lista




import unittest

class TestStringMethods(unittest.TestCase):
   
    def test_00_troca(self):
        self.assertEqual(
          troca([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48],5,6), 
          [3,44,38,5,47,36,15,26,27,2,46,4,19,50,48])
        self.assertEqual(
          troca([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48],5,5), 
          [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48])
        self.assertEqual(
          troca([3,44],0,1), 
          [44,3])
        self.assertEqual(
          troca([3],0,0), 
          [3])
        
    def test_01a_menor(self):
        self.assertEqual(
            menor([1,2,3]),
            1)
        self.assertEqual(
            menor([10,2,3]),
            2)
        self.assertEqual(
            menor([10,2,30]),
            2)

    def test_01b_menor(self):
        resultado = menor([-1,-2,-3])
        if resultado != -3:
            self.fail('sua funcao menor está falhando com números negativos\n Será que você inventou um menor=0?')

    def test_02_indices_da_lista(self):
        self.assertTrue(2 in indices_da_lista([10,20,30]))
        self.assertTrue(0 in indices_da_lista([10,20,30])) 
        self.assertTrue(5 in indices_da_lista([10,20,30,40,50,60]))
        self.assertFalse(5 in indices_da_lista([10,20,30,40,50]))
         

    def test_03_indice_menor(self):
        self.assertEqual(
          indice_menor([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]), 
          9)
        self.assertEqual(
          indice_menor([3,44,38,5,47,15,36,26,27,46,4,19,50,48]), 
          0)
        self.assertEqual(
          indice_menor([44,38,5,47,15,36,26,27,46,4,19,50,48]), 
          9)
    
    def test_04_indices_parciais_da_lista(self):
        l1 = [10,20,30]
        l2 = [10,20,30,40,50,60]
        self.assertTrue(
            3 in
            indices_parciais_da_lista(3,l2)
        )
        self.assertFalse(
            2 in
            indices_parciais_da_lista(3,l2)
        )
        self.assertFalse(
            6 in
            indices_parciais_da_lista(3,l2)
        )
        self.assertTrue(
            2 in
            indices_parciais_da_lista(0,l1)
        )
    
    def test_05_indice_menor_a_partir_de(self):
        self.assertEqual(
          indice_menor_a_partir_de([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48],0), 
          9)
        self.assertEqual(
          indice_menor_a_partir_de([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48],9), 
          9)
        self.assertEqual(
          indice_menor_a_partir_de([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48],10), 
          11)
    
    def test_06_selection(self):
        self.assertEqual(
          selectionSort([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]), 
          [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50])
        self.assertEqual(
          selectionSort([46,1,18,35,18,9,6,26,47,24,4,29,38,26,30,23,49,5,44,6]), 
          [1, 4, 5, 6, 6, 9, 18, 18, 23, 24, 26, 26, 29, 30, 35, 38, 44, 46, 47, 49])
        self.assertEqual(
          selectionSort( [1,5,15,20,18,30,35,35,38,45,47,48,50]), 
          [1,5,15,18,20,30,35,35,38,45,47,48,50])
    def test_07_mostra_tempos(self):
        print("\nOk, você passou todos os testes!")
        print("Vamos ver qual o tempo que esse algoritmo leva pra rodar")
        print("Rode o código no terminal (o play do VSCode não funciona!)")
        input("aperte enter para continuar")
        finish()

    




    


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

def indices(lista):
    return list(range(len(lista)))

#esse codigo nao roda a menos que o gabarito tenha sido
#fornecido. Ele é pra eu testar o exercicio, nao
#pra voce usar, pode ignorar ou deletar
try:
    from gabarito_sorts_com_tempos import *
except:
    pass


import time
import random

def gera_lista(n=400):
    print('a lista agora tem '+str(n)+' elementos.')
    print('Se quiser testar novamente os tempos, chame a funcao tempos(n=nova_quantidade) ')
    return [random.randint(1,10*n) for x in range(n)]

def tempos(n=400):
    l = gera_lista(n)
    start = time.process_time()
    for a in range(1,100):
        l1 = l[:]
        l1.sort()
    end = time.process_time()
    print('o python levou: '+str(end-start))
    start = time.process_time()
    for a in range(1,100):
        l1 = l[:]
        selectionSort(l1)
    end = time.process_time()
    print('selectionSort levou: '+str(end-start))

#imprimiria os tempos, mas nao deu muito certo. Os tempos funcionam, vincular com o fim dos testes, nao
def finish():
        print("ok \n")
        print("-----------------------------------------------------------------------------------------------")
        print("Você passou todos os testes")
        print("agora que você terminou todos os testes, podemos rodar o algoritmo e medir o tempo que ele leva")
        tempos(400)
        tempos(800)
        tempos(1600)

runTests()
