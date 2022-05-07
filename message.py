import pywhatkit

# Send a WhatsApp Message to a Contact at 1:30 PM
pywhatkit.sendwhatmsg("+22896382445", "Hi", 19, 17)

# # Same as above but Closes the Tab in 2 Seconds after Sending the Message
# pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30, 15, True, 2)

# # Send an Image to a Group with the Caption as Hello
# pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")

# # Send an Image to a Contact with the no Caption
# pywhatkit.sendwhats_image("+910123456789", "Images/Hello.png")

# # Send a WhatsApp Message to a Group at 12:00 AM
pywhatkit.sendwhatmsg_to_group("EspaceEtudiants DA2", "Hey All!", 19, 27)

# # Play a Video on YouTube
# pywhatkit.playonyt("PyWhatKit")

# By Fred-codeur
