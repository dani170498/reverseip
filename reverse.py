import requests
import colorama
from colorama import init,Fore
init(autoreset=True)
def reverse_ip_lookup(ip_address, access_token):
    url = f"https://ipinfo.io/{ip_address}/json?token={access_token}"
    response = requests.get(url)
    data = response.json()

    if 'error' not in data:
        return data
    else:
        return f"Error: {data['error']['message']}"

# Solicita al usuario que ingrese la dirección IP y el token de acceso
ip_address = input(Fore.GREEN+"Introduce la dirección IP que deseas investigar: ")
access_token = 'fd2f2527c1437b'

# Llama a la función con los datos ingresados
info = reverse_ip_lookup(ip_address, access_token)

if isinstance(info, dict):
    # Imprime cada clave-valor en una nueva línea en formato "clave: valor"
    for key, value in info.items():
        print(Fore.CYAN+f"{key}: "+Fore.WHITE+f"{value}")
else:
    print(info)

