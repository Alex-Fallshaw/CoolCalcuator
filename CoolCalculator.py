import PySimpleGUI as sg
import re

sg.theme('DarkTeal4')	# Add a touch of colour

re_numbers = re.compile(r"^\d+(\.\d+)?$")

# Strings
exit_button_text = 'Leave' 
calculate_button_text = 'Calculate'

# All the stuff inside your window.
layout = [  [sg.Text('Quadratic-o-matic')],
            [sg.Text('Input your quadratic:'), sg.InputText(size=(5,1), key='paramA'),
             sg.Text('x^2 +'), sg.InputText(size=(5,1), key='paramB'),
             sg.Text('x +'), sg.InputText(size=(5,1), key='paramC')],
            [sg.Text('This is where the discriminant will show.', size=(100,1), key="sumText")],
            [sg.Button(calculate_button_text), sg.Button(exit_button_text)] ]

# Create the Window
window = sg.Window('Number summer', layout)
# Event Loop to process "events" and get the "values" of the inputs

while True:
    event, values = window.read()
    if event in (None, exit_button_text):	# if user closes window or clicks cancel
        break
    if re.match(re_numbers, values['paramA']) and re.match(re_numbers, values['paramB']) and re.match(re_numbers, values['paramC']):
        params={'a': float(values['paramA']), 'b': float(values['paramB']), 'c': float(values['paramC'])}
        discrim=params['a']**2.0 - 4.0*params['b']*params['c']
        window["sumText"].update('The discriminant is ' + str(discrim))
    else:
        window["sumText"].update('Give me real numbers, stupid.')

window.close()