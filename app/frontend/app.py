# import streamlit as st
# from afn import AFN

# def main():
#     st.title("Simulador de Autômatos Finitos")
    
#     st.sidebar.title("Configurações do AFN")
#     estados = st.sidebar.text_area("Estados (separados por vírgulas)")
#     alfabeto = st.sidebar.text_area("Alfabeto (separado por vírgulas)")
#     transicoes = st.sidebar.text_area("Transições (formato: estado,símbolo->estado; estado,símbolo->estado;...)")
#     estado_inicial = st.sidebar.text_input("Estado Inicial")
#     estados_aceitacao = st.sidebar.text_area("Estados de Aceitação (separados por vírgulas)")
    
#     if st.sidebar.button("Simular"):
#         estados = set(estados.split(","))
#         alfabeto = set(alfabeto.split(","))
#         transicoes_dict = {}
#         for trans in transicoes.split(";"):
#             estado, resto = trans.split(",")
#             simbolo, prox_estado = resto.split("->")
#             if estado not in transicoes_dict:
#                 transicoes_dict[estado] = {}
#             if simbolo not in transicoes_dict[estado]:
#                 transicoes_dict[estado][simbolo] = set()
#             transicoes_dict[estado][simbolo].add(prox_estado)
#         estado_inicial = estado_inicial.strip()
#         estados_aceitacao = set(estados_aceitacao.split(","))
        
#         afn = AFN(estados, alfabeto, transicoes_dict, estado_inicial, estados_aceitacao)
#         afd = afn.converter_para_afd()
        
#         palavra = st.text_input("Digite uma palavra para simulação")
#         if palavra:
#             aceito = afd.simular(palavra)
#             st.write(f"A palavra '{palavra}' foi {'aceita' if aceito else 'rejeitada'} pelo AFD.")

# if __name__ == "__main__":
#     main()
# import sys
# import os
# import streamlit as st

# # Adiciona o diretório 'app' ao sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# from app.backend.automatos.afd import AFD
# from app.backend.automatos.afn import AFN
# from app.backend.automatos.operations import afn_to_afd, check_equivalence, minimize_afd

# st.title("Autômato Finito Determinístico e Não-determinístico")

# option = st.selectbox("Escolha o tipo de autômato", ("AFN", "AFD"))

# states = st.text_input("Estados (separados por vírgulas)")
# alphabet = st.text_input("Alfabeto (separados por vírgulas)")
# initial_state = st.text_input("Estado Inicial")
# final_states = st.text_input("Estados Finais (separados por vírgulas)")

# transitions_input = st.text_area("Transições (um por linha, formato: estado,símbolo=estado(s))")

# # Campo adicional para palavras de teste
# test_words_input = st.text_area("Palavras de teste para verificação de equivalência (separadas por vírgulas)")

# if st.button("Executar"):
#     states_list = states.split(",")
#     alphabet_list = alphabet.split(",")
#     final_states_list = final_states.split(",")

#     transitions = {}
#     for line in transitions_input.split("\n"):
#         state, transition = line.split("=")
#         source_state, symbol = state.split(",")
#         target_states = transition.split(",")
#         if option == "AFN":
#             if source_state not in transitions:
#                 transitions[source_state] = {}
#             if symbol not in transitions[source_state]:
#                 transitions[source_state][symbol] = []
#             transitions[source_state][symbol].extend(target_states)
#         else:
#             if source_state not in transitions:
#                 transitions[source_state] = {}
#             transitions[source_state][symbol] = target_states[0]

#     if option == "AFN":
#         afn = AFN(states_list, alphabet_list, initial_state, final_states_list, transitions)
#         afd = afn_to_afd(afn)
#         minimized_afd = minimize_afd(afd)
#         st.write("AFD Minimizado:", minimized_afd)
#     else:
#         afd = AFD(states_list, alphabet_list, initial_state, final_states_list, transitions)
#         minimized_afd = minimize_afd(afd)
#         st.write("AFD Minimizado:", minimized_afd)

#     # Verificação de equivalência
#     if test_words_input:
#         test_words = test_words_input.split(",")
#         if option == "AFN":
#             equivalent = check_equivalence(afn, afd, test_words)
#         else:
#             equivalent = check_equivalence(afd, minimized_afd, test_words)
        
#         st.write(f"Os autômatos são {'equivalentes' if equivalent else 'não equivalentes'} para as palavras de teste fornecidas.")

