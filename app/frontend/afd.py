# # import sys
# # import os
# # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
# from automatos import AutomatoABC
# from typing import List, Dict

# class AFD(AutomatoABC):

#     def __init__(self, 
#         states: List[str], 
#         alphabet: List[str], 
#         initial_state: str, 
#         final_states: List[str], 
#         transitions: Dict[str, Dict[str, str]]
#     ):
#         super().__init__(states, alphabet, initial_state, final_states, transitions)
#         self.states = states
#         self.alphabet = alphabet
#         self.initial_state = initial_state
#         self.final_states = final_states
#         self.transitions = transitions
#         self.current_state = initial_state
    
#     def run(self, input_string: str) -> bool:
#         self.set_current_state(self.get_initial_state())
#         for symbol in input_string:
#             self.set_current_transition({
#                 'state': self.get_current_state(),
#                 'symbol': symbol
#             })
#             next_state = self.get_next_state(symbol)
#             if next_state is None:
#                 return False  # Transição inválida
#             self.set_current_state(next_state)
#         return self.get_current_state() in self.get_final_states()
    
#     def convert_for_afn(self) -> Dict[str, Dict[str, List[str]]]:
#         afn_transitions = {}
#         for state, transitions in self.get_transitions().items():
#             afn_transitions[state] = {}
#             for symbol, next_state in transitions.items():
#                 if symbol not in afn_transitions[state]:
#                     afn_transitions[state][symbol] = []
#                 afn_transitions[state][symbol].append(next_state)
#         return afn_transitions

#     def get_next_state(self, symbol: str) -> str:
#         return self.get_transitions().get(self.get_current_state(), {}).get(symbol)

#     # Implementações dos métodos abstratos
#     def get_alphabet(self) -> List[str]:
#         return self.alphabet

#     def get_current_state(self) -> str:
#         return self.current_state

#     def get_final_states(self) -> List[str]:
#         return self.final_states

#     def get_initial_state(self) -> str:
#         return self.initial_state

#     def get_next_states(self, symbol: str) -> List[str]:
#         next_state = self.get_next_state(symbol)
#         return [next_state] if next_state else []

#     def get_states(self) -> List[str]:
#         return self.states

#     def get_transitions(self) -> Dict[str, Dict[str, str]]:
#         return self.transitions

#     def set_current_state(self, state: str):
#         self.current_state = state

#     def set_current_transition(self, transition: Dict[str, str]):
#         self.current_transition = transition

# # Exemplo de uso
# if __name__ == "__main__":
#     states = ["q0", "q1", "q2"]
#     alphabet = ["a", "b"]
#     initial_state = "q0"
#     final_states = ["q2"]
#     transitions = {
#         "q0": {"a": "q1", "b": "q0"},
#         "q1": {"a": "q2", "b": "q1"},
#         "q2": {"a": "q2", "b": "q2"}
#     }
    
#     afd = AFD(states, alphabet, initial_state, final_states, transitions)
    
#     input_string = "aab"
#     print(f"A palavra '{input_string}' foi {'aceita' if afd.run(input_string) else 'rejeitada'} pelo AFD.")


from typing import List, Dict
from automatos import AutomatoABC

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

    def run(self, input_string: str) -> bool:
        self.set_current_state(self.get_initial_state())
        for symbol in input_string:
            self.set_current_transition({
                'state': self.get_current_state(),
                'symbol': symbol
            })
            next_state = self.get_next_states(symbol)
            if not next_state:
                return False  # Transição inválida
            self.set_current_state(next_state[0])  # AFD tem transições determinísticas
        return self.get_current_state() in self.get_final_states()
    
    def get_next_states(self, symbol: str) -> List[str]:
        next_state = self.transitions.get(self.get_current_state(), {}).get(symbol)
        return [next_state] if next_state else []

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
