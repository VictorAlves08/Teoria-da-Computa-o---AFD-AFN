# # import sys
# # import os
# # import streamlit as st
# # import graphviz

# # # Adiciona o diretório raiz do projeto ao sys.path
# # sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# # from afd import AFD
# # from afn import AFN
# # from operations import afn_to_afd, afd_to_afn, minimize_afd

# # def parse_transitions(transitions_input):
# #     transitions = {}
# #     for line in transitions_input.split("\n"):
# #         line = line.strip()
# #         if not line:
# #             continue  # Ignora linhas vazias

# #         parts = line.split('=')
# #         if len(parts) != 2:
# #             continue  # Ignora linhas que não têm '=' ou têm menos de duas partes

# #         state_symbol, result = parts[0].strip(), parts[1].strip()
# #         if ',' not in state_symbol:
# #             continue  # Ignora se não há vírgula separando estado e símbolo
        
# #         state, symbol = [x.strip() for x in state_symbol.split(',', 1)]
# #         targets = [x.strip() for x in result.split('|')]

# #         if state not in transitions:
# #             transitions[state] = {}
# #         transitions[state][symbol] = targets

# #     return transitions

# # def render_automaton(automaton):
# #     dot = graphviz.Digraph()
# #     dot.attr(rankdir='LR')
# #     automaton_type = 'AFD' if isinstance(automaton, AFD) else 'AFN'
# #     dot.attr(label=f'Tipo de Autômato: {automaton_type}')
# #     for state in automaton.get_states():
# #         shape = 'doublecircle' if state in automaton.get_final_states() else 'circle'
# #         dot.node(state, shape=shape)
# #     dot.node('', shape='none')
# #     dot.edge('', automaton.get_initial_state())
# #     for state, transitions in automaton.get_transitions().items():
# #         for symbol, targets in transitions.items():
# #             for target in targets:
# #                 dot.edge(state, target, label=symbol)
# #     return dot

# # def simulate_automaton(automaton, word):
# #     current_states = {automaton.get_initial_state()}
# #     for symbol in word:
# #         next_states = set()
# #         for state in current_states:
# #             if state in automaton.get_transitions() and symbol in automaton.get_transitions()[state]:
# #                 next_states.update(automaton.get_transitions()[state][symbol])
# #         current_states = next_states
# #         if not current_states:  # Se nenhum estado for alcançável, a palavra é rejeitada
# #             return False
# #     # A palavra é aceita se algum dos estados finais for alcançado
# #     return any(state in automaton.get_final_states() for state in current_states)

# # def check_equivalence(afn, afd, test_words):
# #     for word in test_words:
# #         if simulate_automaton(afn, word) != simulate_automaton(afd, word):
# #             return False
# #     return True

# # st.title("Autômato Finito Determinístico e Não-determinístico")

# # option = st.selectbox(
# #     "Escolha a operação", 
# #     ["Criar AFD", "Criar AFN", "Converter AFN para AFD", "Converter AFD para AFN", "Minimizar AFD", "Verificar Equivalência", "Renderizar Autômato"]
# # )

# # states = st.text_input("Estados (separados por vírgulas)")
# # alphabet = st.text_input("Alfabeto (separados por vírgulas)")
# # initial_state = st.text_input("Estado Inicial")
# # final_states = st.text_input("Estados Finais (separados por vírgulas)")
# # transitions_input = st.text_area("Transições (um por linha, formato: estado,símbolo=estado(s))")
# # test_words_input = st.text_area("Palavras de teste (separadas por vírgulas)")

# # if st.button("Executar"):
# #     states_list = states.split(",")
# #     alphabet_list = alphabet.split(",")
# #     final_states_list = final_states.split(",")
# #     transitions = parse_transitions(transitions_input)
# #     test_words = test_words_input.split(",")

# #     automaton = None
# #     if option == "Criar AFD":
# #         automaton = AFD(states_list, alphabet_list, initial_state, final_states_list, transitions)
# #     elif option == "Criar AFN":
# #         automaton = AFN(states_list, alphabet_list, initial_state, final_states_list, transitions)
# #     elif option == "Converter AFN para AFD":
# #         automaton = afn_to_afd(automaton)
# #     elif option == "Converter AFD para AFN":
# #         automaton = afd_to_afn(automaton)
# #     elif option == "Minimizar AFD":
# #         automaton = minimize_afd(automaton)
# #     elif option == "Verificar Equivalência":
# #         afd = afn_to_afd(automaton)  # Converte novamente para garantir que está usando o AFD mais recente
# #         equivalence = check_equivalence(automaton, afd, test_words)
# #         st.write(f"Os autômatos são {'equivalentes' if equivalence else 'não equivalentes'} para as palavras de teste fornecidas.")

