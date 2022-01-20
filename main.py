from random import choice
import os
import resultado
    
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
        
        resultado.result(election, option)
        
    
    except ValueError:
        error = """
                 * ** ** ** ** ** ** ** ** **  * 
                -----------SOLO NÚMEROS----------
                 * ** ** ** ** ** ** ** ** **  * """
        options(error)   


if __name__ == '__main__':
    options("")
    
