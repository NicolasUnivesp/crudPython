import pyodbc

server = 'FORABOLSONARO\SQLEXPRESS'
database = 'clientes'
username = 'sa'
password = 'root'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
