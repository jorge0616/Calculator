import Interface as Int
import Accessibility as Acc

# Helper variables
Hist = ""
Disp = ""

# Helper function
def update_screen():
    Int.Window['History'].update(Hist)
    if Disp != "":
        Int.Window['Display'].update(Disp)
    else:
        Int.Window['Display'].update("0")


# Main
if __name__ == '__main__':
    while True:
        Event, Value = Int.Window.read()
        print(Event)
        if Event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            Disp += Event
        elif Event in ['.', ','] and len(Disp) > 0:
            Disp += '.'
        elif Event in ['×', '*', '÷', '/', '+', '-', '(', ')']:
            if Event in ['×', '*'] and len(Disp) > 0:
                Disp += '*'
            elif Event in ['÷', '/'] and len(Disp) > 0:
                Disp += '/'
            elif Event == '+' and len(Disp) > 0:
                Disp += Event
            elif Event == '-':
                Disp += Event
            elif Event in ['(', ')']:
                Disp += Event
        elif Event in ['√x', 'x²', '±'] and len(Disp) > 0:
            if Event == '√x':
                Disp += '**(1/2)'
            elif Event == 'x²':
                Disp += '**(2)'
            elif Event == '±':
                Disp += '*(-1)'
        elif Event in ['ᴄᴇ', 'ᴄ', '«']:
            if Event == 'ᴄᴇ':
                Disp = ""
            elif Event == 'ᴄ':
                Hist, Disp = "", ""
            elif Event == '«' and len(Disp) > 0:
                Disp = Disp[:-1]
        elif Event == '=' and len(Disp) > 0:
            try:
                Hist, Disp = Disp+" =", str(round(eval(Disp), 4))
            except Exception as Error:
                print(Error)
                Hist, Disp = "", ""
        elif Event == '🔊':
            Acc.reader(Hist+Disp)
        elif Event == Int.Psg.WIN_CLOSED:
            break
        update_screen()
