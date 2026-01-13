import streamlit as st

# Configuração da página e ícone
st.set_page_config(page_title="Calculadora de Notas", page_icon="🎓", layout="centered")

# Customização de Layout (CSS Minimalista)
st.markdown("""
    <style>
    .stApp { background-color: #fcfcfc; }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] { 
        height: 45px; 
        border-radius: 8px; 
        background-color: #f0f2f6; 
        font-weight: bold;
    }
    .stTabs [aria-selected="true"] { background-color: #007bff; color: white; }
    div[data-testid="stMetricValue"] { font-size: 45px; color: #007bff; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎓 Calculadora de Notas")
st.caption("Layout Simples & Funcional")


tab1, tab2 = st.tabs(["Quanto preciso tirar?", "Calcular Nota Final"])

# OPÇÃO 1: Quanto preciso tirar?
with tab1:
    st.markdown("### 🎯 Simulador de Meta")
    st.write("Ajuste as notas que você já possui:")
    
    ap1_m = st.slider("Nota da AP1", 0.0, 10.0, 5.0, step=0.1, key="m1")
    ac_m = st.slider("Nota da AC", 0.0, 10.0, 5.0, step=0.1, key="m2")
    
    # Cálculo inverso
    nota_necessaria = (7.0 - (0.4 * ap1_m) - (0.2 * ac_m)) / 0.4
    
    st.divider()
    
    if nota_necessaria <= 0:
        st.success("**Você já está aprovado!** 🎉")
        st.balloons()
    elif nota_necessaria > 10:
        st.error(f"**Atenção:** Você precisaria de {nota_necessaria:.1f} na AP2. Foco na AS!")
    else:
        st.metric("Sua nota para a AP2 é:", f"{nota_necessaria:.1f}")
        st.info("A média para passar sem AS é 7.0")

# OPÇÃO 2: Calcular Nota Final
with tab2:
    st.markdown("### 📝 Minha Média Final")
    st.write("Insira as notas das três avaliações:")
    
    # Aqui usamos campos numéricos para precisão total
    col1, col2 = st.columns(2)
    with col1:
        f_ap1 = st.number_input("Nota AP1", 0.0, 10.0, step=0.1, key="f1")
        f_ac = st.number_input("Nota AC", 0.0, 10.0, step=0.1, key="f2")
    with col2:
        f_ap2 = st.number_input("Nota AP2", 0.0, 10.0, step=0.1, key="f3")
    
    media_final = (0.4 * f_ap1) + (0.4 * f_ap2) + (0.2 * f_ac)
    
    st.divider()
    
    if media_final >= 7.0:
        st.metric("Média Final:", f"{media_final:.1f}")
        st.success("Parabéns! Você está aprovado! ✅")
    else:
        st.metric("Média Final:", f"{media_final:.1f}")
        st.warning("Você precisará fazer a prova de AS! ✍️")

st.markdown("---")
st.caption("Desenvolvido por uma estudante para estudantes.")