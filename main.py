# Pen-Testing automation Tools
logo = """\033[33m
  ('-. .-.                            ('-.           ('-.                 .-') _                
( OO )  /                          _(  OO)         ( OO ).-.            (  OO) )               
,--. ,--. .-'),-----.   ,----.    (,------.        / . --. / ,--. ,--.  /     '._  .-'),-----. 
|  | |  |( OO'  .-.  ' '  .-./-')  |  .---'        | \-.  \  |  | |  |  |'--...__)( OO'  .-.  '
|   .|  |/   |  | |  | |  |_( O- ) |  |          .-'-'  |  | |  | | .-')'--.  .--'/   |  | |  |
|       |\_) |  |\|  | |  | .--, \(|  '--.        \| |_.'  | |  |_|( OO )  |  |   \_) |  |\|  |
|  .-.  |  \ |  | |  |(|  | '. (_/ |  .--'         |  .-.  | |  | | `-' /  |  |     \ |  | |  |
|  | |  |   `'  '-'  ' |  '--'  |  |  `---.        |  | |  |('  '-'(_.-'   |  |      `'  '-'  '
`--' `--'     `-----'   `------'   `------'        `--' `--'  `-----'      `--'        `-----' 
                                         ▀                                                                            ▀                             
                                    \033[34m[✔] https://github.com/TheCyberDiver   [✔]
                                    \033[34m[✔]            Version 1.1.0               [✔]
                                    \033[91m[X] Please Don't Use For illegal Activity  [X]
\033[97m """

import subprocess

print (logo)

def menu():

    print("[1] Run Auto Tool")
    print("[2] Print the Load")
    print("[3] Print the Load")

    input_chosen = input("Please choose an option: ")
    
    # The first option will run a subprocess of the shell script with the input you provide as the IP.
    # The shell script for auto enumeration is still under progress and best used for CTF at this time.

    if int(input_chosen) == 1:
        
        input_ip_chosen = input("What is the IP of the target machine: ")

        rc = subprocess.call(["./Enumerator.sh", input_ip_chosen])

    elif int(input_chosen) == 2:
      
        print('Currently Under Construction')

    elif int(input_chosen) == 3:
      
        print('Currently Under Construction')


    else:
        print('Sorry, value must be from the given list!')


if __name__ == '__main__':
    menu()
