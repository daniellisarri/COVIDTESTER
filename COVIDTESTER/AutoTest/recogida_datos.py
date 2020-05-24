import requests

def recoger_datos():
    response = requests.get('https://api.covid19tracking.narrativa.com/api/2020-05-24/country/spain/region/navarra')
    
    confirmados = response.json()["dates"]["2020-05-24"]["countries"]["Spain"]["regions"][0]["today_confirmed"]
    hospitalizados = response.json()["dates"]["2020-05-24"]["countries"]["Spain"]["regions"][0]["today_intensive_care"]
    muertes = response.json()["dates"]["2020-05-24"]["countries"]["Spain"]["regions"][0]["today_deaths"]
    recuperados = response.json()["dates"]["2020-05-24"]["countries"]["Spain"]["regions"][0]["today_recovered"]
    
    datos = {
        "confirmados":confirmados, 
        "hospitalizados":hospitalizados,
        "muertes":muertes,
        "recuperados":recuperados}

    return datos