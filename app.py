import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Calculadora de Notas", page_icon="🎓", layout="centered")

# 2. CSS Ajustado
st.markdown("""
    <style>
    /* Estilo das abas */
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        padding: 0px 30px;
        font-size: 18px;
        border-radius: 8px;
    }
    
    [data-testid="stCaptionContainer"] {
        color: #262730 !important;
        font-weight: 500;
        opacity: 1; 
    }

    /* Estilo do Rodapé */
    .footer {
        text-align: center;
        color: #888;
        font-size: 14px;
        padding-top: 50px;
        padding-bottom: 20px;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Calculadora Acadêmica")

# Criando as abas
tab1, tab2 = st.tabs(["Quanto preciso tirar?", "Calcular Nota Final"])

# Aba 1: Quanto preciso tirar?
with tab1:
    st.markdown("### Simulador de Notas")
    # Texto explicativo sobre a média 7.0
    st.caption("ℹ️ Cálculo baseado na média mínima **7.0** para aprovação direta (sem necessidade de AS).")
    
    ap1_n = st.number_input("Digite sua nota da AP1", 0.0, 10.0, step=0.1, key="nota_ap1")
    ac_n = st.number_input("Digite sua nota da AC", 0.0, 10.0, step=0.1, key="notaa_ac")
    
    # Lógica para mostrar apenas se houver algum valor inserido
    if ap1_n > 0 or ac_n > 0:
        # Fórmula inversa para atingir a nota 7.0
        nota_necessaria = (7.0 - (0.4 * ap1_n) - (0.2 * ac_n)) / 0.4
        
        st.divider()
        if nota_necessaria <= 0:
            st.success("🎉 Com essas notas, você já atingiu a média 7.0!")
        elif nota_necessaria > 10:
            st.error(f"Nota necessária na AP2: {nota_necessaria:.1f}. Mesmo com 10 na AP2, você precisará de AS.")
        else:
            st.metric("Sua nota na AP2 para passar direto é:", f"{nota_necessaria:.1f}")
    else:
        st.info("Insira suas notas para calcular a nota necessária para aprovação direta.")

# Aba 2: Calcular Nota Final
with tab2:
    st.markdown("### Minha Média Final")
    col1, col2 = st.columns(2)
    with col1:
        f_ap1 = st.number_input("Nota AP1", 0.0, 10.0, step=0.1, key="f_ap1")
        f_ac = st.number_input("Nota AC", 0.0, 10.0, step=0.1, key="f_ac")
    with col2:
        f_ap2 = st.number_input("Nota AP2", 0.0, 10.0, step=0.1, key="f_ap2")
    
    # Lógica para mostrar apenas se AP1 ou AP2 tiverem valor
    if f_ap1 > 0 or f_ap2 > 0:
        media_final = (0.4 * f_ap1) + (0.4 * f_ap2) + (0.2 * f_ac)
        
        st.divider()
        st.metric("Média Final:", f"{media_final:.1f}")
        if media_final >= 7.0:
            st.success("Aprovado! ✅")
        else:
            st.warning("Média abaixo de 7.0. Você precisará fazer a prova de AS!.✍️")

st.markdown('<div class="footer">Desenvolvido por uma estudante para estudantes.</div>', unsafe_allow_html=True)