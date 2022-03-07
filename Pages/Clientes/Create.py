
from typing import List
import streamlit as st
import controllers.clienteController as clienteController
import models.Cliente as cliente


def Incluir():
    st.title("Incluir clientes")

    with st.form(key="include_cliente"):
        input_name = st.text_input(label="Insira o seu nome: ")
        input_age = st.number_input(label="Insira sua idade: ", format="%d",
                                    step=1)  # o %d é para formatar o numero como um inteiro! ou %e
        input_occupation = st.selectbox(label="Selecione sua profissão: ",
                                        options=["Desenvolvedor", "Músico", "Professor"])
        input_button_submit = st.form_submit_button("Enviar")
        input_button_visualisar = st.form_submit_button("Visualisar Clientes")

    if input_button_submit:
        clienteController.incluir(cliente.Cliente(0, input_name, input_age, input_occupation))
        st.success("Cliente incluido com sucesso!")




