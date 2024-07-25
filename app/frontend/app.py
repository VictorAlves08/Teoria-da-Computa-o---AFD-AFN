# import sys
# import os
# import streamlit as st
# import graphviz

# # Adiciona o diretório raiz do projeto ao sys.path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# from afd import AFD
# from afn import AFN
# from operations import afn_to_afd, afd_to_afn, check_equivalence, minimize_afd, parse_transitions, render_automaton

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
#     ("Criar AFD", "Criar AFN", "Converter AFN para AFD", "Converter AFD para AFN", "Minimizar AFD", "Verificar Equivalência", "Renderizar Autômato")
# )

# states = st.text_input("Estados (separados por vírgulas)", value="q0, q1, q2")
# alphabet = st.text_input("Alfabeto (separados por vírgulas)", value="a, b")
# initial_state = st.text_input("Estado Inicial", value="q0")
# final_states = st.text_input("Estados Finais (separados por vírgulas)", value="q2")
# transitions_input = st.text_area("Transições (um por linha, formato: estado,símbolo=estado(s))", value="q0,a=q1\nq0,b=q0\nq1,a=q2\nq1,b=q1\nq2,a=q2\nq2,b=q2")

# # Adicionando entrada para palavras de teste
# test_words_input = st.text_area("Palavras de teste para verificação de equivalência (separadas por vírgulas)", value="a, ab, aab, aa")

# if st.button("Executar"):
#     transitions = parse_transitions(transitions_input)
#     automaton = None
#     if "AFN" in option:
#         automaton = AFN(states.split(","), alphabet.split(","), initial_state, final_states.split(","), transitions)
#     elif "AFD" in option:
#         automaton = AFD(states.split(","), alphabet.split(","), initial_state, final_states.split(","), transitions)

#     if "Converter AFN para AFD" in option:
#         automaton = afn_to_afd(automaton)
#     elif "Converter AFD para AFN" in option:
#         automaton = afd_to_afn(automaton)
#     elif "Minimizar AFD" in option:
#         automaton = minimize_afd(automaton)
#     elif "Verificar Equivalência" in option:
#         test_words = test_words_input.split(",")
#         equivalent = check_equivalence(automaton, afn_to_afd(automaton), test_words)
#         st.write(f"Os autômatos são {'equivalentes' if equivalent else 'não equivalentes'} para as palavras de teste fornecidas.")

#     if automaton:
#         st.graphviz_chart(render_automaton(automaton), use_container_width=True)


# import sys
# import os
# import streamlit as st
# import graphviz
# from graphviz import Digraph

# # Adiciona o diretório raiz do projeto ao sys.path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# from afd import AFD
# from afn import AFN
# from operations import afn_to_afd, afd_to_afn, check_equivalence, minimize_afd, parse_transitions

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
#     ("Criar AFD", "Criar AFN", "Converter AFN para AFD", "Converter AFD para AFN", "Minimizar AFD", "Verificar Equivalência", "Renderizar Autômato")
# )

# states = st.text_input("Estados (separados por vírgulas)", value="q0, q1, q2")
# alphabet = st.text_input("Alfabeto (separados por vírgulas)", value="a, b")
# initial_state = st.text_input("Estado Inicial", value="q0")
# final_states = st.text_input("Estados Finais (separados por vírgulas)", value="q2")
# transitions_input = st.text_area("Transições (um por linha, formato: estado,símbolo=estado(s))", value="q0,a=q1\nq0,b=q0\nq1,a=q2\nq1,b=q1\nq2,a=q2\nq2,b=q2")

# # Adicionando entrada para palavras de teste
# test_words_input = st.text_area("Palavras de teste para verificação de equivalência (separadas por vírgulas)", value="a, ab, aab, aa")

# def desenhar_automato(automaton):
#     dot = Digraph()
#     dot.attr(rankdir='LR')
#     dot.attr('node', shape='circle')

#     if isinstance(automaton, AFD):
#         dot.attr(label='Tipo: AFD')
#     else:
#         dot.attr(label='Tipo: AFN')

#     dot.node('->', shape='none', width='0', height='0', label='')
#     dot.edge('->', automaton.get_initial_state())

#     for state in automaton.get_final_states():
#         dot.node(state, shape='doublecircle', fontsize='19', fontcolor='green')
#     for state, transitions in automaton.get_transitions().items():
#         for symbol, targets in transitions.items():
#             if isinstance(targets, list):  # Handling AFN
#                 for target in targets:
#                     dot.edge(state, target, label=symbol)
#             else:  # Handling AFD
#                 dot.edge(state, targets, label=symbol)

