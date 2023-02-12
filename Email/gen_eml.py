# Prototype to create an eml file using python

import os
import uuid
from email import generator
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# where to write the output file
directory = r"C:\tmp"

body = "The text editor in OpenProject FactoryTestKeyWord  supports basic text styles, "  \
       "such as bold and italic formatting, headings, strikethrough, inline code, and "   \
       "quotes as well as inline image handling. Pasting content such as images or rich " \
       "text is also supported, while unsupported styling will be stripped by the editor."

subject = "test"
toAddress = "joe@example.com"
fromAddress = "katrin@example.org"


def create_message():
    msg = MIMEMultipart()
    msg["To"] = toAddress
    msg["From"] = fromAddress
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    return msg

def write_eml_file(msg):
    os.chdir(directory)
    filename = str(uuid.uuid4()) + ".eml"

    with open(filename, 'w') as file:
        emlGenerator = generator.Generator(file)
        emlGenerator.flatten(msg)

def main():
    msg = create_message()
    write_eml_file(msg)

if __name__ == "__main__":
    main()