# import sys
# import os
# import streamlit as st

# # Adiciona o diretório raiz do projeto ao sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# from afd import AFD
# from afn import AFN
# from operations import afn_to_afd, check_equivalence, minimize_afd

# st.title("Autômato Finito Determinístico e Não-determinístico")

# option = st.selectbox("Escolha o tipo de autômato", ("AFN", "AFD"))

# states = st.text_input("Estados (separados por vírgulas)")
# alphabet = st.text_input("Alfabeto (separados por vírgulas)")
# initial_state = st.text_input("Estado Inicial")
# final_states = st.text_input("Estados Finais (separados por vírgulas)")

# transitions_input = st.text_area("Transições (um por linha, formato: estado,símbolo=estado(s))")

# # Campo adicional para palavras de teste
# test_words_input = st.text_area("Palavras de teste para verificação de equivalência (separadas por vírgulas)")

# if st.button("Executar"):
#     states_list = states.split(",")
#     alphabet_list = alphabet.split(",")
#     final_states_list = final_states.split(",")

#     transitions = {}
#     for line in transitions_input.split("\n"):
#         state, transition = line.split("=")
#         source_state, symbol = state.split(",")
#         target_states = transition.split(",")
#         if option == "AFN":
#             if source_state not in transitions:
#                 transitions[source_state] = {}
#             if symbol not in transitions[source_state]:
#                 transitions[source_state][symbol] = []
#             transitions[source_state][symbol].extend(target_states)
#         else:
#             if source_state not in transitions:
#                 transitions[source_state] = {}
#             transitions[source_state][symbol] = target_states[0]

#     if option == "AFN":
#         afn = AFN(states_list, alphabet_list, initial_state, final_states_list, transitions)
#         afd = afn_to_afd(afn)
#         minimized_afd = minimize_afd(afd)
#         st.write("AFD Minimizado:", minimized_afd)
#     else:
#         afd = AFD(states_list, alphabet_list, initial_state, final_states_list, transitions)
#         minimized_afd = minimize_afd(afd)
#         st.write("AFD Minimizado:", minimized_afd)

#     # Verificação de equivalência
#     if test_words_input:
#         test_words = test_words_input.split(",")
#         if option == "AFN":
#             equivalent = check_equivalence(afn, afd, test_words)
#         else:
#             equivalent = check_equivalence(afd, minimized_afd, test_words)
        
#         st.write(f"Os autômatos são {'equivalentes' if equivalent else 'não equivalentes'} para as palavras de teste fornecidas.")

# import sys
# import os
# import streamlit as st

# # Adiciona o diretório raiz do projeto ao sys.path
# #sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# from afd import AFD
# from afn import AFN
# from operations import afn_to_afd, check_equivalence, minimize_afd

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

# option = st.selectbox("Escolha o tipo de autômato", ("AFN", "AFD"))

# states = st.text_input("Estados (separados por vírgulas)", value="q0, q1, q2")
# alphabet = st.text_input("Alfabeto (separados por vírgulas)", value="a, b")
# initial_state = st.text_input("Estado Inicial", value="q0")
# final_states = st.text_input("Estados Finais (separados por vírgulas)", value="q2")

# transitions_input = st.text_area("Transições (um por linha, formato: estado,símbolo=estado(s))", 
#                                  value="q0,a=q1\nq0,b=q0\nq1,a=q2\nq1,b=q1\nq2,a=q2\nq2,b=q2")

# # Campo adicional para palavras de teste
# test_words_input = st.text_area("Palavras de teste para verificação de equivalência (separadas por vírgulas)", value="a, ab, aab, aa")

# if st.button("Executar"):
#     states_list = states.split(",")
#     alphabet_list = alphabet.split(",")
#     final_states_list = final_states.split(",")

#     transitions = {}
#     for line in transitions_input.split("\n"):
#         state, transition = line.split("=")
#         source_state, symbol = state.split(",")
#         target_states = transition.split(",")
#         if option == "AFN":
#             if source_state not in transitions:
#                 transitions[source_state] = {}
#             if symbol not in transitions[source_state]:
#                 transitions[source_state][symbol] = []
#             transitions[source_state][symbol].extend(target_states)
#         else:
#             if source_state not in transitions:
#                 transitions[source_state] = {}
#             transitions[source_state][symbol] = target_states[0]

