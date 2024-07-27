# Projeto de Teoria da Computação

Este projeto implementa um sistema para manipular Autômatos Finitos Determinísticos (AFD) e Autômatos Finitos Não-determinísticos (AFN).

## Funcionalidades

- Recebe um AFN como entrada
- Converte um AFN em AFD
- Simula a aceitação de palavras no AFD e AFN
- Demonstra a equivalência entre AFN e AFD
- Minimização de AFDs

## Estrutura do Projeto

- `app/`: Contém toda a lógica da aplicação.
  - `app.py`: Arquivo principal da aplicação.
  - `backend/`: Lógica do backend.
    - `automatos/`: Classes e funções dos autômatos.
    - `scripts/`: Scripts executáveis.
    - `tests/`: Testes unitários.
  - `frontend/`: Lógica do frontend.
    - `app_streamlit.py`: Frontend usando Streamlit.

## Como Executar

1. Instale as dependências:
    ```
    pip install -r requirements.txt
    ```

2. Acesse o path do frontend:
    ```
    cd {seuPath}\app\frontend
    ```
3. Execute o arquivo app.py:
    ```
    streamlit run app.py
    ```
4. Seu projeto estará rodando na porta:
    ```
     http://localhost:8501/
    ```