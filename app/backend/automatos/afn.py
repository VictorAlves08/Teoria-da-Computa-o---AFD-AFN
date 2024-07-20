# from automatos import AutomatoABC
# from typing import List, Dict

# class AFN(AutomatoABC):

#     def __init__(self, 
#         states: List[str], 
#         alphabet: List[str], 
#         initial_state: str, 
#         final_states: List[str], 
#         transitions: Dict[str, Dict[str, List[str]]]
#     ):
#         super().__init__(states, alphabet, initial_state, final_states, transitions)
#         self.states = states
#         self.alphabet = alphabet
#         self.initial_state = initial_state
#         self.final_states = final_states
#         self.transitions = transitions
#         self.current_states = [initial_state]  # AFN pode estar em múltiplos estados ao mesmo tempo
    
#     def run(self, input_string: str) -> bool:
#         self.set_current_state(self.get_initial_state())
#         for symbol in input_string:
#             self.set_current_transition({
#                 'state': self.get_current_state(),
#                 'symbol': symbol
#             })
#             next_states = self.get_next_states(symbol)
#             if not next_states:
#                 return False  # Transição inválida
#             self.set_current_state(next_states)
#         return any(state in self.get_final_states() for state in self.get_current_state())
    
#     def get_next_state(self, symbol: str) -> List[str]:
#         return self.get_transitions().get(self.get_current_state(), {}).get(symbol, [])

#     def get_next_states(self, symbol: str) -> List[str]:
#         next_states = []
#         for state in self.get_current_state():
#             next_states.extend(self.get_transitions().get(state, {}).get(symbol, []))
#         return next_states

#     # Implementações dos métodos abstratos
#     def get_alphabet(self) -> List[str]:
#         return self.alphabet

#     def get_current_state(self) -> List[str]:
#         return self.current_states

#     def get_final_states(self) -> List[str]:
#         return self.final_states

#     def get_initial_state(self) -> str:
#         return self.initial_state

#     def get_states(self) -> List[str]:
#         return self.states

#     def get_transitions(self) -> Dict[str, Dict[str, List[str]]]:
#         return self.transitions

#     def set_current_state(self, states: List[str]):
#         self.current_states = states

#     def set_current_transition(self, transition: Dict[str, str]):
#         self.current_transition = transition

# # Exemplo de uso
# if __name__ == "__main__":
#     states = ["q0", "q1", "q2"]
#     alphabet = ["a", "b"]
#     initial_state = "q0"
#     final_states = ["q2"]
#     transitions = {
#         "q0": {"a": ["q1"], "b": ["q0"]},
#         "q1": {"a": ["q2"], "b": ["q1"]},
#         "q2": {"a": ["q2"], "b": ["q2"]}
#     }
    
#     afn = AFN(states, alphabet, initial_state, final_states, transitions)
    
#     input_string = "aab"
#     print(f"A palavra '{input_string}' foi {'aceita' if afn.run(input_string) else 'rejeitada'} pelo AFN.")


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
        self.current_states = [initial_state]  # AFN pode estar em múltiplos estados ao mesmo tempo

    def run(self, input_string: str) -> bool:
        self.set_current_state([self.get_initial_state()])
        for symbol in input_string:
            self.set_current_transition({
                'state': self.get_current_state(),
                'symbol': symbol
            })
            next_states = self.get_next_states(symbol)
            if not next_states:
                return False  # Transição inválida
            self.set_current_state(next_states)
        return any(state in self.get_final_states() for state in self.get_current_state())
    
    def get_next_states(self, symbol: str) -> List[str]:
        next_states = []
        for state in self.get_current_state():
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

    
