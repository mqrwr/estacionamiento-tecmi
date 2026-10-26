# Estacionamiento TecMi

Sistema de estacionamiento (proyecto de práctica, Ciclo de Vida del Software).

## Módulos
1. Registro de ingreso de vehículo (placa, hora, tipo)
2. Cálculo de tarifa por hora y cobro
3. Disponibilidad de lugares en tiempo real

## Configuración
- Capacidad: 15 autos y 5 motos
- Tarifa: $20/hora auto, $10/hora moto (por hora o fracción)

## Cómo ejecutar
    python main.py

## Cómo probar
    python -m unittest discover -s tests -t .

## Flujo de trabajo
Una rama `feature/...` por módulo, con Pull Request revisado hacia `main`.
