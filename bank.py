import PySimpleGUI
sg = PySimpleGUI


def open_file():
    with open('bank.txt', 'r+', encoding='utf-8') as f:
       l = f.readlines()

       
    return l[0]
       
def bankapp():
    layout = [
        [sg.Text('Bank app')],
        [sg.Text('Vad vill du göra?')],
        [sg.Input('')],
        [sg.Button('1. Vill du sätta in pengar?')],
        [sg.Button('2. Vill du ta ut pengar?')],
        [sg.Button('3. Vill du se ditt saldo?')],
        [sg.Button('4. Avsluta app')]
        
    ]

    

    window = sg.Window('Window Title', layout)
    event, values = window.read()
    window.close()

def val():
        if sg.Button == 1:
            sätta_in_pengar()

def sätta_in_pengar():
    layout = [
        [sg.Text('Hur mycket pengar vill du sätta in?')]
        [sg.Input('')],
    ]

def main():
   print('')
  

if __name__ == '__main__':
    main()

bankapp()