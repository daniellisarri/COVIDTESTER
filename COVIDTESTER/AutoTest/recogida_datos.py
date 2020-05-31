import requests
import datetime

# Devuelve los datos recogidos de la API 
def recoger_datos():

    # Fecha de ayer, con formato americano, para evitar errores en primeras horas del día
    fecha = datetime.datetime.today() + datetime.timedelta(days=-1) 
    fecha_formateada = fecha.strftime("%Y-%m-%d")

    # Petición GET a la API de datos
    url = 'https://api.covid19tracking.narrativa.com/api/'+fecha_formateada+'/country/spain/region/navarra'
    
    # Recogida de la respuesta (es un JSON)
    response = requests.get(url)
    
    # Recogida de datos concretos de interés
    confirmados = response.json()["dates"][fecha_formateada]["countries"]["Spain"]["regions"][0]["today_confirmed"]
    hospitalizados = response.json()["dates"][fecha_formateada]["countries"]["Spain"]["regions"][0]["today_intensive_care"]
    muertes = response.json()["dates"][fecha_formateada]["countries"]["Spain"]["regions"][0]["today_deaths"]
    recuperados = response.json()["dates"][fecha_formateada]["countries"]["Spain"]["regions"][0]["today_recovered"]
    fecha_actualizacion = response.json()["dates"][fecha_formateada]["countries"]["Spain"]["regions"][0]["date"]
    
    # Retorna los datos como diccionario
    datos = {
        "confirmados":confirmados, 
        "hospitalizados":hospitalizados,
        "muertes":muertes,
        "recuperados":recuperados,
        "fecha_actualizacion":fecha_actualizacion}
    return datos