#     if option == "AFN":
#         afn = AFN(states_list, alphabet_list, initial_state, final_states_list, transitions)
#         afd = afn_to_afd(afn)
#         minimized_afd = minimize_afd(afd)
#         st.write("AFD Minimizado:", minimized_afd)
#     else:
#         afd = AFD(states_list, alphabet_list, initial_state, final_states_list, transitions)
#         minimized_afd = minimize_afd(afd)
#         st.write("AFD Minimizado:", minimized_afd)

#     # Verificação de equivalência
#     if test_words_input:
#         test_words = test_words_input.split(",")
#         if option == "AFN":
#             equivalent = check_equivalence(afn, afd, test_words)
#         else:
#             equivalent = check_equivalence(afd, minimized_afd, test_words)
        
#         st.write(f"Os autômatos são {'equivalentes' if equivalent else 'não equivalentes'} para as palavras de teste fornecidas.")


# import sys
# import os
# import streamlit as st
# import graphviz
# from afd import AFD
# from afn import AFN
# from operations import afn_to_afd, minimize_afd, check_equivalence, render_automaton

# # Adiciona o diretório raiz do projeto ao sys.path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))



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

# # Entrada dos autômatos
# option = st.selectbox("Escolha a operação", ("Criar AFD", "Criar AFN", "Converter AFN para AFD", "Minimizar AFD", "Verificar Equivalência"))

# states = st.text_input("Estados (separados por vírgulas)", value="q0, q1, q2")
# alphabet = st.text_input("Alfabeto (separados por vírgulas)", value="a, b")
# initial_state = st.text_input("Estado Inicial", value="q0")
# final_states = st.text_input("Estados Finais (separados por vírgulas)", value="q2")

# transitions_input = st.text_area("Transições (um por linha, formato: estado,símbolo=estado(s))", 
#                                  value="q0,a=q1\nq0,b=q0\nq1,a=q2\nq1,b=q1\nq2,a=q2\nq2,b=q2")

# test_words_input = st.text_area("Palavras de teste para verificação de equivalência (separadas por vírgulas)", value="a, ab, aab, aa")

# if st.button("Executar"):
#     states_list = states.split(",")
#     alphabet_list = alphabet.split(",")
#     final_states_list = final_states.split(",")

#     transitions = {}
#     for line in transitions_input.split("\n"):
#         state, transition = line.split("=")
#         source_state, symbol = state.split(",")
#         target_states = transition.split(",")
#         if option == "Criar AFN" or option == "Converter AFN para AFD":
#             if source_state not in transitions:
#                 transitions[source_state] = {}
#             if symbol not in transitions[source_state]:
#                 transitions[source_state][symbol] = []
#             transitions[source_state][symbol].extend(target_states)
#         else:
#             if source_state not in transitions:
#                 transitions[source_state] = {}
#             transitions[source_state][symbol] = target_states[0]

#     if option == "Criar AFD":
#         afd = AFD(states_list, alphabet_list, initial_state, final_states_list, transitions)
#         st.write("AFD Criado")
#         st.graphviz_chart(render_automaton(afd))

#     elif option == "Criar AFN":
#         afn = AFN(states_list, alphabet_list, initial_state, final_states_list, transitions)
#         st.write("AFN Criado")
#         st.graphviz_chart(render_automaton(afn))

#     elif option == "Converter AFN para AFD":
#         afn = AFN(states_list, alphabet_list, initial_state, final_states_list, transitions)
#         afd = afn_to_afd(afn)
#         st.write("AFN Convertido para AFD")
#         st.graphviz_chart(render_automaton(afd))

#     elif option == "Minimizar AFD":
#         afd = AFD(states_list, alphabet_list, initial_state, final_states_list, transitions)
#         minimized_afd = minimize_afd(afd)
#         st.write("AFD Minimizado")
#         st.graphviz_chart(render_automaton(minimized_afd))

#     elif option == "Verificar Equivalência":
#         afn = AFN(states_list, alphabet_list, initial_state, final_states_list, transitions)
#         afd = afn_to_afd(afn)
#         minimized_afd = minimize_afd(afd)
#         test_words = test_words_input.split(",")
#         equivalent = check_equivalence(afn, minimized_afd, test_words)
#         st.write(f"Os autômatos são {'equivalentes' if equivalent else 'não equivalentes'} para as palavras de teste fornecidas.")
































