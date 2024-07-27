from afn import AFN
from afd import AFD
from typing import List, Dict

class Operations:
    def afn_to_afd(afn: AFN) -> AFD:
            new_states = []
            new_transitions = {}
            state_map = {}
            initial_state = tuple([afn.get_initial_state()])
            state_queue = [initial_state]
            final_states = []

            while state_queue:
                current_state = state_queue.pop(0)
                current_state_str = ','.join(current_state)

                if current_state_str not in state_map:
                    state_map[current_state_str] = current_state
                    new_states.append(current_state_str)
                    new_transitions[current_state_str] = {}

                    if any(s in afn.get_final_states() for s in current_state):
                        final_states.append(current_state_str)

                    for symbol in afn.get_alphabet():
                        next_states = set()
                        for state in current_state:
                            next_states.update(afn.get_next_states(symbol))

                        next_state_tuple = tuple(next_states)
                        if next_state_tuple:
                            next_state_str = ','.join(next_state_tuple)
                            new_transitions[current_state_str][symbol] = next_state_str
                            if next_state_tuple not in state_map:
                                state_queue.append(next_state_tuple)

            return AFD(new_states, afn.get_alphabet(), ','.join(initial_state), final_states, new_transitions)


    def check_equivalence(afn, afd, test_words) -> bool:
        for word in test_words:
            if afn.run(word) != afd.run(word):
                return False
        return True

    def minimize_afd(afd: AFD) -> AFD:
        P = [set(afd.get_final_states()), set(afd.get_states()) - set(afd.get_final_states())]
        W = [set(afd.get_final_states())]

        while W:
            A = W.pop()
            for c in afd.get_alphabet():
                X = {q for q in afd.get_states() if afd.get_transitions().get(q, {}).get(c) in A}
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
        new_states = []
        new_transitions = {}
        state_map = {}
        for group in P:
            new_state = ','.join(group)
            new_states.append(new_state)
            state_map[new_state] = group
            for s in group:
                for c, t in afd.get_transitions().get(s, {}).items():
                    target_state = next((k for k, v in state_map.items() if t in v), None)
                    if target_state:
                        if new_state not in new_transitions:
                            new_transitions[new_state] = {}
                        new_transitions[new_state][c] = target_state

        initial_state = next((k for k, v in state_map.items() if afd.get_initial_state() in v), None)
        final_states = [k for k, v in state_map.items() if set(v) & set(afd.get_final_states())]
        
        return AFD(new_states, afd.get_alphabet(), initial_state, final_states, new_transitions)

