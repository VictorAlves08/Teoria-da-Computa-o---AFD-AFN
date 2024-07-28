import pytest
from app.backend.automatos.afn import AFN
from app.backend.automatos.afd import AFD
from app.backend.automatos.operations import Operations

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

@pytest.fixture
def afd():
    afd_states = ['q0', 'q1', 'q2']
    afd_alphabet = ['a', 'b']
    afd_initial_state = 'q0'
    afd_final_states = ['q2']
    afd_transitions = {
        'q0': {'a': 'q1', 'b': 'q0'},
        'q1': {'a': 'q2', 'b': 'q1'},
        'q2': {'a': 'q2', 'b': 'q2'}
    }
    return AFD(afd_states, afd_alphabet, afd_initial_state, afd_final_states, afd_transitions)


class TestOperations:

    def test_minimize_afd(self, afd):
        minimized_afd = Operations.minimize_afd(afd)
        assert isinstance(minimized_afd, AFD)
        assert len(minimized_afd.get_states()) <= len(afd.get_states())

    def test_afd_to_afn(self, afd):
        afn = Operations.afd_to_afn(afd)
        assert isinstance(afn, AFN)
        assert 'q0' in afn.get_states()
        assert 'q2' in afn.get_final_states()
        assert afn.get_transitions()['q0']['a'] == ['q1']

    def test_check_equivalence(self, afd):
        minimized_afd = Operations.minimize_afd(afd)
        words = ['a', 'aa', 'ab', 'b']
        assert Operations.check_equivalence(afd, minimized_afd, words)

    def test_parse_transitions(self):
        transitions_input = """
        q0,a=q0|q1
        q0,b=q0
        q1,b=q2
        """
        expected_transitions = {
            'q0': {'a': ['q0', 'q1'], 'b': 'q0'},
            'q1': {'b': 'q2'}
        }
        parsed_transitions = Operations.parse_transitions(transitions_input)
        assert parsed_transitions == expected_transitions
