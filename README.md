# Ejercicio: Lógica de Seguridad y Aprendizaje por Refuerzo

¡Hola! Este es mi primer proyecto "en serio" mientras exploro el mundo de la **Ciberseguridad** y la programación con Python desde mi entorno en **Kubuntu**.

## 🧠 ¿De qué trata esto?
Es un simulador básico de toma de decisiones. He creado una "IA" muy sencilla que utiliza un sistema de recompensas para aprender qué acciones son efectivas y cuáles son arriesgadas en un entorno de red simulado.

### Acciones que simula:
* **Escaneo silencioso:** Poco riesgo, recompensa baja.
* **Explotación controlada:** Riesgo medio, recompensa alta si funciona.
* **Fuerza bruta:** Riesgo alto, suele ser detectado o bloqueado.

## 🛠️ Tecnologías
* **Lenguaje:** Python 3
* **OS:** Kubuntu (KDE Plasma)
* **Concepto clave:** Q-Learning (Aprendizaje por refuerzo básico)

## 🚀 Cómo probarlo
Si tienes Python instalado, solo clona el repo y corre el archivo:
```bash
python3 main.py
