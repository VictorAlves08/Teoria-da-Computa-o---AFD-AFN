import pytest
from app.backend.automatos.afd import AFD

@pytest.fixture
def afd():
    states = ['q0', 'q1', 'q2']
    alphabet = ['a', 'b']
    initial_state = 'q0'
    final_states = ['q2']
    transitions = {
        'q0': {'a': 'q1', 'b': 'q0'},
        'q1': {'a': 'q2', 'b': 'q1'},
        'q2': {'a': 'q2', 'b': 'q2'}
    }
    return AFD(states, alphabet, initial_state, final_states, transitions)

class TestAFD:

    def test_initialization(self):
        estados = ['q0', 'q1', 'q2']
        alfabeto = ['a', 'b']
        transicoes = {
            'q0': {'a': 'q1', 'b': 'q0'},
            'q1': {'a': 'q2', 'b': 'q1'},
            'q2': {'a': 'q2', 'b': 'q2'}
        }
        estado_inicial = 'q0'
        estados_aceitacao = ['q2']
        automato = AFD(estados, alfabeto, estado_inicial, estados_aceitacao, transicoes)
        assert automato.get_states() == estados
        assert automato.get_alphabet() == alfabeto
        assert automato.get_transitions() == transicoes
        assert automato.get_initial_state() == estado_inicial
        assert automato.get_final_states() == estados_aceitacao

    def test_accepts(self, afd):
        assert afd.accepts("aab") == True
        assert afd.accepts("aaa") == True
        assert afd.accepts("abb") == False
        assert afd.accepts("bba") == False

    def test_run(self, afd):
        assert afd.run("aab") == True
        assert afd.run("aaa") == True
        assert afd.run("abb") == False
        assert afd.run("bba") == False

    def test_get_next_states(self, afd):
        afd.set_current_state('q0')
        assert afd.get_next_states('a') == 'q1'
        assert afd.get_next_states('b') == 'q0'
        
        afd.set_current_state('q1')
        assert afd.get_next_states('a') == 'q2'
        assert afd.get_next_states('b') == 'q1'

        afd.set_current_state('q2')
        assert afd.get_next_states('a') == 'q2'
        assert afd.get_next_states('b') == 'q2'