# import sys
# import os
# import streamlit as st
# import graphviz

# # Adiciona o diretório raiz do projeto ao sys.path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# from afd import AFD
# from afn import AFN
# from operations import afn_to_afd, afd_to_afn, check_equivalence, minimize_afd

# test_words_input = st.text_area("Palavras de teste para verificação de equivalência (separadas por vírgulas)", value="a, ab, aab, aa")

# def parse_transitions(transitions_input):
#     transitions = {}
#     for line in transitions_input.split("\n"):
#         if line.strip():  # Verifica se a linha não está vazia
#             parts = line.split("=")
#             if len(parts) == 2:
#                 state_symbol, results = parts[0].strip(), parts[1].strip()
#                 symbol_result = results.split(',')
#                 if len(symbol_result) == 2:
#                     state, symbol = state_symbol.split(',')
#                     state = state.strip()
#                     symbol = symbol.strip()
#                     targets = symbol_result[1].strip().split('|')
#                     if state not in transitions:
#                         transitions[state] = {}
#                     transitions[state][symbol] = targets
#     return transitions


# def render_automaton(automaton):
#     dot = graphviz.Digraph()
#     dot.attr(rankdir='LR')
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

# option = st.selectbox("Escolha a operação", ("Criar AFD", "Criar AFN", "Converter AFN para AFD", "Converter AFD para AFN", "Minimizar AFD", "Verificar Equivalência", "Renderizar Autômato"))

# states = st.text_input("Estados (separados por vírgulas)", value="q0, q1, q2")
# alphabet = st.text_input("Alfabeto (separados por vírgulas)", value="a, b")
# initial_state = st.text_input("Estado Inicial", value="q0")
# final_states = st.text_input("Estados Finais (separados por vírgulas)", value="q2")
# transitions_input = st.text_area("Transições (um por linha, formato: estado,símbolo=estado(s))", value="q0,a=q1\nq0,b=q0\nq1,a=q2\nq1,b=q1\nq2,a=q2\nq2,b=q2")

# if st.button("Executar"):
#     states_list = states.split(",")
#     alphabet_list = alphabet.split(",")
#     final_states_list = final_states.split(",")
#     transitions = parse_transitions(transitions_input)

#     if option == "Criar AFD":
#         afd = AFD(states_list, alphabet_list, initial_state, final_states_list, transitions)
#         st.write("AFD Criado")
#         st.graphviz_chart(render_automaton(afd))
#     elif option == "Criar AFN":
#         afn = AFN(states_list, alphabet_list, initial_state, final_states_list, transitions)
#         st.write("AFN Criado")
#         st.graphviz_chart(render_automaton(afn))
#     elif option == "Converter AFN para AFD":
#         afn = AFN(states_list, alphabet_list, initial_state, final_states_list, transitions)
#         afd = afn_to_afd(afn)
#         st.write("AFN Convertido para AFD")
#         st.graphviz_chart(render_automaton(afd))
#     elif option == "Converter AFD para AFN":
#         afd = AFD(states_list, alphabet_list, initial_state, final_states_list, transitions)
#         afn = afd_to_afn(afd)
#         st.write("AFD Convertido para AFN")
#         st.graphviz_chart(render_automaton(afn))
#     elif option == "Minimizar AFD":
#         afd = AFD(states_list, alphabet_list, initial_state, final_states_list, transitions)
#         minimized_afd = minimize_afd(afd)
#         st.write("AFD Minimizado")
#         st.graphviz_chart(render_automaton(minimized_afd))
#     elif option == "Verificar Equivalência":
#         afn = AFN(states_list, alphabet_list, initial_state, final_states_list, transitions)
#         afd = afn_to_afd(afn)
#         test_words = test_words_input.split(",")
#         equivalent = check_equivalence(afn, afd, test_words)
#         st.write(f"Os autômatos são {'equivalentes' if equivalent else 'não equivalentes'} para as palavras de teste fornecidas.")

























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
#         parts = line.split("=")
#         if len(parts) == 2:
#             state_symbol, result = parts[0].strip(), parts[1].strip()
#             state, symbol = state_symbol.split(',')
#             targets = result.split('|')
#             if state.strip() not in transitions:
#                 transitions[state.strip()] = {}
#             transitions[state.strip()][symbol.strip()] = targets
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
