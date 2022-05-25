import PySimpleGUI as sg

form = sg.FlexForm('Ya Mum')

layout = [
    [sg.Text('Blahhhh')],
    [sg.Input()],
    [sg.Text('Yep'), sg.InputText('lopi')],
    [sg.Submit(), sg.Cancel()],
    [sg.Button('OK')]
]

window = sg.Window('Window Title', layout)

event, values = window.read()

print('Hello', values[0], 'what loserrrrrr')

window.close()