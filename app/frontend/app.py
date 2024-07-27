from operations import afn_to_afd, afd_to_afn, check_equivalence, minimize_afd, parse_transitions, render_automato
from afn import AFN
from afd import AFD
import sys
import os
import streamlit as st
import graphviz
from graphviz import Digraph

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')))


st.title("Projeto de Autômatos Teoria da Computação 🚀")

# Navegação
# menu = ["Home", "Criar AFD", "Criar AFN", "Converter AFN para AFD", "Converter AFD para AFN",
#         "Minimizar AFD", "Verificar Equivalência", "Renderizar Autômato", "Testar Palavra"]
menu = ["Home", "Criar AFD", "Criar AFN", "Converter AFN para AFD",
         "Minimizar AFD", "Verificar Equivalência", "Testar Palavras"]
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
st.sidebar.write(
    "```\nq0,a=q1\nq0,b=q0\nq1,a=q2\nq1,b=q1\nq2,a=q2\nq2,b=q2\n```")
st.sidebar.write("### Palavras de Teste")
st.sidebar.write("`a, ab, aab, aa`")


def input_fields():
    states = st.text_input(
        "Estados (separados por vírgulas)", value="q0, q1, q2").split(',')
    alphabet = st.text_input(
        "Alfabeto (separados por vírgulas)", value="a, b").split(',')
    initial_state = st.text_input("Estado Inicial", value="q0")
    final_states = st.text_input(
        "Estados Finais (separados por vírgulas)", value="q2").split(',')
    transitions_input = st.text_area("Transições (um por linha, formato: estado,símbolo=estado(s))",
                                     value="q0,a=q1\nq0,b=q0\nq1,a=q2\nq1,b=q1\nq2,a=q2\nq2,b=q2")
    return states, alphabet, initial_state, final_states, transitions_input


if choice == "Home":
    st.write("## Selecione uma operação no menu lateral à esquerda.")

elif choice in ["Criar AFD", "Criar AFN"]:
    st.write(f"## {choice}")
    states, alphabet, initial_state, final_states, transitions_input = input_fields()

    if st.button("Criar"):
        transitions = parse_transitions(transitions_input)
        if choice == "Criar AFD":
            automaton = AFD(states, alphabet, initial_state,
                            final_states, transitions)
        else:
            automaton = AFN(states, alphabet, initial_state,
                            final_states, transitions)

        dot = render_automato(automaton)
        st.graphviz_chart(dot.source, use_container_width=True)

elif choice == "Converter AFN para AFD":
    st.write(f"## {choice}")
    states, alphabet, initial_state, final_states, transitions_input = input_fields()

    if st.button("Converter"):
        transitions = parse_transitions(transitions_input)
        automaton = AFN(states, alphabet, initial_state,
                        final_states, transitions)
        converted_automaton = afn_to_afd(automaton)

        dot = render_automato(converted_automaton)
        st.graphviz_chart(dot.source, use_container_width=True)

# elif choice == "Converter AFD para AFN":
#     st.write(f"## {choice}")
#     states, alphabet, initial_state, final_states, transitions_input = input_fields()

#     if st.button("Converter"):
#         transitions = parse_transitions(transitions_input)
#         automaton = AFD(states, alphabet, initial_state,
#                         final_states, transitions)
#         converted_automaton = afd_to_afn(automaton)

#         dot = render_automato(converted_automaton)
#         st.graphviz_chart(dot.source, use_container_width=True)

elif choice == "Minimizar AFD":
    st.write(f"## {choice}")
    states, alphabet, initial_state, final_states, transitions_input = input_fields()

    if st.button("Minimizar"):
        transitions = parse_transitions(transitions_input)
        automaton = AFD(states, alphabet, initial_state,
                        final_states, transitions)
        minimized_automaton = minimize_afd(automaton)

        dot = render_automato(minimized_automaton)
        st.graphviz_chart(dot.source, use_container_width=True)

elif choice == "Verificar Equivalência":
    st.write(f"## {choice}")
    states, alphabet, initial_state, final_states, transitions_input = input_fields()
    test_words_input = st.text_area(
        "Palavras de teste para verificação de equivalência (separadas por vírgulas)", value="a, ab, aab, aa")

    if st.button("Verificar"):
        transitions = parse_transitions(transitions_input)
        automaton = AFN(states, alphabet, initial_state,
                        final_states, transitions)
        equivalent = check_equivalence(automaton, afn_to_afd(
            automaton), test_words_input.split(","))
        st.write(f"Os autômatos são {
                 'equivalentes' if equivalent else 'não equivalentes'} para as palavras de teste fornecidas.")

# elif choice == "Renderizar Autômato":
#     st.write(f"## {choice}")
#     states, alphabet, initial_state, final_states, transitions_input = input_fields()

#     if st.button("Renderizar"):
#         transitions = parse_transitions(transitions_input)
#         automaton = AFD(states, alphabet, initial_state,
#                         final_states, transitions)

#         dot = render_automato(automaton)
#         st.graphviz_chart(dot.source, use_container_width=True)


elif choice == "Testar Palavras":
    st.write(f"## {choice}")
    states, alphabet, initial_state, final_states, transitions_input = input_fields()
    test_words_input = st.text_input(
        "Palavras de teste (separadas por vírgulas)", value="a, ab, aab, aa")

    if st.button("Testar"):
        transitions = parse_transitions(transitions_input)
        is_afd = all(isinstance(v, str)
                     for trans in transitions.values() for v in trans.values())

        if is_afd:
            automaton = AFD(states, alphabet, initial_state,
                            final_states, transitions)
        else:
            automaton = AFN(states, alphabet, initial_state,
                            final_states, transitions)

        dot = render_automato(automaton)
        st.graphviz_chart(dot.source, use_container_width=True)

        test_words = [word.strip() for word in test_words_input.split(",")]
        results = {word: automaton.accepts(word) for word in test_words}

        for word, result in results.items():
            st.write(f"A palavra '{word}' é {
                     'aceita' if result else 'rejeitada'} pelo autômato.")
