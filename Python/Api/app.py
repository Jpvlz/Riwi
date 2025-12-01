from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Tu API key de OpenWeatherMap
API_KEY = "dc0787662401ca3a715b01f866ee8e32"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# =====================================
# Ruta de prueba
# =====================================
@app.route("/")
def home():
    return jsonify({"mensaje": "API de Clima funcionando correctamente"})


# =====================================
# GET: Clima de una ciudad
# =====================================
@app.route("/clima/<ciudad>", methods=["GET"])
def obtener_clima(ciudad):
    try:
        # Armar la URL con la ciudad y tu API Key
        url = f"{BASE_URL}?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza excepción si hay error HTTP

        datos = respuesta.json()

        # Crear un JSON limpio con los datos relevantes
        resultado = {
            "ciudad": datos.get("name"),
            "pais": datos.get("sys", {}).get("country"),
            "clima": datos.get("weather", [{}])[0].get("main"),
            "descripcion": datos.get("weather", [{}])[0].get("description"),
            "temperatura": datos.get("main", {}).get("temp"),
            "sensacion_termica": datos.get("main", {}).get("feels_like"),
            "temperatura_min": datos.get("main", {}).get("temp_min"),
            "temperatura_max": datos.get("main", {}).get("temp_max"),
            "humedad": datos.get("main", {}).get("humidity"),
            "presion": datos.get("main", {}).get("pressure"),
            "velocidad_viento": datos.get("wind", {}).get("speed"),
            "direccion_viento": datos.get("wind", {}).get("deg"),
        }

        return jsonify({"mensaje": "Datos obtenidos correctamente", "data": resultado})

    except requests.exceptions.HTTPError as errh:
        return jsonify({"error": f"HTTP Error: {errh}"}), 400
    except requests.exceptions.RequestException as err:
        return jsonify({"error": f"Error al conectar con OpenWeatherMap: {err}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
