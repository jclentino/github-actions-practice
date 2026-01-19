import os

def main():
    nombre = os.getenv("USERNAME", "Usuario")
    lenguaje = os.getenv("LANGUAGE", "Python")

    print(f"¡Hola, {nombre}! 👋")
    print(f"Tu lenguaje favorito es {lenguaje} 🚀")
    print("Este workflow fue ejecutado manualmente usando workflow_dispatch ✅")

if __name__ == "__main__":
    main()
