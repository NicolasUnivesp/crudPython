from os import write
from numpy.core.fromnumeric import size
from typing import List
import streamlit as st
import controllers.clienteController as clienteController
import models.Cliente as cliente
import pandas as pd
import streamlit.components.v1 as components
import Pages.Clientes.Create as PageIncluirCliente
import Pages.Clientes.List as PageListCliente



st.sidebar.title('Menu')
page_cliente = st.sidebar.selectbox('Cliente', ['Incluir', 'Alterar', 'Excluir', 'Consultar'])

if page_cliente == 'Consultar':
    PageListCliente.List()


if page_cliente == 'Incluir':
    PageIncluirCliente.Incluir()
