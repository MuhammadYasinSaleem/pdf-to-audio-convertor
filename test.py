import PyPDF2
import pyttsx3

user_input = input("Enter path of the PDF file: ")
pdf_path = user_input + ".pdf"

try:
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        page_index = int(input("Enter page number you want to start from: "))
        if 0 <= page_index < len(pdf_reader.pages):
            for current_page in range(page_index, len(pdf_reader.pages)):
                from_page = pdf_reader.pages[current_page]

                text = from_page.extract_text()
                speak = pyttsx3.init()
                speak.say(text)
                speak.runAndWait()

                user_input = input("Press 'Enter' to continue reading or 'Q' to quit: ")

                if user_input.lower() == 'q':
                    print("Reading stopped.")
                    speak.stop()
                    break  # Exit the loop if the user enters 'Q'
        else:
            print("Invalid starting page index.")
except Exception as e:
    print(f"An error occurred: {e}")