#     return dot

# if st.button("Executar"):
#     transitions = parse_transitions(transitions_input)
#     automaton = None
#     if "AFN" in option:
#         automaton = AFN(states.split(","), alphabet.split(","), initial_state, final_states.split(","), transitions)
#     elif "AFD" in option:
#         automaton = AFD(states.split(","), alphabet.split(","), initial_state, final_states.split(","), transitions)

#     if "Converter AFN para AFD" in option:
#         automaton = afn_to_afd(automaton)
#     elif "Converter AFD para AFN" in option:
#         automaton = afd_to_afn(automaton)
#     elif "Minimizar AFD" in option:
#         automaton = minimize_afd(automaton)
#     elif "Verificar Equivalência" in option:
#         test_words = test_words_input.split(",")
#         equivalent = check_equivalence(automaton, afn_to_afd(automaton), test_words)
#         st.write(f"Os autômatos são {'equivalentes' if equivalent else 'não equivalentes'} para as palavras de teste fornecidas.")

#     if automaton:
#         dot = desenhar_automato(automaton)
#         st.graphviz_chart(dot.source, use_container_width=True)
import sys
import os
import streamlit as st
import graphviz
from graphviz import Digraph

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from afd import AFD
from afn import AFN
from operations import afn_to_afd, afd_to_afn, check_equivalence, minimize_afd, parse_transitions, render_automato

st.title("Projeto de Autômatos Teoria da Computação 🚀")

# Navegação
menu = ["Home", "Criar AFD", "Criar AFN", "Converter AFN para AFD", "Converter AFD para AFN", "Minimizar AFD", "Verificar Equivalência", "Renderizar Autômato","Testar Palavra"]
choice = st.sidebar.selectbox("Escolha a operação", menu)
# Exemplos de entrada na barra lateral
st.sidebar.write("## Exemplo de entrada")
st.sidebar.write("### Estados")
st.sidebar.write("`q0, q1, q2`")
st.sidebar.write("### Alfabeto")
st.sidebar.write("`a, b`")
st.sidebar.write("### Estado Inicial")
st.sidebar.write("`q0`")
st.sidebar.write("### Estados Finais")
st.sidebar.write("`q2`")
st.sidebar.write("### Transições")
st.sidebar.write("```\nq0,a=q1\nq0,b=q0\nq1,a=q2\nq1,b=q1\nq2,a=q2\nq2,b=q2\n```")
st.sidebar.write("### Palavras de Teste")
st.sidebar.write("`a, ab, aab, aa`")


def input_fields():
    states = st.text_input("Estados (separados por vírgulas)", value="q0, q1, q2")
    alphabet = st.text_input("Alfabeto (separados por vírgulas)", value="a, b")
    initial_state = st.text_input("Estado Inicial", value="q0")
    final_states = st.text_input("Estados Finais (separados por vírgulas)", value="q2")
    transitions_input = st.text_area("Transições (um por linha, formato: estado,símbolo=estado(s))", value="q0,a=q1\nq0,b=q0\nq1,a=q2\nq1,b=q1\nq2,a=q2\nq2,b=q2")
    return states, alphabet, initial_state, final_states, transitions_input

if choice == "Home":
    st.write("## Selecione uma operação no menu lateral à esquerda.")

elif choice == "Criar AFD" or choice == "Criar AFN":
    st.write(f"## {choice}")
    states, alphabet, initial_state, final_states, transitions_input = input_fields()
    
    if st.button("Criar"):
        transitions = parse_transitions(transitions_input)
        if choice == "Criar AFD":
            automaton = AFD(states.split(","), alphabet.split(","), initial_state, final_states.split(","), transitions)
        else:
            automaton = AFN(states.split(","), alphabet.split(","), initial_state, final_states.split(","), transitions)
        
        dot = render_automato(automaton)
        st.graphviz_chart(dot.source, use_container_width=True)

elif choice == "Converter AFN para AFD":
    st.write(f"## {choice}")
    states, alphabet, initial_state, final_states, transitions_input = input_fields()

    if st.button("Converter"):
        transitions = parse_transitions(transitions_input)
        automaton = AFN(states.split(","), alphabet.split(","), initial_state, final_states.split(","), transitions)
        automaton = afn_to_afd(automaton)
        
        dot = render_automato(automaton)
        st.graphviz_chart(dot.source, use_container_width=True)

