from typing import List, Dict
from app.backend.abstract.automatos import AutomatoABC

class AFD(AutomatoABC):
    def __init__(self,
                 states: List[str],
                 alphabet: List[str],
                 initial_state: str,
                 final_states: List[str],
                 transitions: Dict[str, Dict[str, str]]
                 ):
        self.states = states
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions
        self.current_state = initial_state

    def accepts(self, word: str) -> bool:
        current_state = self.initial_state
        for symbol in word:
            if symbol not in self.alphabet:
                return False  # Símbolo não reconhecido
            if current_state in self.transitions and symbol in self.transitions[current_state]:
                current_state = self.transitions[current_state][symbol]
            else:
                return False  # Transição inválida
        return current_state in self.final_states

    def run(self, input_string: str) -> bool:
        self.current_state = self.initial_state
        for symbol in input_string:
            next_state = self.get_next_states(symbol)
            if not next_state:
                return False  # Transição inválida
            self.current_state = next_state
        return self.current_state in self.final_states

    def get_next_states(self, symbol: str) -> str:
        return self.transitions.get(self.current_state, {}).get(symbol, None)

    def get_transitions(self) -> Dict[str, Dict[str, str]]:
        return self.transitions

    def get_states(self) -> List[str]:
        return self.states

    def get_alphabet(self) -> List[str]:
        return self.alphabet

    def get_initial_state(self) -> str:
        return self.initial_state

    def get_final_states(self) -> List[str]:
        return self.final_states

    def get_current_state(self) -> str:
        return self.current_state

    def set_current_state(self, state: str):
        self.current_state = state

    def set_current_transition(self, transition: Dict[str, str]):
        self.current_transition = transition
