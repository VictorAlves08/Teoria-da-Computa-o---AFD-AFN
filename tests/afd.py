import unittest
from app.backend.afd import AFD

class TestAutomatoFinito(unittest.TestCase):
    def test_initialization(self):
        estados = {'q0', 'q1'}
        alfabeto = {'a', 'b'}
        transicoes = {'q0': {'a': 'q1'}}
        estado_inicial = 'q0'
        estados_aceitacao = {'q1'}
        automato = AFD(estados, alfabeto, transicoes, estado_inicial, estados_aceitacao)
        self.assertEqual(automato.estados, estados)
        self.assertEqual(automato.alfabeto, alfabeto)
        self.assertEqual(automato.transicoes, transicoes)
        self.assertEqual(automato.estado_inicial, estado_inicial)
        self.assertEqual(automato.estados_aceitacao, estados_aceitacao)

if __name__ == '__main__':
    unittest.main()
