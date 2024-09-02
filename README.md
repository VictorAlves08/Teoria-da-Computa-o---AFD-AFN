<div align="center">
  <h1>Projeto de Teoria da Computação</h1>
</div>

Este projeto implementa um sistema para manipular Autômatos Finitos Determinísticos (AFD) e Autômatos Finitos Não-determinísticos (AFN). Ele permite a conversão, simulação e minimização de autômatos, demonstrando a equivalência entre AFN e AFD, assim como a manipulação de uma Máquina de Turing (MT), possibilitando a verificação de uma palavra em uma determinada linguagem.

![Demonstração do Projeto](https://github.com/user-attachments/assets/f2efa14c-2d3e-4fa7-8e28-d4a5b00a319b)

## ✨ Funcionalidades

- ✨ Recebe um AFD ou AFN como entrada
- 🔄 Converte um AFN em AFD
- 🎯 Simula a aceitação de palavras em AFDs e AFNs
- 🔍 Demonstra a equivalência entre AFN e AFD
- 🛠️ Minimização de AFDs para otimização
- 📜 Reconhecimento de palavras pela Máquina de Turing

## 🗂️ Arquitetura do Projeto

- `app/`: Contém toda a lógica da aplicação.
  - `backend/`: Lógica do backend.
    - `abstract/`: Abstrações e classes base.
    - `automatos/`: Implementações dos autômatos.
    - `turing_machine/`: Implementação da máquina de turing
  - `frontend/`: Lógica do frontend e interface do usuário.
    - `app.py`: Arquivo principal para execução da interface.
    - `automata_app.py`: Lógica da aplicação de autômatos.
- `utils/`: Arquivos Utilitários

## 🚀 Como Executar

1. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

2. Navegue até o diretório do frontend:
    ```bash
    cd {seuPath}\app\frontend
    ```

3. Execute o arquivo `app.py`:
    ```bash
    streamlit run app.py
    ```

4. Acesse a aplicação no seu navegador:
    ```bash
    http://localhost:8501/
    ```

## 🎓 Autores

Este projeto foi desenvolvido como parte da disciplina de Teoria da Computação pela Universidade Federal de Viçosa, campus Rio Paranaíba, por:

- **Victor Oliveira**
  - [LinkedIn](https://www.linkedin.com/in/victor-alves-de-oliveira/)
  - [GitHub](https://github.com/VictorAlves08)

- **Gabriel Mota**
  - [LinkedIn](https://www.linkedin.com/in/gabriel-mota-a58899185/)
  - [GitHub](https://github.com/gslmota)