# #     if automaton:
# #         st.graphviz_chart(render_automaton(automaton), use_container_width=True)




# import sys
# import os
# import streamlit as st
# import graphviz

# # Adiciona o diretório raiz do projeto ao sys.path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# from afd import AFD
# from afn import AFN
# from operations import afn_to_afd, afd_to_afn, check_equivalence, minimize_afd

# def parse_transitions(transitions_input):
#     transitions = {}
#     for line in transitions_input.split("\n"):
#         line = line.strip()
#         if not line:
#             continue  # Ignora linhas vazias

#         parts = line.split('=')
#         if len(parts) != 2:
#             continue  # Ignora linhas que não têm '=' ou têm menos de duas partes

#         state_symbol, result = parts[0].strip(), parts[1].strip()
#         if ',' not in state_symbol:
#             continue  # Ignora se não há vírgula separando estado e símbolo
        
#         state, symbol = [x.strip() for x in state_symbol.split(',', 1)]
#         targets = [x.strip() for x in result.split('|')]

#         if state not in transitions:
#             transitions[state] = {}
#         transitions[state][symbol] = targets

#     return transitions

# def render_automaton(automaton):
#     dot = graphviz.Digraph()
#     dot.attr(rankdir='LR')
#     automaton_type = 'AFD' if isinstance(automaton, AFD) else 'AFN'
#     dot.attr(label=f'Tipo de Autômato: {automaton_type}')
#     for state in automaton.get_states():
#         shape = 'doublecircle' if state in automaton.get_final_states() else 'circle'
#         dot.node(state, shape=shape)
#     dot.node('', shape='none')
#     dot.edge('', automaton.get_initial_state())
#     for state, transitions in automaton.get_transitions().items():
#         for symbol, targets in transitions.items():
#             for target in targets:
#                 dot.edge(state, target, label=symbol)
#     return dot

# def simulate_automaton(automaton, word):
#     current_states = {automaton.get_initial_state()}
#     for symbol in word:
#         next_states = set()
#         for state in current_states:
#             if state in automaton.get_transitions() and symbol in automaton.get_transitions()[state]:
#                 next_states.update(automaton.get_transitions()[state][symbol])
#         current_states = next_states
#         if not current_states:  # Se nenhum estado for alcançável, a palavra é rejeitada
#             return False
#     return any(state in automaton.get_final_states() for state in current_states)

# def check_equivalence(afn, afd, test_words):
#     for word in test_words:
#         if simulate_automaton(afn, word) != simulate_automaton(afd, word):
#             return False
#     return True

# st.title("Autômato Finito Determinístico e Não-determinístico")

# st.sidebar.write("## Exemplo de entrada")
# st.sidebar.write("### Estados")
# st.sidebar.write("`q0, q1, q2`")
# st.sidebar.write("### Alfabeto")
# st.sidebar.write("`a, b`")
# st.sidebar.write("### Estado Inicial")
# st.sidebar.write("`q0`")
# st.sidebar.write("### Estados Finais")
# st.sidebar.write("`q2`")
# st.sidebar.write("### Transições")
# st.sidebar.write("```\nq0,a=q1\nq0,b=q0\nq1,a=q2\nq1,b=q1\nq2,a=q2\nq2,b=q2\n```")
# st.sidebar.write("### Palavras de Teste")
# st.sidebar.write("`a, ab, aab, aa`")

# option = st.selectbox(
#     "Escolha a operação", 
#     ["Criar AFD", "Criar AFN", "Converter AFN para AFD", "Converter AFD para AFN", "Minimizar AFD", "Verificar Equivalência", "Renderizar Autômato"]
# )

# states = st.text_input("Estados (separados por vírgulas)")
# alphabet = st.text_input("Alfabeto (separados por vírgulas)")
# initial_state = st.text_input("Estado Inicial")
# final_states = st.text_input("Estados Finais (separados por vírgulas)")
# transitions_input = st.text_area("Transições (um por linha, formato: estado,símbolo=estado(s))")
# test_words_input = st.text_area("Palavras de teste para verificação de equivalência (separadas por vírgulas)")

# if st.button("Executar"):
#     states_list = states.split(",")
#     alphabet_list = alphabet.split(",")
#     final_states_list = final_states.split(",")
#     transitions = parse_transitions(transitions_input)
#     test_words = test_words_input.split(",")

