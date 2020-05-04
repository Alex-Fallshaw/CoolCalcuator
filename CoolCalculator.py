import PySimpleGUI as sg
import re

sg.theme('DarkAmber')	# Add a touch of colour

re_numbers = re.compile(r"^\d+(\.\d+)?$")

# Strings
exit_button_text = 'Leave'
calculate_button_text = 'Calculate'

# All the stuff inside your window.
layout = [  [sg.Text('Input first number:'), sg.InputText()],
            [sg.Text('Input second number:'), sg.InputText()],
            [sg.Text('Input third number:'), sg.InputText()],
            [sg.Text('This is where your sum will show.', size=(100,1), key="sum")],
            [sg.Button(calculate_button_text), sg.Button(exit_button_text)] ]

# Create the Window
window = sg.Window('Number summer', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, exit_button_text):	# if user closes window or clicks cancel
        break
    if re.match(re_numbers, values[0]) and re.match(re_numbers, values[1]) and re.match(re_numbers, values[2]):
        sum=float(values[0])+float(values[1])+float(values[2])
        window["sum"].update('The sum of your numbers is ' + str(round(sum, 5)))
    else:
        window["sum"].update('Give me real numbers, dickhead.')

window.close()