elif choice == "Converter AFD para AFN":
    st.write(f"## {choice}")
    states, alphabet, initial_state, final_states, transitions_input = input_fields()

    if st.button("Converter"):
        transitions = parse_transitions(transitions_input)
        automaton = AFD(states.split(","), alphabet.split(","), initial_state, final_states.split(","), transitions)
        automaton = afd_to_afn(automaton)
        
        dot = render_automato(automaton)
        st.graphviz_chart(dot.source, use_container_width=True)

elif choice == "Minimizar AFD":
    st.write(f"## {choice}")
    states, alphabet, initial_state, final_states, transitions_input = input_fields()

    if st.button("Minimizar"):
        transitions = parse_transitions(transitions_input)
        automaton = AFD(states.split(","), alphabet.split(","), initial_state, final_states.split(","), transitions)
        automaton = minimize_afd(automaton)
        
        dot = render_automato(automaton)
        st.graphviz_chart(dot.source, use_container_width=True)

elif choice == "Verificar Equivalência":
    st.write(f"## {choice}")
    states, alphabet, initial_state, final_states, transitions_input = input_fields()
    test_words_input = st.text_area("Palavras de teste para verificação de equivalência (separadas por vírgulas)", value="a, ab, aab, aa")

    if st.button("Verificar"):
        transitions = parse_transitions(transitions_input)
        automaton = AFN(states.split(","), alphabet.split(","), initial_state, final_states.split(","), transitions)
        equivalent = check_equivalence(automaton, afn_to_afd(automaton), test_words_input.split(","))
        st.write(f"Os autômatos são {'equivalentes' if equivalent else 'não equivalentes'} para as palavras de teste fornecidas.")

elif choice == "Renderizar Autômato":
    st.write(f"## {choice}")
    states, alphabet, initial_state, final_states, transitions_input = input_fields()
    
    if st.button("Renderizar"):
        transitions = parse_transitions(transitions_input)
        automaton = AFD(states.split(","), alphabet.split(","), initial_state, final_states.split(","), transitions)
        
        dot = render_automato(automaton)
        st.graphviz_chart(dot.source, use_container_width=True)


# elif choice == "Testar Palavra":
#     st.write(f"## {choice}")
#     states, alphabet, initial_state, final_states, transitions_input = input_fields()
#     test_word = st.text_input("Palavra de teste", value="a")

#     if st.button("Testar"):
#         transitions = parse_transitions(transitions_input)
#         is_afd = all(isinstance(v, str) for v in transitions.values())
        
#         if is_afd:
#             automaton = AFD(states.split(","), alphabet.split(","), initial_state, final_states.split(","), transitions)
#             dot = render_automato(automaton)
#             st.graphviz_chart(dot.source, use_container_width=True)
#         else:
#             automaton = AFN(states.split(","), alphabet.split(","), initial_state, final_states.split(","), transitions)
#             dot = render_automato(automaton)
#             st.graphviz_chart(dot.source, use_container_width=True)
        
#         result = automaton.accepts(test_word)
#         st.write(f"A palavra {test_word} é {'aceita' if result else 'rejeitada'} pelo autômato.")

elif choice == "Testar Palavra":
    st.write(f"## {choice}")
    states, alphabet, initial_state, final_states, transitions_input = input_fields()
    test_words_input = st.text_input("Palavras de teste (separadas por vírgulas)", value="a, ab, aab, aa")

    if st.button("Testar"):
        transitions = parse_transitions(transitions_input)
        is_afd = all(isinstance(v, str) for v in transitions.values())
        
        if is_afd:
            automaton = AFD(states.split(","), alphabet.split(","), initial_state, final_states.split(","), transitions)
            dot = render_automato(automaton)
            st.graphviz_chart(dot.source, use_container_width=True)
        else:
            automaton = AFN(states.split(","), alphabet.split(","), initial_state, final_states.split(","), transitions)
            dot = render_automato(automaton)
            st.graphviz_chart(dot.source, use_container_width=True)
        
        test_words = [word.strip() for word in test_words_input.split(",")]
        results = {word: automaton.accepts(word) for word in test_words}

        for word, result in results.items():
            st.write(f"A palavra '{word}' é {'aceita' if result else 'rejeitada'} pelo autômato.")
