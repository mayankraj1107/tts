from tkinter import Tk
from tkinter.filedialog import askopenfilename
import PyPDF2
import pyttsx3

engine = pyttsx3.init(driverName= 'sapi5')
engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")   



Tk().withdraw()
file_location = askopenfilename()


with open(file_location, "rb") as f:
    pdf = PyPDF2.PdfFileReader(f)

    i = 0
    text = " "
    while i < pdf.getNumPages():
        page = pdf.getPage(i)
        text += page.extractText()
        i += 1   
    
engine.save_to_file(text, "audio.mp3")  
engine.runAndWait()
engine.stop()
print("Task Completed ")



