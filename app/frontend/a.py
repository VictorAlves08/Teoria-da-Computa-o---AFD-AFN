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
    dot = graphviz.Digraph()
    dot.attr(rankdir='LR')
    automaton_type = 'AFD' if isinstance(automaton, AFD) else 'AFN'
    dot.attr(label=f'Tipo de Autômato: {automaton_type}')
    for state in automaton.get_states():
        shape = 'doublecircle' if state in automaton.get_final_states() else 'circle'
        dot.node(state, shape=shape)
    dot.node('', shape='plaintext', label="Start")
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

automaton = None  # Inicializa automaton como None para garantir que ela exista

if st.button("Executar"):
    states_list = states.split(",")
    alphabet_list = alphabet.split(",")
    final_states_list = final_states.split(",")
    transitions = parse_transitions(transitions_input)

    if option in ["Criar AFD", "Minimizar AFD", "Converter AFN para AFD"]:
        automaton = AFD(states_list, alphabet_list, initial_state, final_states_list, transitions)
        if option == "Minimizar AFD":
            automaton = minimize_afd(automaton)
        elif option == "Converter AFN para AFD":
            automaton = afn_to_afd(automaton)
    elif option in ["Criar AFN", "Converter AFD para AFN"]:
        automaton = AFN(states_list, alphabet_list, initial_state, final_states_list, transitions)
        if option == "Converter AFD para AFN":
            automaton = afd_to_afn(automaton)

    if automaton:
        st.graphviz_chart(render_automaton(automaton), use_container_width=True)

