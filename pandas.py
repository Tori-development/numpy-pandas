import pandas as pd
import numpy as np
from scipy import stats
import xlsxwriter


#1.my dataframe
frameExample = {"equipos":{"1":"Santos Laguna","2":"León","3":"Tigres","4":"Querétaro","5":"Necaxa","6":"América","7":"Monarcas Morelia","8":"Monterrey"
    ,"9":"Pachuca","10":"Chivas","11":"Club Tijuana","12":"Cruz Azul","13":"Pumas UNAM","14":"Atlas","15":"Atlético San Luis","16":"FC Juárez"
    ,"17":"Toluca","18":"Puebla","19":"Veracruz"}
        }

df = pd.DataFrame(frameExample, columns = ['equipos'])

#2.first 5 rows
print("first 5 rows",df.head())


print("10 last rows",df.tail(10))
#3.ten last registers

#4.headers
print(df.columns.values)

#5.getting the
keyValues = df.equipos.keys()

#6.Transformar la columna de posicion a un arreglo de numpy
a = []
for num in keyValues :
    print(num)
    a.append(int(num))

aNumpy = np.array(a)
print(a)

#7.Mostrar estadistica descriptiva de los valores
print(stats.describe(aNumpy))

#8. Ordenar valores alfabeticamente
df.sort_values(by=['equipos'], inplace=True)
print (df)

#9.Guardar valores a un csv
pd.DataFrame(df).to_csv("Accepted.csv",index=False)

#10.Cargar algun excel de los disponibles en GDrive
df.to_excel('example.xlsx', sheet_name='example')
print("numbre 10",df)
#11.Cortar un dataframe de 3x4 a partir del anterior

#12.Cargar el json q se encuentra al final de esta pagina
jsonTest = {"Product":{"0":"Desktop Computer","1":"Tablet","2":"iPhone","3":"Laptop"},"Price":{"0":700,"1":250,"2":800,"3":1200}}

#12. Imprimir dataframe resultante del json
df2 = pd.DataFrame(jsonTest, columns = ['Product','Price'])
#13. Imprimir dataframe resultante del json
print("jsonValues: ",df2)

#Guardar a un XLS

# 14. Guardar a un XLS
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df2.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
# ----------Guardar a un XLS---------

#15.Cargar el resultado de este ws en un dataframe https://api.exchangeratesapi.io/latest e imprimirlo

jsonWs = {"rates":{"CAD":1.4495,"HKD":8.4658,"ISK":137.9,"PHP":55.061,"DKK":7.4721,"HUF":337.93,"CZK":24.965,"AUD":1.626,"RON":4.7693,"SEK":10.5373,"IDR":14919.11,"INR":77.6945,"BRL":4.6995,"RUB":69.3198,"HRK":7.459,"JPY":119.73,"THB":34.082,"CHF":1.0667,"SGD":1.5127,"PLN":4.2569,"BGN":1.9558,"TRY":6.5775,"CNY":7.6025,"NOK":10.0953,"NZD":1.7055,"ZAR":16.2331,"USD":1.0901,"MXN":20.3563,"ILS":3.72,"GBP":0.84325,"KRW":1290.63,"MYR":4.5059},"base":"EUR","date":"2020-02-11"}

df3 = pd.DataFrame(jsonWs, columns = ['rates'])

print(df3)