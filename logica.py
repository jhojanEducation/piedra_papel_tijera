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