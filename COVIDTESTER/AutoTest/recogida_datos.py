import requests
import datetime

def recoger_datos():

    fecha = datetime.datetime.today() + datetime.timedelta(days=-1) # Coge el día anterior para evitar errores
    fecha_formateada = fecha.strftime("%Y-%m-%d")

    url = 'https://api.covid19tracking.narrativa.com/api/'+fecha_formateada+'/country/spain/region/navarra'
    
    response = requests.get(url)
    
    confirmados = response.json()["dates"][fecha_formateada]["countries"]["Spain"]["regions"][0]["today_confirmed"]
    hospitalizados = response.json()["dates"][fecha_formateada]["countries"]["Spain"]["regions"][0]["today_intensive_care"]
    muertes = response.json()["dates"][fecha_formateada]["countries"]["Spain"]["regions"][0]["today_deaths"]
    recuperados = response.json()["dates"][fecha_formateada]["countries"]["Spain"]["regions"][0]["today_recovered"]
    fecha_actualizacion = response.json()["dates"][fecha_formateada]["countries"]["Spain"]["regions"][0]["date"]
    
    datos = {
        "confirmados":confirmados, 
        "hospitalizados":hospitalizados,
        "muertes":muertes,
        "recuperados":recuperados,
        "fecha_actualizacion":fecha_actualizacion}

    return datos