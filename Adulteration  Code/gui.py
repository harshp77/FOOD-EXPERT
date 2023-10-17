import PySimpleGUI as sg
from PIL import Image, ImageTk
import io
import os

sg.theme('DarkBlack')
img1=sg.Image('image2.png',size=(350,200), key="-IMAGE-")
file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]

layout = [  [sg.Column([[img1]], justification='center')],
            [sg.Column([[sg.Button('Load image', size=(20,2)),sg.Button('Capture image', size= (20,2))]], justification='center')],
           
            [sg.Column([[sg.Button('Exit', size=(20,2))]], justification='center')],
            
    ]
window = sg.Window('Home', layout, size= (480,320))

while True:
    event , values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
window.close()