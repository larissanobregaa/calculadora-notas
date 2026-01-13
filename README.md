# 🎓 Calculadora Acadêmica

Um Web App desenvolvido em Python com o framework Streamlit, projetado para auxiliar estudantes do Ibmec na gestão de suas metas e notas acadêmicas. A interface foi otimizada para dispositivos móveis, garantindo agilidade no uso cotidiano.

### ✨ Funcionalidades

O projeto oferece duas ferramentas principais organizadas em abas:
1. **Simulador de Nota:** Calcula automaticamente a nota necessária na AP2 para atingir a média mínima de 7.0 e garantir a aprovação direta, sem necessidade de Prova Substitutiva (AS).

2. **Cálculo de Média Final:** Processa as notas de AP1, AP2 e AC para fornecer a média final exata e o status de aprovação do aluno.

### 🛠️ Tecnologias e Lógica
- **Python:** Linguagem base para o processamento dos dados.

- **Streamlit:** Utilizado para a criação da interface web e deploy.

- **CSS Customizado:** Aplicado para garantir que as abas sejam nítidas no celular e o rodapé permaneça estável.

- **Lógica de Cálculo:** Implementação da fórmula ponderada institucional: $$Média = (0.4 \times AP1) + (0.4 \times AP2) + (0.2 \times AC)$$

### 🚀 Como acessar
A aplicação está disponível online através do Streamlit Cloud: 👉


#### Como rodar localmente:
1. Instale o Streamlit: `pip install streamlit`

2. Execute o comando: `python -m streamlit run app.py`