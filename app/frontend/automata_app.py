import streamlit as st
from app.backend.automatos.operations import Operations
from app.backend.automatos.afn import AFN
from app.backend.automatos.afd import AFD


class AutomataApp:
    def __init__(self):
        self.operations = Operations()
        st.title("Projeto de Autômatos Teoria da Computação 🚀")
        self.menu = ["Home", "Criar AFD", "Criar AFN", "Converter AFN para AFD",
                     "Minimizar AFD", "Verificar Equivalência", "Testar Palavras", "Máquina de Turing - Testar Palavra"]
        self.choice = st.sidebar.selectbox("Escolha a operação", self.menu)
        self.show_examples()
        self.route()

    def show_examples(self):
        st.sidebar.write("## Exemplo de entrada")
        st.sidebar.write("### Estados")
        st.sidebar.write("`q0,q1,q2,q3,q4,q5`")
        st.sidebar.write("### Alfabeto")
        st.sidebar.write("`a,b`")
        st.sidebar.write("### Estado Inicial")
        st.sidebar.write("`q0`")
        st.sidebar.write("### Estados Finais")
        st.sidebar.write("`q3,q4`")
        st.sidebar.write("### Transições")
        st.sidebar.write(
            "```\nq0,a=q1\nq0,b=q5\nq1,a=q3\nq1,b=q2\nq5,a=q5\nq5,b=q5\nq3,a=q3\nq3,b=q2\nq2,b=q5\nq2,a=q4\nq4,a=q3\nq4,b=q2```")
        st.sidebar.write("### Palavras de Teste")
        st.sidebar.write("`a,b,ab,ba,aabb,bbaa`")

    def input_fields(self, label=""):
        states = st.text_input(
            f"Estados (separados por vírgulas - sem espaços entre eles) {label}", value="q0,q1,q2,q3,q4,q5").split(',')
        alphabet = st.text_input(
            f"Alfabeto (separados por vírgulas - sem espaços entre eles) {label}", value="a,b").split(',')
        initial_state = st.text_input(f"Estado Inicial {label}", value="q0")
        final_states = st.text_input(
            f"Estados Finais (separados por vírgulas - sem espaços entre eles) {label}", value="q3,q4").split(',')
        transitions_input = st.text_area(f"Transições (um por linha, formato: estado,símbolo=estado(s) - sem espaços entre eles) {label}",
                                         value="q0,a=q1\nq0,b=q5\nq1,a=q3\nq1,b=q2\nq5,a=q5\nq5,b=q5\nq3,a=q3\nq3,b=q2\nq2,b=q5\nq2,a=q4\nq4,a=q3\nq4,b=q2")
        return states, alphabet, initial_state, final_states, transitions_input

    def create_automaton(self, automaton_type: str):
        st.write(f"## Criar {automaton_type}")
        states, alphabet, initial_state, final_states, transitions_input = self.input_fields()
        if st.button("Criar"):
            transitions = self.operations.parse_transitions(transitions_input)
            automaton = AFD(states, alphabet, initial_state, final_states, transitions) if automaton_type == "AFD" else AFN(
                states, alphabet, initial_state, final_states, transitions)
            self.render_and_display_automaton(automaton)

    def convert_afn_to_afd(self):
        st.write("## Converter AFN para AFD")
        states, alphabet, initial_state, final_states, transitions_input = self.input_fields()
        if st.button("Converter"):
            transitions = self.operations.parse_transitions(transitions_input)
            afn = AFN(states, alphabet, initial_state,
                      final_states, transitions)
            afd = self.operations.afn_to_afd(afn)
            self.render_and_display_automaton(afd)

    def minimize_afd(self):
        st.write("## Minimizar AFD")
        states, alphabet, initial_state, final_states, transitions_input = self.input_fields()
        if st.button("Minimizar"):
            transitions = self.operations.parse_transitions(transitions_input)
            afd = AFD(states, alphabet, initial_state,
                      final_states, transitions)
            minimized_afd = self.operations.minimize_afd(afd)
            self.render_and_display_automaton(minimized_afd)

    def check_equivalence(self):
        st.write("## Verificar Equivalência")

        st.write("### Autômato 1")
        states1, alphabet1, initial_state1, final_states1, transitions_input1 = self.input_fields(
            "(Autômato 1)")

        st.write("### Autômato 2")
        states2, alphabet2, initial_state2, final_states2, transitions_input2 = self.input_fields(
            "(Autômato 2)")

        st.write("### Palavras de Teste")
        test_words_input = st.text_area(
            "Palavras de teste para verificação de equivalência (separadas por vírgulas - sem espaços entre eles)", value="a,b,ab,ba,aabb,bbaa")

        if st.button("Verificar"):
            transitions1 = self.operations.parse_transitions(
                transitions_input1)
            transitions2 = self.operations.parse_transitions(
                transitions_input2)

            afn1 = AFN(states1, alphabet1, initial_state1,
                       final_states1, transitions1)
            afn2 = AFN(states2, alphabet2, initial_state2,
                       final_states2, transitions2)

            equivalent = self.operations.check_equivalence(
                afn1, afn2, test_words_input.split(","))
            st.write(f"Os autômatos são {
                     'equivalentes' if equivalent else 'não equivalentes'} para as palavras de teste fornecidas.")

    def test_words(self):
        st.write("## Testar Palavras")
        states, alphabet, initial_state, final_states, transitions_input = self.input_fields()
        test_words_input = st.text_input(
            "Palavras de teste (separadas por vírgulas - sem espaços entre eles)", value="a,b,ab,ba,aabb,bbaa")

        if st.button("Testar"):
            transitions = self.operations.parse_transitions(transitions_input)

            is_afd = all(isinstance(v, str)
                         for trans in transitions.values() for v in trans.values())

            if is_afd:
                automaton = AFD(states, alphabet, initial_state,
                                final_states, transitions)
            else:
                automaton = AFN(states, alphabet, initial_state,
                                final_states, transitions)

            self.render_and_display_automaton(automaton)

            test_words = [word.strip() for word in test_words_input.split(",")]

            results = {word: automaton.accepts(word) for word in test_words}

            for word, result in results.items():
                st.write(f"A palavra '{word}' é {
                         'aceita' if result else 'rejeitada'} pelo autômato.")

    def turing_machine(self):
        st.write("## Máquina de Turing - Testar Palavra")
        st.write(
            "Ainda não implementei a funcionalidade de criação de uma Máquina de Turing.")

    def render_and_display_automaton(self, automaton):
        dot = self.operations.render_automato(automaton)
        st.graphviz_chart(dot.source, use_container_width=True)

    def route(self):
        if self.choice == "Home":
            st.write("## Selecione uma operação no menu lateral à esquerda.")
        elif self.choice == "Criar AFD":
            self.create_automaton("AFD")
        elif self.choice == "Criar AFN":
            self.create_automaton("AFN")
        elif self.choice == "Converter AFN para AFD":
            self.convert_afn_to_afd()
        elif self.choice == "Minimizar AFD":
            self.minimize_afd()
        elif self.choice == "Verificar Equivalência":
            self.check_equivalence()
        elif self.choice == "Testar Palavras":
            self.test_words()
        elif self.choice == "Máquina de Turing - Testar Palavra":
            self.turing_machine()
