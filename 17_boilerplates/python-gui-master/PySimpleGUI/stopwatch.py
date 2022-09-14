import PySimpleGUI as sg

layout = [[sg.Text('Stopwatch', size=(20, 2), justification='center')],
            [sg.Text('', size=(10, 2), font=('Helvetica', 20), justification='center', key='_OUTPUT_')],
            [sg.T(' ' * 5), sg.Button('Start/Stop', focus=True), sg.Quit()]]

window = sg.Window('Running Timer').Layout(layout)

timer_running = True
i = 0
# Event Loop
while True:
    i += 1 * (timer_running is True)
    event, values = window.Read(timeout=10) # Please try and use a timeout when possible
    if event is None or event == 'Quit':  # if user closed the window using X or clicked Quit button
        break
    elif event == 'Start/Stop':
        timer_running = not timer_running
    window.FindElement('_OUTPUT_').Update('{:02d}:{:02d}.{:02d}'.format((i // 100) // 60, (i // 100) % 60, i % 100))