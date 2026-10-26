import json
import os
from datetime import datetime

ARCHIVO = "datos.json"
TIPOS_VALIDOS = ("auto", "moto")


def cargar(archivo=ARCHIVO):
    """Devuelve la lista de vehículos dentro del estacionamiento."""
    if not os.path.exists(archivo):
        return []
    with open(archivo, encoding="utf-8") as f:
        return json.load(f)


def guardar(vehiculos, archivo=ARCHIVO):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(vehiculos, f, indent=2, ensure_ascii=False)


def registrar_ingreso(placa, tipo, archivo=ARCHIVO, hora=None):
    """Registra el ingreso de un vehículo. Lanza ValueError si hay datos inválidos."""
    placa = placa.strip().upper()
    tipo = tipo.strip().lower()

    if not placa:
        raise ValueError("La placa no puede estar vacía.")
    if tipo not in TIPOS_VALIDOS:
        raise ValueError("El tipo debe ser 'auto' o 'moto'.")

    vehiculos = cargar(archivo)
    if any(v["placa"] == placa for v in vehiculos):
        raise ValueError(f"El vehículo {placa} ya está dentro del estacionamiento.")

    registro = {
        "placa": placa,
        "tipo": tipo,
        "hora_ingreso": (hora or datetime.now()).isoformat(timespec="seconds"),
    }
    vehiculos.append(registro)
    guardar(vehiculos, archivo)
    return registro
