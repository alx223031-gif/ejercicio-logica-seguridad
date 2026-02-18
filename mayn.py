import time
import random
import os

# --- Clase de Lógica de la IA ---
class VisualBrain:
    def __init__(self):
        # Memoria simple: confianza inicial en cada acción
        self.memory = {
            "explotacion_controlada": 50,
            "fuerza_bruta": 50,
            "escaneo_silencioso": 50
        }

    def get_best_action(self, epsilon=0.1):
        # Exploración vs Explotación (epsilon-greedy)
        if random.random() < epsilon:
            return random.choice(list(self.memory.keys()))
        # Elige la acción con mayor puntaje en memoria
        return max(self.memory, key=self.memory.get)

    def learn(self, action, reward):
        # Ajusta la confianza: si funciona sube, si falla baja
        self.memory[action] += reward
        # Evitamos que los valores sean negativos extremos o demasiado altos
        self.memory[action] = max(0, min(self.memory[action], 200))

    def draw_dashboard(self, action, status):
        # Limpia la pantalla (multiplataforma)
        os.system('clear' if os.name == 'posix' else 'cls')
        print("="*45)
        print(f" SIMULADOR DE LÓGICA EN CIBERSEGURIDAD ")
        print("="*45)
        print(f" Acción actual:  {action.replace('_', ' ').upper()}")
        print(f" Estado:         {status}")
        print("-"*45)
        print(" Confianza del Sistema (Memoria Q):")
        for key, val in self.memory.items():
            barras = "█" * (val // 10)
            print(f" {key.ljust(22)}: {barras} ({val} pts)")
        print("="*45)

# --- Funciones de Simulación ---

def simulate_penetration_step(action):
    """Simula resultados basados en la probabilidad real de detección."""
    prob = random.random()
    
    if action == "explotacion_controlada":
        return "pwned" if prob > 0.4 else "detectado"
    
    if action == "fuerza_bruta":
        # CORREGIDO: Lógica invertida - ahora 80% de éxito
        return "pwned" if prob > 0.2 else "bloqueado"
    
    if action == "escaneo_silencioso":
        return "limpio" # El escaneo casi siempre pasa desapercibido
    
    return "error"

def calculate_reward(outcome):
    """Asigna puntos según el éxito o el riesgo de la acción."""
    rewards = {
        "pwned": 100,      # Éxito total
        "limpio": 10,      # Cauteloso pero efectivo
        "detectado": -20,  # Fallo leve
        "bloqueado": -50   # Error grave (detección del IPS/Firewall)
    }
    return rewards.get(outcome, 0)

# --- Bucle Principal ---

def main():
    brain = VisualBrain()
    
    print("Iniciando entorno de pruebas...")
    time.sleep(1)
    
    try:
        while True:
            # 1. La IA decide qué intentar
            current_action = brain.get_best_action()
            
            # 2. Mostramos qué está pasando
            brain.draw_dashboard(current_action, "EJECUTANDO...")
            time.sleep(1.5)
            
            # 3. Se ejecuta la simulación
            result = simulate_penetration_step(current_action)
            
            # 4. Cálculo de puntos y aprendizaje
            reward = calculate_reward(result)
            brain.learn(current_action, reward)
            
            # 5. Actualización final del turno
            brain.draw_dashboard(current_action, f"RESULTADO: {result.upper()} ({reward} pts)")
            
            print("\n[Presiona Ctrl+C para detener la simulación]")
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n\n[!] Simulación finalizada por el usuario. Memoria guardada en sesión.")

if __name__ == "__main__":
    main()