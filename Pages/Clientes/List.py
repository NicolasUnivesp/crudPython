from typing import List
import streamlit as st
import controllers.clienteController as clienteController
import pandas as pd

def List():
    st.title("Clientes")
    costumerList = []

    for item in clienteController.SelecionarTodos():
        costumerList.append([item.id, item.nome, item.idade, item.profissao])

    df = pd.DataFrame(
        costumerList,
        columns=['id', 'Nome', 'Idade', 'Profissão']
    )
    st.table(df)