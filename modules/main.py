import message

print(message.hello)


message.print_message("Hello work")

from message import print_message

print_message("Hello work")


import message as mes

mes.print_message("Hello")