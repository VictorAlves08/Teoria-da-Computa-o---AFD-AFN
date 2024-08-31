from typing import List, Dict, Union
from abc import ABC, abstractmethod


class AutomatoABC(ABC):

    @abstractmethod
    def run(self, input_string: str) -> bool:
        pass

    @abstractmethod
    def get_transitions(self) -> Union[Dict[str, Dict[str, str]], Dict[str, Dict[str, List[str]]]]:
        pass

    @abstractmethod
    def get_states(self) -> List[str]:
        pass

    @abstractmethod
    def get_alphabet(self) -> List[str]:
        pass

    @abstractmethod
    def get_initial_state(self) -> str:
        pass

    @abstractmethod
    def get_final_states(self) -> List[str]:
        pass

    @abstractmethod
    def get_current_state(self) -> Union[str, List[str]]:
        pass

    @abstractmethod
    def set_current_state(self, state: Union[str, List[str]]):
        pass

    @abstractmethod
    def get_next_states(self, symbol: str) -> List[str]:
        pass

    @abstractmethod
    def set_current_transition(self, transition: Dict[str, str]):
        pass
