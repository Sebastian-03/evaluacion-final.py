import pandas as pd
import sqlite3 as sq3
import datetime
import controller as ctler

df=pd.read_excel('python\datatienda.evalu',sheet_name="datatienda",header=0)
values=df.values.tolist()
c=sq3.connect('python/tienda.db')
pointer=c.cursor()
pointer.executemany("INSERT INTO TABLAPRODUCTOS (ORDER_ID,	PRICE_TOTAL,PRODUCT_ID,	NAME,NROSERIE,CANTIDAD,	PRODUCT,PRICE_UNIT,CATEGORIA,STOCK_ACUTAL,DATE,USER_ADMIN,USER_CLIENT")
print("Los datos son:")
c.commit()
c.close()

