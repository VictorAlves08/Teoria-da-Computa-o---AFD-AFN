from typing import List, Dict, Tuple


class TuringMachine:
    def __init__(self,
                 states: List[str],
                 alphabet: List[str],
                 tape_alphabet: List[str],
                 blank_symbol: str,
                 initial_state: str,
                 final_states: List[str],
                 transitions: Dict[str, Dict[str, Tuple[str, str, str]]]):
        self.states = states
        self.alphabet = alphabet
        self.tape_alphabet = tape_alphabet
        self.blank_symbol = blank_symbol
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions
        self.tape = []
        self.head_position = 0
        self.current_state = initial_state

    def initialize_tape(self, input_string: str):
        self.tape = list(input_string) + [self.blank_symbol]
        self.head_position = 0
        self.current_state = self.initial_state

    def step(self) -> bool:
        if self.current_state in self.final_states:
            return False

        current_symbol = self.tape[self.head_position]
        if current_symbol not in self.transitions[self.current_state]:
            return False

        next_state, write_symbol, move = self.transitions[self.current_state][current_symbol]
        self.tape[self.head_position] = write_symbol
        self.current_state = next_state

        if move == 'R':
            self.head_position += 1
            if self.head_position == len(self.tape):
                self.tape.append(self.blank_symbol)
        elif move == 'L':
            self.head_position = max(0, self.head_position - 1)

        return True

    def run(self, input_string: str) -> bool:
        self.initialize_tape(input_string)

        while self.step():
            pass

        return self.current_state in self.final_states

    def get_tape(self) -> str:
        return ''.join(self.tape).rstrip(self.blank_symbol)
