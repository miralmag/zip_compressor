import PySimpleGUI as sg
from zip_creator import make_archive

label_files = sg.Text('Select files to compress:')
input_files = sg.InputText()
button_files = sg.FilesBrowse('Choose', key='files')
label_folder = sg.Text('Select destination folder:')
input_folder = sg.InputText()
button_folder = sg.FolderBrowse('Choose', key='folder')
button_compress = sg.Button('Compress')
output_label = sg.Text(key='output', text_color='red')

window = sg.Window("File zipper", layout=[[label_files, input_files, button_files],
                                          [label_folder, input_folder, button_folder],
                                          [button_compress, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values['files'].split(';')
    folder = values['folder']
    make_archive(filepaths, folder)
    window['output'].update(value='Compression completed!')
window.close()