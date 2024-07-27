from typing import List, Dict
from automatos import AutomatoABC


class AFN(AutomatoABC):
    def __init__(self,
                 states: List[str],
                 alphabet: List[str],
                 initial_state: str,
                 final_states: List[str],
                 transitions: Dict[str, Dict[str, List[str]]]
                 ):
        self.states = states
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions
        # AFN pode estar em múltiplos estados ao mesmo tempo
        self.current_states = [initial_state]

    def accepts(self, word):
        def _dfs(state, word):
            if not word:
                return state in self.final_states
            symbol = word[0]
            next_states = self.transitions.get(state, {}).get(symbol, [])
            for next_state in next_states:
                if _dfs(next_state, word[1:]):
                    return True
            return False

        return _dfs(self.initial_state, word)

    def run(self, input_string: str) -> bool:
        self.current_states = [self.initial_state]
        for symbol in input_string:
            next_states = self.get_next_states(symbol)
            if not next_states:
                return False  # Transição inválida
            self.current_states = next_states
        return any(state in self.final_states for state in self.current_states)

    def get_next_states(self, symbol: str) -> List[str]:
        next_states = []
        for state in self.current_states:
            next_states.extend(self.transitions.get(state, {}).get(symbol, []))
        return next_states

    def get_transitions(self) -> Dict[str, Dict[str, List[str]]]:
        return self.transitions

    def get_states(self) -> List[str]:
        return self.states

    def get_alphabet(self) -> List[str]:
        return self.alphabet

    def get_initial_state(self) -> str:
        return self.initial_state

    def get_final_states(self) -> List[str]:
        return self.final_states

    def get_current_state(self) -> List[str]:
        return self.current_states

    def set_current_state(self, states: List[str]):
        self.current_states = states

    def set_current_transition(self, transition: Dict[str, str]):
        self.current_transition = transition
