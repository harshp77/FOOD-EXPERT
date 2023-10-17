import PySimpleGUI as sg
from PIL import Image, ImageTk
import io
import os

sg.theme('DarkBlack')
img1=sg.Image('out.png',size=(350,200), key="-IMAGE-")
file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]

layout = [  [sg.Column([[img1]], justification='center')],
            [sg.Column([[sg.Button('This sample of daal is of Adulteration level 3')]], justification='center')],
            [sg.Column([[sg.Text('Alert: The sample of daal is not suitable for consumption', text_color='red')]], justification='center')],
            [sg.Column([[sg.Button('Exit')]], justification='center')],
            
    ]
window = sg.Window('Ouptut', layout, size= (480,320))

while True:
    event , values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
window.close()