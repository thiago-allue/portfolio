import time
import PySimpleGUI as sg

# ----------------  Create Form  ----------------
sg.ChangeLookAndFeel('Black')
sg.SetOptions(element_padding=(0, 0))

layout = [[sg.Text('')],
          [sg.Text('', size=(8, 2), font=('Helvetica', 20),
                   justification='center', key='text')],
          [sg.Button('Pause', key='button', button_color=('white', '#001480')),
           sg.Button('Reset', button_color=('white', '#007339'), key='Reset'),
           sg.Exit(button_color=('white', 'firebrick4'), key='Exit')]]

window = sg.Window('Running Timer', no_titlebar=True, auto_size_buttons=False,
                   keep_on_top=True, grab_anywhere=True).Layout(layout)

# ----------------  main loop  ----------------
current_time = 0
paused = False
start_time = int(round(time.time() * 100))
while (True):
    # --------- Read and update window --------
    if not paused:
        event, values = window.Read(timeout=10)
        current_time = int(round(time.time() * 100)) - start_time
    else:
        event, values = window.Read()
    if event == 'button':
        event = window.FindElement(event).GetText()
    # --------- Do Button Operations --------
    if event is None or event == 'Exit':        # ALWAYS give a way out of program
        break
    if event is 'Reset':
        start_time = int(round(time.time() * 100))
        current_time = 0
        paused_time = start_time
    elif event == 'Pause':
        paused = True
        paused_time = int(round(time.time() * 100))
        element = window.FindElement('button')
        element.Update(text='Run')
    elif event == 'Run':
        paused = False
        start_time = start_time + int(round(time.time() * 100)) - paused_time
        element = window.FindElement('button')
        element.Update(text='Pause')

    # --------- Display timer in window --------
    window.FindElement('text').Update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60,
                                                                    (current_time //
                                                                     100) % 60,


                                                                    current_time % 100))
