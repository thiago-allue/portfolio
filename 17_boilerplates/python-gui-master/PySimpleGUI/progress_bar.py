import PySimpleGUI as sg

for i in range(1,10000):      
    sg.OneLineProgressMeter('My Meter', i+1, 10000, 'key', 'Optional message')