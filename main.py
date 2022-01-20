from random import choice
import os

def game(election, option):
    if election == option:
        return f"""
        ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
          {election}           {option}

                 ╭╭━╭━╮━┳━╮
                 ┣▅╋▅┫┈┈┈┃
             ╭━━━┻┻━╯━╯┈┃┈┃
            ◢▉◣┈┈┈┈┈┈┈┈┈╰┳╯
            ▉▉▉┈┈┈┈┈┈┈┈┈┈┃
            ◥▉◤┈┈┈┈┈┈┈┈┈┈┃
             ╰━━━━┳━╮┈┈┈┈┃
                  ┣━━━━━━┫


                EMPATE (≖_≖)
        ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼"""
    elif election == 'PIEDRA' and option == 'PAPEL':
        return f"""
        ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
          {election}           {option}

           █ █ █           ████
          █     █    VS    ████          
           █ █ █           ████

                 __________
                 GANA {option}
                 ----------

              PERDISTE (｡>﹏<｡)
        ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼"""
    elif election == 'PIEDRA' and option == 'TIJERA':
        return f"""
        ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
           {election}           {option}

                          ☼☼       ♦♦      
                         ☼  ☼     ♦♦       
            █ █ █         ☼☼  ♦♦//         
           █     █   VS   ☼☼  ♦♦\\\\         
            █ █ █        ☼  ☼     ♦♦       
                          ☼☼        ♦♦

                 ___________
                 GANA {election}   
                 -----------

               GANASTE   ≧^◡^≦
        ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼"""
    elif election == 'PAPEL' and option == 'PIEDRA':
        return f"""
        ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
          {election}        {option}

          ████          █ █ █
          ████    VS   █     █          
          ████          █ █ █

              __________
              GANA {election}
              ----------

            GANASTE  ≧^◡^≦
        ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼""" 
    elif election == 'PAPEL' and option == 'TIJERA':
        return f"""
        ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
            {election}                  {option}

                                 ☼☼       ♦♦      
            ████                ☼  ☼     ♦♦       
            ████                 ☼☼  ♦♦//         
            ████         VS      ☼☼  ♦♦\\\\         
            ████                ☼  ☼     ♦♦       
                                 ☼☼        ♦♦
                    
                     ___________
                     GANA {option}
                     -----------

                  PERDISTE (｡>﹏<｡)
        ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼"""
    elif election == 'TIJERA' and option == 'PIEDRA':
        return f"""
        ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
           {election}              {option}

            ☼☼       ♦♦           █
           ☼  ☼     ♦♦          █   █
            ☼☼  ♦♦//     VS   █       █
            ☼☼  ♦♦\\\\            █   █ 
           ☼  ☼     ♦♦            █
            ☼☼        ♦♦

                      ___________
                      GANA {option}
                      -----------

                    PERDISTE (｡>﹏<｡)
        ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼"""
    elif election == 'TIJERA' and option == 'PAPEL':
        return f"""
        ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
           {election}              {option}

            ☼☼       ♦♦      
           ☼  ☼     ♦♦         ████
            ☼☼  ♦♦//     VS    ████
            ☼☼  ♦♦\\\\           ████ 
           ☼  ☼     ♦♦         ████
            ☼☼        ♦♦

                ___________
                GANA {election}
                -----------

                GANASTE (｡>﹏<｡)
        ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼"""

def result(election, option):
    result = game(election, option)
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
            options("")
        else:
            return
        
        

def options(error):
    os.system('cls')
    
    print(error)
    
    try:
        menu = """
                //// PIEDRA - PAPEL - TIJERA \\\\\\\\
                    ╩───────────────────────╩

                         ELIJE UN NÚMERO: 
              ----------------------------------------
                                                     /
                                      █ █ █          /
              1 = PIEDRA             █     █         /
                                      █ █ █          /  
                                                     /
              ----------------------------------------
                                                     /
                                       ████          /
              2 = PAPEL                ████          /
                                       ████          /
                                                     /
              ----------------------------------------
                                    ☼☼       ♦♦      / 
                                   ☼  ☼     ♦♦       /
                                    ☼☼  ♦♦//         /
              3 = TIJERA            ☼☼  ♦♦\\\\         /
                                   ☼  ☼     ♦♦       /
                                    ☼☼       ♦♦      /
              ----------------------------------------
                            NÚMERO: """

        electio = int(input(menu))
        if electio <1 or electio >3:
            while electio <1 or electio >3:
                os.system('cls')
                print("""
                =================================            
                    ELIJE UN NÚMERO DEL 1 AL 3
                =================================""")
                electio = int(input(menu))

                election = ""
        if electio == 1:
            election = 'PIEDRA'
        elif electio == 2:
            election = 'PAPEL'
        elif electio == 3:
            election = 'TIJERA'

        ia = ['PIEDRA', 'PAPEL', 'TIJERA']
        option = choice(ia)
        
        result(election, option)
        
    
    except ValueError:
        error = """
                 * ** ** ** ** ** ** ** ** **  * 
                -----------SOLO NÚMEROS----------
                 * ** ** ** ** ** ** ** ** **  * """
        options(error)   


if __name__ == '__main__':
    options("")
    
