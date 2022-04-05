import PySimpleGUI as Psg

# Buttons
Bn = {'size': (4, 1), 'font': ('arial', 20), 'button_color': ('white', '#060606'), 'border_width': 0}
Bf = {'size': (4, 1), 'font': ('arial', 20), 'button_color': ('white', '#131313'), 'border_width': 0}
Be = {'size': (4, 1), 'font': ('arial', 20), 'button_color': ('white', '#134369'), 'border_width': 0}
Ba = {'size': (2, 1), 'font': ('arial', 12), 'button_color': ('white', '#1F1F1F'), 'border_width': 0}

# Layout
Layout = [[Psg.Button('🔊', **Ba), Psg.Text('', size=(24, 1), font=('arial', 15), justification='right', background_color='#1F1F1F', text_color='gray', key='History')],
          [Psg.Text('0', size=(14, 1), font=('arial', 28), justification='right', background_color='#1F1F1F', text_color='white', key='Display')],
          [Psg.Button('√x', **Bf), Psg.Button('ᴄᴇ', **Bf), Psg.Button('ᴄ', **Bf), Psg.Button('«', **Bf)],
          [Psg.Button('x²', **Bf), Psg.Button('(', **Bf), Psg.Button(')', **Bf), Psg.Button('÷', **Bf)],
          [Psg.Button('7', **Bn), Psg.Button('8', **Bn), Psg.Button('9', **Bn), Psg.Button('×', **Bf)],
          [Psg.Button('4', **Bn), Psg.Button('5', **Bn), Psg.Button('6', **Bn), Psg.Button('-', **Bf)],
          [Psg.Button('1', **Bn), Psg.Button('2', **Bn), Psg.Button('3', **Bn), Psg.Button('+', **Bf)],
          [Psg.Button('±', **Bn), Psg.Button('0', **Bn), Psg.Button('.', **Bn), Psg.Button('=', **Be)]]

# Window
Window = Psg.Window("Calculator", layout=Layout, background_color='#1F1F1F', return_keyboard_events=True)
