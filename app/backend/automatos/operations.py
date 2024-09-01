from app.backend.automatos.afn import AFN
from app.backend.automatos.afd import AFD

from typing import List, Dict, Set, Set, FrozenSet, Union
from graphviz import Digraph


class Operations:
    @staticmethod
    def afn_to_afd(afn: AFN) -> AFD:
        def epsilon_closure(states: Set[str]) -> FrozenSet[str]:
            closure = set(states)
            queue = list(states)

            while queue:
                current_state = queue.pop()
                for origin, transitions in afn.get_transitions().items():
                    if origin == current_state:
                        for symbol, destinations in transitions.items():
                            if symbol == 'e':
                                for destination in destinations if isinstance(destinations, list) else [destinations]:
                                    if destination not in closure:
                                        closure.add(destination)
                                        queue.append(destination)

            return frozenset(closure)

        afd_transitions = []
        state_mapping = {}
        new_states = [epsilon_closure({afn.get_initial_state()})]
        state_mapping[new_states[0]] = "S0"

        while new_states:
            current_state = new_states.pop()

            for symbol in afn.get_alphabet():
                next_state = set()

                for state in current_state:
                    for origin, transitions in afn.get_transitions().items():
                        if origin == state:
                            for label, destinations in transitions.items():
                                if label == symbol:
                                    next_state.update(destinations if isinstance(
                                        destinations, list) else [destinations])

                if next_state:
                    next_state_closure = epsilon_closure(next_state)
                    if next_state_closure not in state_mapping:
                        new_state_name = f"S{len(state_mapping)}"
                        state_mapping[next_state_closure] = new_state_name
                        new_states.append(next_state_closure)

                    afd_transitions.append(
                        [state_mapping[current_state], symbol,
                            state_mapping[next_state_closure]]
                    )

        afd_states = list(state_mapping.values())
        afd_initial_state = state_mapping[epsilon_closure(
            {afn.get_initial_state()})]
        afd_final_states = {
            state_mapping[state] for state in state_mapping if state & set(afn.get_final_states())
        }

        afd_transitions_dict = {}
        for transition in afd_transitions:
            origin, symbol, destination = transition
            if origin not in afd_transitions_dict:
                afd_transitions_dict[origin] = {}
            afd_transitions_dict[origin][symbol] = destination

        return AFD(afd_states, afn.get_alphabet(), afd_initial_state, list(afd_final_states), afd_transitions_dict)

    @staticmethod
    def minimize_afd(afd: AFD) -> AFD:
        P: List[Set[str]] = [set(afd.get_final_states()), set(
            afd.get_states()) - set(afd.get_final_states())]
        W: List[Set[str]] = [set(afd.get_final_states())]

        while W:
            A = W.pop()
            for c in afd.get_alphabet():
                X = {q for q in afd.get_states(
                ) if afd.get_transitions().get(q, {}).get(c) in A}
                for Y in P:
                    inter = X & Y
                    diff = Y - X
                    if inter and diff:
                        P.remove(Y)
                        P.append(inter)
                        P.append(diff)
                        if Y in W:
                            W.remove(Y)
                            W.append(inter)
                            W.append(diff)
                        else:
                            if len(inter) <= len(diff):
                                W.append(inter)
                            else:
                                W.append(diff)

        new_states: List[str] = []
        new_transitions: Dict[str, Dict[str, str]] = {}
        state_map: Dict[str, Set[str]] = {}
        for group in P:
            new_state = ','.join(sorted(group))
            new_states.append(new_state)
            state_map[new_state] = group

        for new_state, group in state_map.items():
            for s in group:
                for c, t in afd.get_transitions().get(s, {}).items():
                    target_state = next(
                        (k for k, v in state_map.items() if t in v), None)
                    if target_state:
                        if new_state not in new_transitions:
                            new_transitions[new_state] = {}
                        new_transitions[new_state][c] = target_state

        initial_state = next(
            (k for k, v in state_map.items() if afd.get_initial_state() in v), None)
        final_states = [k for k, v in state_map.items() if set(
            v) & set(afd.get_final_states())]

        return AFD(new_states, afd.get_alphabet(), initial_state, final_states, new_transitions)

    @staticmethod
    def afd_to_afn(afd: AFD) -> AFN:
        new_transitions: Dict[str, Dict[str, List[str]]] = {}
        for state, transitions in afd.get_transitions().items():
            new_transitions[state] = {symbol: [target]
                                      for symbol, target in transitions.items()}
        return AFN(afd.get_states(), afd.get_alphabet(), afd.get_initial_state(), afd.get_final_states(), new_transitions)

    @staticmethod
    def render_automato(automaton) -> Digraph:
        dot = Digraph()
        dot.attr(rankdir='LR')
        dot.attr('node', shape='circle')

        if isinstance(automaton, AFD):
            dot.attr(label='Tipo: AFD')
        else:
            dot.attr(label='Tipo: AFN')

        dot.node('start', shape='none', width='0', height='0', label='')
        dot.edge('start', automaton.get_initial_state())

        for state in automaton.get_final_states():
            dot.node(state, shape='doublecircle')

        for state, transitions in automaton.get_transitions().items():
            for symbol, targets in transitions.items():
                if isinstance(targets, list):  # AFN
                    for target in targets:
                        dot.edge(state, target, label=symbol)
                else:  # AFD
                    dot.edge(state, targets, label=symbol)

        return dot

    @staticmethod
    def check_equivalence(automaton1, automaton2, test_words: List[str]) -> bool:
        for word in test_words:
            if automaton1.run(word) != automaton2.run(word):
                return False
        return True

    @staticmethod
    def parse_transitions(transitions_input: str) -> Dict[str, Dict[str, Union[List[str], str]]]:
        transitions = {}
        for line in transitions_input.strip().split("\n"):
            state_symbol, result = line.split("=")
            state, symbol = state_symbol.strip().split(',')
            targets = result.strip().split('|')
            if state not in transitions:
                transitions[state] = {}
            transitions[state][symbol] = targets if len(
                targets) > 1 else targets[0]
        return transitions
