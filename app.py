import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Calculadora de Notas", page_icon="🎓", layout="centered")

if 'reset_counter' not in st.session_state:
    st.session_state.reset_counter = 0

# 2. CSS
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab"] { 
        height: 60px; 
        padding: 0px 20px; 
        font-size: 16px; 
        border-radius: 8px; 
    }
    
    .instrucoes {
        color: #262730;
        font-size: 16px;
        margin-bottom: 20px;
        line-height: 1.6;
    }
            
    .footer { 
        text-align: center; 
        color: #888; 
        font-size: 14px; 
        padding-top: 50px; 
        padding-bottom: 20px; 
        width: 100%; 
    }

    div[data-testid="stFormSubmitButton"] {
        display: block !important;
        width: 100% !important;
    }
            
    div[data-testid="stFormSubmitButton"] > button {
        width: 100% !important;
        border-radius: 8px !important;
        height: 3.5em !important;
        font-weight: bold !important;
        margin-bottom: 10px !important;
        display: block !important;
    }       
            
    [data-testid="column"] {
        width: 100% !important;
        flex: 1 1 100% !important;
        min-width: 100% !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Calculadora Acadêmica")

tab1, tab2 = st.tabs(["Quanto preciso tirar?", "Calcular Nota Final"])

# Aba 1: Quanto preciso tirar?
with tab1:
    with st.form(key=f"simulado_{st.session_state.reset_counter}"):
        st.markdown("### Simulador de Notas")
        st.markdown(f"""
            <div class="instrucoes">
                <b>Como usar:</b> Preencha os campos abaixo e clique em <b>Calcular Nota</b>.<br>
                <span style="font-size: 14px;">
                ℹ️ <i>Cálculo baseado na média mínima <b>7.00</b> para aprovação direta.</i><br>
                Fórmula utilizada: <b>(0.4 × AP1) + (0.4 × AP2) + (0.2 × AC)</b>
                </span>
            </div>
            """, unsafe_allow_html=True)
        
        ap1 = st.text_input("Digite sua nota da AP1", placeholder="0.00", key=f"ap1_{st.session_state.reset_counter}")
        ac = st.text_input("Digite sua nota da AC", placeholder="0.00", key=f"ac_{st.session_state.reset_counter}")
        
        st.write("")

        btn_calculo1 = st.form_submit_button("Calcular Nota Necessária")
        btn_limpar1 = st.form_submit_button("Limpar Tudo")

        if btn_limpar1:
            st.session_state.reset_counter += 1
            st.rerun()

        if btn_calculo1:
            try:
                ap1 = float(ap1.replace(",", ".")) if ap1 else 0.0
                ac = float(ac.replace(",", ".")) if ac else 0.0
            
                if ap1 or ac:
                    if ap1 > 10 or ac > 10:
                        st.error("As notas devem ser entre 0 e 10.")
                    else:
                        nota_necessaria = (7.0 - (0.4 * ap1) - (0.2 * ac)) / 0.4
                        st.divider()
                        if nota_necessaria <= 0:
                            st.success("🎉 Com essas notas, você já atingiu a média 7.0!")
                        elif nota_necessaria > 10:
                            st.error(f"Nota necessária na AP2: {nota_necessaria:.2f}. Mesmo com 10 na AP2, você precisará de AS.")
                        else:
                            st.metric("Sua nota na AP2 para passar direto é:", f"{nota_necessaria:.2f}")
                else:
                    st.info("Insira suas notas para calcular a nota necessária para aprovação direta.")
            except ValueError:
                st.warning("Por favor, insira valores numéricos válidos para AP1 e AC.")


# Aba 2: Calcular Nota Final e AS
with tab2:
    with st.form(key=f"final_{st.session_state.reset_counter}"):
        st.markdown("### Minha Média Final")
        st.markdown("""
            <div class="instrucoes">
                Insira todas as suas notas obtidas para verificar sua situação final e 
                necessidade de <b>Avaliação Substitutiva (AS)</b>.
            </div>
            """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            final_ap1 = st.text_input("Nota AP1", placeholder="0.00", key=f"final_ap1_{st.session_state.reset_counter}")
            final_ac = st.text_input("Nota AC", placeholder="0.00", key=f"final_ac_{st.session_state.reset_counter}")
        with col2:
            final_ap2 = st.text_input("Nota AP2", placeholder="0.00", key=f"final_ap2_{st.session_state.reset_counter}")

        st.write("")    

        btn_calculo2 = st.form_submit_button("Calcular Média Final")
        btn_limpar2 = st.form_submit_button("Limpar Tudo")

        if btn_limpar2:
            st.session_state.reset_counter += 1
            st.rerun()
        
        if btn_calculo2:
            try:
                final_ap1 = float(final_ap1.replace(",", ".")) if final_ap1 else 0.0
                final_ap2 = float(final_ap2.replace(",", ".")) if final_ap2 else 0.0
                final_ac = float(final_ac.replace(",", ".")) if final_ac else 0.0
                
                if final_ap1 or final_ap2:
                    if final_ap1 > 10 or final_ap2 > 10 or final_ac > 10:
                        st.error("As notas devem ser entre 0 e 10.")
                    else:
                        media_final = (0.4 * final_ap1) + (0.4 * final_ap2) + (0.2 * final_ac)
                        st.divider()
                        st.metric("Média Final Atual:", f"{media_final:.2f}")    
                    
                        if media_final >= 7.0:
                            st.success("Aprovado!✅")
                        else:
                            st.warning("Média abaixo de 7.0. Você precisará fazer a prova de AS! ✍️")
                            
                            # Cálculo para a AS (avaliação substitutiva)
                            # 1. Descobrimos a maior entre AP1 e AP2 (a menor será substituída)
                            maior_nota = max(final_ap1, final_ap2)
                            
                            # 2. Calculamos quanto falta para chegar em 7.0 usando a maior nota + AC
                            # Fórmula: 7.0 = (0.4 * maior_nota) + (0.4 * AS) + (0.2 * AC)
                            nota_as_necessaria = (7.0 - (0.4 * maior_nota) - (0.2 * final_ac)) / 0.4
                            
                            st.markdown("#### 🎯 Projeção para a AS")
                            if nota_as_necessaria > 10:
                                media_maxima = (0.4 * maior_nota) + (0.4 * 10) + (0.2 * final_ac)
                                st.error(f"Nota necessária na AS: {nota_as_necessaria:.2f}")
                                st.write(f"Infelizmente, mesmo com 10 na AS, sua média máxima seria **{media_maxima:.2f}**.")
                            elif nota_as_necessaria <= 0:
                                st.success("Sua nota atual já é suficiente se você fizer a AS!")
                            else:
                                st.info(f"Para atingir a média 7.0, você precisa tirar **{nota_as_necessaria:.2f}** na prova de AS.")
                                st.caption(f"*(O cálculo considera que a AS substituirá sua nota mais baixa, que hoje é {min(final_ap1, final_ap2):.2f})*.\n\n"
                                        f"**Observação:** A AS só substitui as notas da AP1 ou AP2, a nota de AC não é substituída!")
                else:
                    st.info("Insira suas notas de AP1, AP2 e AC para ver sua média final.")
            except ValueError:
                st.warning("Por favor, insira valores numéricos válidos para AP1, AP2 e AC.")

st.write("")
st.divider()
st.markdown(" ###### 📢 Gostou da calculadora? Compartilhe com seus colegas!")

col_share1, col_share2 = st.columns(2)

with col_share1:
    link_projeto = "https://calculadora-notas.streamlit.app/" 
    st.info(f"🔗 **Link do App:** \n{link_projeto}")

with col_share2:
    texto_wa = f"Oii! Descobri essa calculadora de notas que ajuda a calcular as notas. Olha só: {link_projeto}"
    link_wa = f"https://wa.me/?text={texto_wa.replace(' ', '%20')}"
    st.markdown(f' <a href="{link_wa}" target="_blank"><button style="width:100%; border-radius:8px; height:3.5em; background-color:#25D366; color:white; border:none; font-weight:bold; cursor:pointer;"> Enviar no WhatsApp</button></a>', unsafe_allow_html=True)
    
st.markdown('<div class="footer">Desenvolvido por uma estudante para estudantes.</div>', unsafe_allow_html=True)