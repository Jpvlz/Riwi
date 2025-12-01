import requests
import json
from datetime import datetime

# Constantes
API_KEY = "dc0787662401ca3a715b01f866ee8e32"  #API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def obtener_clima(ciudad):
    """
    Obtiene los datos meteorológicos de una ciudad
    """
    # Parámetros de la consulta
    params = {
        'q': ciudad,
        'appid': API_KEY,
        'units': 'metric',  # Para obtener temperatura en Celsius
        'lang': 'es'  # Para descripciones en español
    }
    
    try:
        # Realizar la petición
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Lanza excepción si hay error HTTP
        
        return response.json()
    
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(f"❌ Error: No se encontró la ciudad '{ciudad}'")
        elif response.status_code == 401:
            print("❌ Error: API key inválida")
        else:
            print(f"❌ Error HTTP: {e}")
        return None
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")
        return None

def mostrar_clima(datos):
    """
    Muestra los datos meteorológicos de forma legible
    """
    if not datos:
        return
    
    # Extraer datos importantes
    ciudad = datos['name']
    pais = datos['sys']['country']
    temperatura = datos['main']['temp']
    sensacion = datos['main']['feels_like']
    temp_min = datos['main']['temp_min']
    temp_max = datos['main']['temp_max']
    humedad = datos['main']['humidity']
    presion = datos['main']['pressure']
    descripcion = datos['weather'][0]['description'].capitalize()
    viento = datos['wind']['speed']
    nubosidad = datos['clouds']['all']
    
    # Amanecer y atardecer
    amanecer = datetime.fromtimestamp(datos['sys']['sunrise']).strftime('%H:%M')
    atardecer = datetime.fromtimestamp(datos['sys']['sunset']).strftime('%H:%M')
    
    # Mostrar información
    print("\n" + "="*50)
    print(f"🌍 CLIMA EN {ciudad.upper()}, {pais}")
    print("="*50)
    print(f"\n🌡️  TEMPERATURA")
    print(f"   Actual:        {temperatura}°C")
    print(f"   Sensación:     {sensacion}°C")
    print(f"   Mínima:        {temp_min}°C")
    print(f"   Máxima:        {temp_max}°C")
    
    print(f"\n☁️  CONDICIONES")
    print(f"   Descripción:   {descripcion}")
    print(f"   Nubosidad:     {nubosidad}%")
    print(f"   Humedad:       {humedad}%")
    print(f"   Presión:       {presion} hPa")
    
    print(f"\n💨 VIENTO")
    print(f"   Velocidad:     {viento} m/s")
    
    print(f"\n🌅 SOL")
    print(f"   Amanecer:      {amanecer}")
    print(f"   Atardecer:     {atardecer}")
    
    # Visibilidad (si está disponible)
    if 'visibility' in datos:
        visibilidad = datos['visibility'] / 1000  # Convertir a km
        print(f"\n👁️  VISIBILIDAD")
        print(f"   {visibilidad} km")
    
    # Lluvia (si está disponible)
    if 'rain' in datos:
        if '1h' in datos['rain']:
            print(f"\n🌧️  LLUVIA")
            print(f"   Última hora:   {datos['rain']['1h']} mm")
    
    print("\n" + "="*50 + "\n")

def main():
    """
    Función principal
    """
    print("\n╔════════════════════════════════════════╗")
    print("║     CONSULTA DEL CLIMA ACTUAL          ║")
    print("╚════════════════════════════════════════╝\n")
    
    while True:
        # Solicitar ciudad al usuario
        ciudad = input("Ingresa el nombre de la ciudad (o 'salir' para terminar): ").strip()
        
        if ciudad.lower() == 'salir':
            print("\n👋 ¡Hasta luego!\n")
            break
        
        if not ciudad:
            print("⚠️  Por favor ingresa un nombre válido\n")
            continue
        
        # Obtener y mostrar datos
        datos = obtener_clima(ciudad)
        mostrar_clima(datos)

if __name__ == "__main__":
    main()