#     automaton = None
#     if option == "Criar AFD":
#         automaton = AFD(states_list, alphabet_list, initial_state, final_states_list, transitions)
#     elif option == "Criar AFN":
#         automaton = AFN(states_list, alphabet_list, initial_state, final_states_list, transitions)
#     elif option == "Converter AFN para AFD":
#         automaton = afn_to_afd(automaton)
#     elif option == "Converter AFD para AFN":
#         automaton = afd_to_afn(automaton)
#     elif option == "Minimizar AFD":
#         automaton = minimize_afd(automaton)
#     elif option == "Verificar Equivalência":
#         afd = afn_to_afd(automaton)  # Converte novamente para garantir que está usando o AFD mais recente
#         equivalence = check_equivalence(automaton, afd, test_words)
#         st.write(f"Os autômatos são {'equivalentes' if equivalence else 'não equivalentes'} para as palavras de teste fornecidas.")

#     if automaton:
#         st.graphviz_chart(render_automaton(automaton), use_container_width=True)



import sys
import os
import streamlit as st
import graphviz

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from afd import AFD
from afn import AFN
from operations import afn_to_afd, afd_to_afn, check_equivalence, minimize_afd

def parse_transitions(transitions_input):
    transitions = {}
    for line in transitions_input.split("\n"):
        line = line.strip()
        if not line:
            continue  # Ignora linhas vazias

        parts = line.split('=')
        if len(parts) != 2:
            continue  # Ignora linhas que não têm '=' ou têm menos de duas partes

        state_symbol, result = parts[0].strip(), parts[1].strip()
        if ',' not in state_symbol:
            continue  # Ignora se não há vírgula separando estado e símbolo
        
        state, symbol = [x.strip() for x in state_symbol.split(',', 1)]
        targets = [x.strip() for x in result.split('|')]

        if state not in transitions:
            transitions[state] = {}
        transitions[state][symbol] = targets

    return transitions

def render_automaton(automaton):
    if not automaton:
        return "Nenhum autômato foi definido ou criado para ser renderizado."
    dot = graphviz.Digraph()
    dot.attr(rankdir='LR')
    automaton_type = 'AFD' if isinstance(automaton, AFD) else 'AFN'
    dot.attr(label=f'Tipo de Autômato: {automaton_type}')
    for state in automaton.get_states():
        shape = 'doublecircle' if state in automaton.get_final_states() else 'circle'
        dot.node(state, shape=shape)
    dot.node('', shape='none')
    dot.edge('', automaton.get_initial_state())
    for state, transitions in automaton.get_transitions().items():
        for symbol, targets in transitions.items():
            for target in targets:
                dot.edge(state, target, label=symbol)
    return dot

st.title("Autômato Finito Determinístico e Não-determinístico")

option = st.selectbox(
    "Escolha a operação", 
    ["Criar AFD", "Criar AFN", "Converter AFN para AFD", "Converter AFD para AFN", "Minimizar AFD", "Verificar Equivalência", "Renderizar Autômato"]
)

states = st.text_input("Estados (separados por vírgulas)")
alphabet = st.text_input("Alfabeto (separados por vírgulas)")
initial_state = st.text_input("Estado Inicial")
final_states = st.text_input("Estados Finais (separados por vírgulas)")
transitions_input = st.text_area("Transições (um por linha, formato: estado,símbolo=estado(s))")
test_words_input = st.text_area("Palavras de teste para verificação de equivalência (separadas por vírgulas)")

automaton = None  # Garante que automaton é inicializado como None

if st.button("Executar"):
    states_list = states.split(",")
    alphabet_list = alphabet.split(",")
    final_states_list = final_states.split(",")
    transitions = parse_transitions(transitions_input)

    if option in ["Criar AFD", "Criar AFN"]:
        automaton_type = AFD if option == "Criar AFD" else AFN
        automaton = automaton_type(states_list, alphabet_list, initial_state, final_states_list, transitions)
    elif option in ["Converter AFN para AFD", "Converter AFD para AFN", "Minimizar AFD"]:
        if not automaton:
            st.error("Nenhum autômato foi definido para a operação.")
            st.stop()
        if option == "Converter AFN para AFD":
            automaton = afn_to_afd(automaton)
        elif option == "Converter AFD para AFN":
            automaton = afd_to_afn(automaton)
        elif option == "Minimizar AFD":
            automaton = minimize_afd(automaton)
    elif option == "Verificar Equivalência":
        test_words = test_words_input.split(",")
        afd = afn_to_afd(automaton)  # Converte novamente para garantir que está usando o AFD mais recente
        equivalence = check_equivalence(automaton, afd, test_words)
        st.write(f"Os autômatos são {'equivalentes' if equivalence else 'não equivalentes'} para as palavras de teste fornecidas.")
    elif option == "Renderizar Autômato":
        rendered_graph = render_automaton(automaton)
        if isinstance(rendered_graph, str):
            st.error(rendered_graph)
        else:
            st.graphviz_chart(rendered_graph, use_container_width=True)
