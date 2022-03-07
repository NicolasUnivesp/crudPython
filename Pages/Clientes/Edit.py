#
# from typing import List
# import streamlit as st
# import controllers.clienteController as clienteController
# import pandas as pd
#
# def Edit():
#     st.title("Alterar cliente")
#     costumerList = []
#
#     for item in clienteController.SelecionarTodos():
#         costumerList.append([item.id, item.nome, item.idade, item.profissao])
#
#     df = pd.DataFrame(
#         costumerList,
#         columns=['id', 'Nome', 'Idade', 'Profissão']
#     )
#     st.table(df)

# UPDATE TBEXEMPLO SET VALOR = 120 WHERE ID = '2006';