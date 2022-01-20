from random import choice
import os
import logica
import main

def result(election, option):
    result = logica.game(election, option)
    if result:
        os.system('cls')
        print(f"""      
                        {result} 
        """)
        again = input("""
                ¿VOLVER A JUGAR?
                
                Sí: Escribe 'sí':  
                No: Presiona 'ENTER': """)
        again = again.lower().replace('í', 'i')

        if again == 'si':
            main.options("")
        else:
            return