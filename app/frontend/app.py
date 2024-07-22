import sys
import os
import streamlit as st
import graphviz

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from afd import AFD
from afn import AFN
from operations import afn_to_afd, afd_to_afn, check_equivalence, minimize_afd, parse_transitions, render_automaton

st.title("Autômato Finito Determinístico e Não-determinístico")

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

option = st.selectbox(
    "Escolha a operação", 
    ("Criar AFD", "Criar AFN", "Converter AFN para AFD", "Converter AFD para AFN", "Minimizar AFD", "Verificar Equivalência", "Renderizar Autômato")
)

states = st.text_input("Estados (separados por vírgulas)", value="q0, q1, q2")
alphabet = st.text_input("Alfabeto (separados por vírgulas)", value="a, b")
initial_state = st.text_input("Estado Inicial", value="q0")
final_states = st.text_input("Estados Finais (separados por vírgulas)", value="q2")
transitions_input = st.text_area("Transições (um por linha, formato: estado,símbolo=estado(s))", value="q0,a=q1\nq0,b=q0\nq1,a=q2\nq1,b=q1\nq2,a=q2\nq2,b=q2")

# Adicionando entrada para palavras de teste
test_words_input = st.text_area("Palavras de teste para verificação de equivalência (separadas por vírgulas)", value="a, ab, aab, aa")

if st.button("Executar"):
    transitions = parse_transitions(transitions_input)
    automaton = None
    if "AFN" in option:
        automaton = AFN(states.split(","), alphabet.split(","), initial_state, final_states.split(","), transitions)
    elif "AFD" in option:
        automaton = AFD(states.split(","), alphabet.split(","), initial_state, final_states.split(","), transitions)

    if "Converter AFN para AFD" in option:
        automaton = afn_to_afd(automaton)
    elif "Converter AFD para AFN" in option:
        automaton = afd_to_afn(automaton)
    elif "Minimizar AFD" in option:
        automaton = minimize_afd(automaton)
    elif "Verificar Equivalência" in option:
        test_words = test_words_input.split(",")
        equivalent = check_equivalence(automaton, afn_to_afd(automaton), test_words)
        st.write(f"Os autômatos são {'equivalentes' if equivalent else 'não equivalentes'} para as palavras de teste fornecidas.")

    if automaton:
        st.graphviz_chart(render_automaton(automaton), use_container_width=True)
