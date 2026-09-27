import smtplib, ssl, tkinter, poplib, email
from email.header import decode_header
from tkinter import *

# Use TKInter to build a GUI for the program.

top = tkinter.Tk()
top.title("Email Client")
frame1 = Frame(top)
frame2 = Frame(top)
frame3 = Frame(top)
frame4 = Frame(top)
frame5 = Frame(top)
frame6 = Frame(top)
frame1.pack()
frame2.pack()
frame3.pack()
frame4.pack()
frame5.pack()
frame6.pack()
L1 = Label(frame1, text = "Sender")
L1.pack(side = LEFT)
E1 = Entry(frame1, bd = 5)
E1.pack(side = RIGHT)
L2 = Label(frame2, text = "Receiver")
L2.pack(side = LEFT)
E2 = Entry(frame2, bd = 5)
E2.pack(side = RIGHT)
L3 = Label(frame3, text = "Message")
L3.pack(side = LEFT)
T1 = Text(frame3, bd = 5,highlightthickness = 3, height = 10, width = 60, bg="khaki")
T1.pack(side = RIGHT)
L4 = Label(frame4, text = "Password")
L4.pack(side = LEFT)
E3 = Entry(frame4, bd = 5, show = "*")
E3.pack(side = RIGHT)
L5 = Label(frame6, text = "Mailbox")
L5.pack(side = LEFT)
LT1 = Listbox(frame6, width = 45, bg = "pale green")
LT1.pack(side = RIGHT)

# Action handler for the 'send' button.
# Sends an email to the receiver address
# with the content found in the message field

def sendEmail():
    port = 465  # For SSL
    smtp_server = "smtp.googlemail.com"
    sender_email = E1.get()  # Enter your address
    receiver_email = E2.get()  # Enter receiver address
    password = E3.get()
    message = """\Subject: Hi there  """ + T1.get("1.0", END)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

# Action handler for the 'close' button.
# Closes the TKInter window and exits the email client program.

def closeWindow():
    top.destroy()
    exit()

# Action handler for the 'retrieve' button.
# Obtains the first 10 entries from the sender's mailbox.
# Displays the titles of the emails in a listbox.

def retrieveMail():
    user = E1.get()
    mailbox = poplib.POP3_SSL('pop.googlemail.com', '995')
    mailbox.user(user)
    mailbox.pass_(E3.get())
    numOfMessages = len(mailbox.list()[1])
    for i in range(0,10):
        raw_email = b"\n".join(mailbox.retr(i+1)[1])
        parsed_email = email.message_from_bytes(raw_email)
        subject = decode_header(parsed_email['Subject'])
        LT1.insert(i, subject[0][0])
        print(subject[0][0])
    mailbox.quit()

# Add action handlers to the GUI elements.

retrieveButton = Button(frame5, text = "retrieve", command = retrieveMail)
retrieveButton.pack(side = LEFT)
sendButton = Button(frame5, text = "send", command = sendEmail)
sendButton.pack(side = LEFT)
closeButton = Button(frame5, text = "exit", command = closeWindow)
closeButton.pack(side = RIGHT)

# Start the GUI main loop.

top.mainloop()
