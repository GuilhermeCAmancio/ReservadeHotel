'''Uma rede de hotéis em Miami gostaria de oferecer um serviço de reservas pela internet. A
rede é composta por três hotéis: Lakewood, Bridgewood e Ridgewood. Cada hotel tem taxas
diferenciadas para dia de semana ou final de semana, incluindo taxas específicas para
participantes do programa de fidelidade. Adicionalmente, cada hotel tem uma classificação,
indicando a excelência do serviço.'''
#Imports
from http import client
from pickle import TRUE
import datetime as dt
from tabulate import tabulate
import pandas as pd
import numpy as np

def get_cheapest_hotel(numberC, dayC):   #DO NOT change the function's name
    d = []
    #min special client
    t = 0
    #print(len(dadosEspecial))
    for t in range(len(dadosEspecial)):
        #print(dia[t])
        if(Client == 2 and ((dia[t] == 'Saturday') or (dia[t] == 'Sunday'))):
            d = df2[df2.Weekend == df2.Weekend.min()]
        else:
            d = df2[df2.Week == df2.Week.min()]
    print("-------------------------------------------------------")
    print("\n")
    #min common client
    t = 0
    #print(len(dadosComum))
    for t in range(len(dadosComum)):
        #print(dia[t])
        if(Client == 1 and ((dia[t] == 'Saturday') or (dia[t] == 'Sunday'))):
            d = df1[df1.Weekend == df1.Weekend.min()]
        else:
            d = df1[df1.Week == df1.Week.min()]
    print("-------------------------------------------------------")
    print("\n")
    cheapest_hotel = d
    return cheapest_hotel

#database creation
dadosComum = {'Nome' : ["Lakewood", "Bridgewood", "Ridgewood"], 'Week' : [110, 160, 60], 'Weekend' : [90, 220, 150]}
df1 = pd.DataFrame(dadosComum)
dadosEspecial = {'Nome' : ["Lakewood", "Bridgewood", "Ridgewood"], 'Week' : [80, 110, 100], 'Weekend' : [80, 50, 40]}
df2 = pd.DataFrame(dadosEspecial)
#print(dadosComum)
#print(dadosEspecial)

#print table
col_names = ["Name", "Price Week", "Price Weekend"]
print("Cliente Comum")
print(tabulate(dadosComum, headers=col_names))
print("-------------------------------------------------------")
print("Cliente Especial")
print(tabulate(dadosEspecial, headers=col_names))
print("-------------------------------------------------------")
print("\n \n \n")

Verify = 1
Client = 0

#client select
while Verify == 1:
    print("Tipo de cliente:\n"
        "1- Comum\n"
        "2- Especial\n")
    select = input()
    print("-------------------------------------------------------")
    print("\n")
    if(int(select) == 1) or (int(select) == 2):
        Client = int(select)
        verify = 0
        break
    else:
        print("Valor inválido, escolha algo que seja válido!")
        print("-------------------------------------------------------")
        print("\n \n \n")


date_string = '25/12/2023'
format = "%d/%m/%Y"

datas = 0
verify = True
dataString = []
format = "%d/%m/%Y"

#date analysis
print('Digite as datas (dd/mm/YYYY): ')
while datas < 3:
    dd = input('Dia: ')
    mm = input('Mes: ')
    yy = input('Ano: ')
    dmy = (dd + '/' + mm + '/' + yy)
    print("-------------------------------------------------------")
    print("\n")
    try:
        ok = dt.datetime.strptime(dmy, format)
        datas += 1
        dataString.append(dmy)
    except ValueError:
        print('Inválido, tente o formato (dd/mm/YYYY)')
        print("-------------------------------------------------------")
        print("\n")

#print(dataString)

#catch week day name
dev = dataString
dia = []
for dev in dev:
    day, month, year = (int(x) for x in dev.split('/'))
    ans = dt.date(year, month, day)
    dia.append(ans.strftime("%A"))
    #print (dia)

get_cheapest_hotel(Client, dia)