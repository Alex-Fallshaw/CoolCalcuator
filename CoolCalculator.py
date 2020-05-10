import PySimpleGUI as sg
import re

sg.theme('DarkTeal4')	# Add a touch of colour

re_numbers = re.compile(r"^-?\d+(\.\d+)?$")
exit_button_text = 'Leave' 
calculate_button_text = 'Calculate'
errorCount = 0

def valid_int_or_dec(values):
    return re.match(re_numbers, values['paramA']) and re.match(re_numbers, values['paramB']) and re.match(re_numbers, values['paramC'])

def float_or_none(value):
    try:
        return float(value)
    except:
        return None

def valid_range_and_domain(values):
    return (values['range1']=='' or re.match(re_numbers, values['range1'])) and (values['range2']=='' or re.match(re_numbers, values['range2'])) and (values['domain1']=='' or re.match(re_numbers, values['domain1'])) and (values['domain2']=='' or re.match(re_numbers, values['domain2']))

def extract_params(values):
    return {'a': float(values['paramA']), 'b': float(values['paramB']), 'c': float(values['paramC']), 
                'd1': float_or_none(values['domain1']), 'd2': float_or_none(values['domain2']), 
                'r1': float_or_none(values['range1']), 'r2': float_or_none(values['range2'])}

def tp_in_range_and_domain(params, turnpx, turnpy):
    return (params['d1']==None or turnpx > params['d1']) and (params['d2']==None or turnpx < params['d2']) and (params['r1']==None or turnpy > params['r1']) and (params['r2']==None or turnpy < params['r2'])

def populate_defaults(window):
    window.Finalize()
    window['paramA'].update('1')
    window['paramB'].update('-2')
    window['paramC'].update('2')
    window['domain1'].update('-1')
    window['domain2'].update('')
    window['range1'].update('')
    window['range2'].update('2')

def domain_and_range_are_forwards(params):
    return (params['d1']==None or params['d2']==None or params['d1'] <= params['d2']) and (params['r1']==None or params['r2']==None or params['r1'] <= params['r2'])

# All the stuff inside your window.
layout = [  [sg.Text('Quadratic-o-matic', font='helvetica 20')],
            [sg.Text('1. Input your quadratic: y='), sg.InputText(size=(5,1), key='paramA'),
             sg.Text('x^2 +'), sg.InputText(size=(5,1), key='paramB'),
             sg.Text('x +'), sg.InputText(size=(5,1), key='paramC')],
            [sg.Text('Optional: Input your Domain: ('), sg.InputText(size=(5,1), key='domain1'), 
             sg.Text(','), sg.InputText(size=(5,1), key='domain2'), sg.Text('), and/or your Range: ('), 
             sg.InputText(size=(5,1), key='range1'), sg.Text(','), sg.InputText(size=(5,1), key='range2'), sg.Text(').')],
            [sg.Text('', size=(100,1), key='errorCorrectText1')],
            [sg.Text('Please only use integers or decimals, and type in any 0s or 1s. Feel free to leave Range and Domain blank.')],
            [sg.Text('2.'), sg.Button(calculate_button_text)],
            [sg.Text('_'*100)],
            [sg.Text('Results:', font='helvetica 15')],
            [sg.Text('Discriminant:', size=(100,1), key='sumText')],
            [sg.Text('Turning point:', size=(100,1), key='tpText')],
            [sg.Button(exit_button_text)]]


# Create the Window
window = sg.Window('Quadratic-o-matic', layout)
# Event Loop to process "events" and get the "values" of the inputs

populate_defaults(window)

while True:
    event, values = window.read()
    if event in (None, exit_button_text):	# if user closes window or clicks cancel
        break
    if valid_int_or_dec(values):
        params= extract_params(values)
        discrim=params['b']**2.0-4.0*params['a']*params['c']
        turnpx=(-params['b'])/(2.0*params['a'])
        turnpy=params['c']-(params['b']**2)/4*params['a']   
        window['sumText'].update('Discriminant:' + str(discrim))
        if errorCount > 0:
            window['errorCorrectText1'].update('Much better!')
            errorCount = 0
        else:
            window['errorCorrectText1'].update('')
        if not domain_and_range_are_forwards(params):
            window['errorCorrectText1'].update('Make sure your minimum range and domain are smaller than your maximum range and domain.')
            errorCount = 0
        if valid_range_and_domain(values):
            window['tpText'].update('Turning point: (' + str(turnpx) + ', ' + str(turnpy) + ')')
        else:
            window['errorCorrectText1'].update('Make sure your range and domain are integers, decimals or blank.') 
            errorCount = 1
        if not tp_in_range_and_domain(params, turnpx, turnpy):
            window['tpText'].update('Turning point: (' + str(turnpx) + ', ' + str(turnpy) + '), but it falls outside the range or domain.')
    else:
        window['errorCorrectText1'].update('Make sure your quadratic is made up of integers and decimals.')
        errorCount = 1


window.close()