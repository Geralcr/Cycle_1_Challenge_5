# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 21:35:24 2020

@author: Geraldine Claros
"""
import pandas as pd

def caso_who(ruta_archivo_csv: str)-> dict: 
   
    if ruta_archivo_csv[-3:] == "csv":
        
        try:
            data =  pd.DataFrame(pd.read_csv(ruta_archivo_csv))
        except:
            return "Error al leer el archivo de datos."
        
        data['date'] = pd.to_datetime(data['date'])
        
        data['rate'] = (((data['total_cases_per_million'] * data['population'])/1000000) / (((data['hospital_beds_per_thousand']* data['population'])/1000)))
        
        data.rate.name = "rate"
        
        continent = data.continent
        date = data.date
        rate = data.rate
        
        df_respuesta = pd.concat([continent,date,rate] , axis = 1 )
        
        df_respuesta = df_respuesta.groupby(['date','continent']).rate.mean().unstack()
        
        return df_respuesta.to_dict()
    
    else:
        return "Extensión inválida."

      
    
print(caso_who("https://raw.githubusercontent.com/tikuro/Covid/main/owid-covid-data.csv"))

