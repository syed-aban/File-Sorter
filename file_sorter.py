# Global variables/imports
import os
import shutil
code = ['.py' ,'.c' ,'.cpp' ,'.cs' ,'.java' ,'.sql' ,'.js' ,'.r' ,'.html' ,'.css' ,'.ts' ,'.go' ,'.php' ,'.sh' ,'.rb' ,'.scala' ,'.sc' ,'.mat' ,'.sas' ,'.asm' ,'.kt' ,'.rs' ,'.pl' ,'.m' ,'.dart' ,'.swift' ,'.v' ,'.verilog' ,'.vlg' ,'.vh' ,'.ino' ,'.d' ,'.jl' ,'.cu' ,'.vhdl' ,'.vb' ,'.groovy' ,'.gvy' ,'.gy' ,'.gsh' ,'.lua' ,'.ada' ,'.scm' ,'.abap' ,'.hs' ,'.hls' ,'.cbl' ,'.cob' ,'.ex' ,'.exs' ,'.fsx' ,'.fsi' ,'.fs' ,'.lsp' ,'.pas' ,'.f90' ,'.for' ,'.f' ,'.tcl' ,'.clj' ,'.cljs' ,'.pl' ,'.ml' ,'.llg' ,'.erl' ,'.hrl' ,'.fs' ,'.fth' ,'.4th' ,'.f' ,'.forth' ,'.elm' ,'.raku' ,'.rakumod' ,'.rakudoc' ,'.t' ,'.rakutest' ,'.wasm' ,'.coffe' ,'.litcoffee' ,'.e']
text = ['.txt']
PDF = ['.pdf']
image = ['.gif' ,'.png' ,'.jpeg' ,'.jpg' ,'.psd' ,'.xcf' ,'.ai' ,'.cdr' ,'.tif' ,'.tiff' ,'.bmp' ,'.eps' ,'.raw' ,'.cr2' ,'.nef' ,'.orf' ,'.sr2']
video = ['mp4' ,'.mov' ,'.avi' ,'.flv' ,'.avchd' ,'.mkv' ,'.webm' ,'.wmv' ,'.wmv']
audio = ['.mp3' ,'.wav' ,'.aiff' ,'.pcm' ,'.aac' ,'.wma' ,'.flac' ,'.alac']
office = ['.doc' ,'.docx' ,'.pptx' ,'.xlsx' ,'.one' ,'.gslides' ,'.gsheet']


# Create a list of all the files
cwd = os.getcwd()
files = []
for file in os.listdir(cwd):
    files.append(file)


# Check if the necessary folders are present
def chk_folders(files):
    if 'Code' not in files:
        os.mkdir(cwd+'/Code')
    
    if 'Text' not in files:
        os.mkdir(cwd+'/Text')

    if 'PDF' not in files:
        os.mkdir(cwd+'/PDF')

    if 'Image' not in files:
        os.mkdir(cwd+'/Image')
    
    if 'Video' not in files:
        os.mkdir(cwd+'/Video')

    if 'Audio' not in files:
        os.mkdir(cwd+'/Audio')

    if 'G Suite-MS Office' not in files:
        os.mkdir(cwd+'/G Suit-MS Office')


# Check file type for each file + Send file to corresponding folders.
def chk_FileType(files):
    for file in files:
        
        for x in code:
            if file.lower().endswith(x):
                directory = f'{cwd}/{file}'
                destination = f'{cwd}/Code'
                shutil.move(directory,destination)
            else: 
                pass

        for x in text:
            if file.lower().endswith(x):
                directory = f'{cwd}/{file}'
                destination = f'{cwd}/Text'
                shutil.move(directory,destination)
            else:
                pass

        for x in PDF:
            if file.lower().endswith(x):
                directory = f'{cwd}/{file}'
                destination = f'{cwd}/PDF'
                shutil.move(directory,destination)
            else:
                pass

        for x in image:
            if file.lower().endswith(x):
                directory = f'{cwd}/{file}'
                destination = f'{cwd}/Image'
                shutil.move(directory,destination)
            else:
                pass

        for x in video:
            if file.lower().endswith(x):
                directory = f'{cwd}/{file}'
                destination = f'{cwd}/Video'
                shutil.move(directory,destination)
            else:
                pass

        for x in audio:
            if file.lower().endswith(x):
                directory = f'{cwd}/{file}'
                destination = f'{cwd}/Audio'
                shutil.move(directory,destination)
            else:
                pass

        for x in office:
            if file.lower().endswith(x):
                directory = f'{cwd}/{file}'
                destination = f'{cwd}/G Suit-MS Office'
                shutil.move(directory,destination)
            else:
                pass


        if file.lower().endswith('.exe'):
            pass


# Logic
while __name__ == '__main__':
    chk_folders(files)
    chk_FileType(files)
    break