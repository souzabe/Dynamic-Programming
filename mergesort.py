
'''
Defina uma função merge que faz o seguinte:
    Dadas duas listas ordenadas lista1 e L2, 
    retorna uma lista ordenada com todos os números de L1 e L2.

    A função NAO deve usar o método sort do python.

    Em vez disso, faça o seguinte:
       * Crie um indice i1 para a lista L1 e um i2 para L2
       * Inicialize i1 e i2 com 0
       * Compare L1[i1] com L2[i2] e coloque o menor dos dois
       na lista de resposta. Se o menor era L1[i1], aumente i1.
       Caso contrário, aumente i2
       * Assim, L1[i1] e L2[i2] são sempre os menores elementos
       de L1 e L2, e um  deles é sempre o proximo que deve entrar 
       na resposta
       * Continue fazendo isso até adicionar todos os elementos
       de L1 e L2 na resposta
       * Atenção: uma das listas vai acabar primeiro!
'''
def merge(lista1,lista2):
    i1 = 0
    i2 = 0
    resposta = []
    while i1 < len(lista1) and i2 < len(lista2):
        if lista1[i1] < lista2[i2]:
            resposta.append(lista1[i1])
            i1 += 1
        elif lista1[i1] >= lista2[i2]:
            resposta.append(lista2[i2])
            i2 += 1
    while i1 < len(lista1):
        resposta.append(lista1[i1])
        i1 += 1
    while i2 < len(lista2):
        resposta.append(lista2[i2])
        i2+= 1
    return resposta


'''
Defina uma funcao quebra_em_listas
que recebe uma lista e quebra ela em listas de um único elemento.

Ela retorna uma lista com todas essas listas de um elemento

Por exemplo, quebra_em_listas([10,20,30,40]) retorna
[[10],[20],[30],[40]]

Por exemplo, quebra_em_listas([10,20,30,40,50,0]) retorna
[[10],[20],[30],[40],[50],[0]]

Ou seja, a resposta é uma lista com 6 elementos.
O primeiro desses elementos é uma lista,
e essa lista só tem o número 10 dentro dela

'''

def quebra_em_listas(lista):
    return []


'''
Implemente uma função mergeSort, que recebe uma lista e devolve
uma lista ordenada. Nao use a função sort do python

A ideia é a seguinte: comece com uma lista com listinhas de 1 elemento
(como a que você fez em quebra de listas) e vá juntando as listas

Por exemplo, para ordenar [20,1,15,2,30,40,2,3]
Produza
[[20],[1],[15],[2],[30],[40],[2],[3]]
depois tire as primeiras duas listas
[20],[1]
e as junte com o merge
merge([20],[1]) -> dá [1,20])

E coloque de volta
[[15],[2],[30],[40],[2],[3],[1,20]]

E siga fazendo isso
[[30],[40],[2],[3],[1,20],[2,15]]
[[2],[3],[1,20],[2,15],[30,40]]
[[1,20],[2,15],[30,40],[2,3]]
[[30,40],[2,3],[1,2,15,20]]

e continue assim até ter só ter uma lista (a lista ordenada completa)
'''
def mergeSort(lista):
    return lista


import unittest
class TestStringMethods(unittest.TestCase):
   
    
    
    
    def test_01a_merge_inicio(self):
        self.assertEqual(merge([1,2,3],[4,5,6])[:3], [1,2,3])#Olha os 3 primeiros. Retornou mais? ignoro e testo depois
        self.assertEqual(merge([1,3,5],[2,4,6])[:5], [1,2,3,4,5])#Olha os 5 primeiros. Retornou mais? ignoro e testo depois
        self.assertEqual(merge([1,3,5,7],[2,4,6])[:6], [1,2,3,4,5,6])#Olha os 6 primeiros. Retornou mais? ignoro e testo depois
        self.assertEqual(merge([1,5,7],[2,6])[:4], [1,2,5,6])#Olha os 6 primeiros. Retornou mais? ignoro e testo depois

    
    def test_01b_merge(self):
        self.assertEqual(merge([1,2,3],[4,5,6]), [1,2,3,4,5,6])
        self.assertEqual(merge([1,3,5],[2,4,6]), [1,2,3,4,5,6])
        self.assertEqual(merge([1,3,5,7],[2,4,6]), [1,2,3,4,5,6,7])
        self.assertEqual(merge([1,3,5,7],[2,4,6]), [1,2,3,4,5,6,7])


    def test_01c_merge_vazios(self):
        self.assertEqual(merge([1,2,3],[]), [1,2,3])
        self.assertEqual(merge([],[2,4,6]), [2,4,6])
        self.assertEqual(merge([],[]), [])


    def test_03_quebra_em_listas(self):
        self.assertEqual(quebra_em_listas([10,20,30,40,50,0]),[[10],[20],[30],[40],[50],[0]])
        self.assertEqual(quebra_em_listas([10,20,30]),[[10],[20],[30]])
        self.assertEqual(quebra_em_listas([10]),[[10]])
    
    def test_04_mergesort(self):
        self.assertEqual(
          mergeSort([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]), 
          [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50])
        self.assertEqual(
          mergeSort([46,1,18,35,18,9,6,26,47,24,4,29,38,26,30,23,49,5,44,6]), 
          [1, 4, 5, 6, 6, 9, 18, 18, 23, 24, 26, 26, 29, 30, 35, 38, 44, 46, 47, 49])
        self.assertEqual(
          mergeSort( [1,5,15,20,18,30,35,35,38,45,47,48,50]), 
          [1,5,15,18,20,30,35,35,38,45,47,48,50])
    
    
def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


# pode ignorar esse try except, ou deletar sem problemas
try:
    from mergesort_gabarito import *
except:
    pass

runTests()