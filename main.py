# Import the necessary libraries
import pyttsx3
import PyPDF2

# Open file

file = open('pdf_files/Coffee_Machine_Program_Requirements.pdf', 'rb')
docu = PyPDF2.PdfReader(file)

# Get the page to bread

page = docu.pages[0]
text = page.extract_text()

# Read out page
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()


