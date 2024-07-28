import pytest
from app.backend.automatos.afn import AFN

@pytest.fixture
def afn():
    states = ['q0', 'q1', 'q2']
    alphabet = ['a', 'b']
    initial_state = 'q0'
    final_states = ['q2']
    transitions = {
        'q0': {'a': ['q0', 'q1'], 'b': ['q0']},
        'q1': {'b': ['q2']},
        'q2': {}
    }
    return AFN(states, alphabet, initial_state, final_states, transitions)

class TestAFN:
    
    def test_initialization(self):
        estados = ['q0', 'q1', 'q2']
        alfabeto = ['a', 'b']
        transicoes = {
            'q0': {'a': ['q0', 'q1'], 'b': ['q0']},
            'q1': {'b': ['q2']},
            'q2': {}
        }
        estado_inicial = 'q0'
        estados_aceitacao = ['q2']
        automato = AFN(estados, alfabeto, estado_inicial, estados_aceitacao, transicoes)
        assert automato.get_states() == estados
        assert automato.get_alphabet() == alfabeto
        assert automato.get_transitions() == transicoes
        assert automato.get_initial_state() == estado_inicial
        assert automato.get_final_states() == estados_aceitacao

    def test_accepts(self, afn):
        assert afn.accepts("aab") == True
        assert afn.accepts("aaa") == False
        assert afn.accepts("abb") == False
        assert afn.accepts("bba") == False

    def test_run(self, afn):
        assert afn.run("aab") == True
        assert afn.run("aaa") == False
        assert afn.run("abb") == False
        assert afn.run("bba") == False

    def test_get_next_states(self, afn):
        assert afn.get_next_states('q0', 'a') == ['q0', 'q1']
        assert afn.get_next_states('q0', 'b') == ['q0']
        assert afn.get_next_states('q1', 'b') == ['q2']
        assert afn.get_next_states('q2', 'a') == []

