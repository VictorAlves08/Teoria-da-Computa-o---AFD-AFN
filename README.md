# Projeto de Teoria da Computação

Este projeto implementa um sistema para manipular Autômatos Finitos Determinísticos (AFD) e Autômatos Finitos Não-determinísticos (AFN).
![demo_sin131](https://github.com/user-attachments/assets/f2efa14c-2d3e-4fa7-8e28-d4a5b00a319b)
## Funcionalidades

- Recebe um AFD ou AFN como entrada
- Converte um AFN em AFD
- Simula a aceitação de palavras no AFD e AFN
- Demonstra a equivalência entre AFN e AFD
- Minimização de AFDs

## Estrutura do Projeto

- `app/`: Contém toda a lógica da aplicação.
  - `backend/`: Lógica do backend.
    - `abstract/`
    - `automatos/`
  - `frontend/`: Lógica do frontend.
    - `app.py`
    - `automata_app.py`

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
