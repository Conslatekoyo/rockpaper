from mimetypes import init
from platform import win32_edition
import random

def play():
    user=input("What's your choice 'r' for rock, 'p' for paper and 's' for scissors")
    computer = random.choice(['r','p' and 's'])

    if user == computer:
        return'tie'
# 'r'>s ,s>p and p>r
    if is_win(user,computer):
         return "You won"


    return "You lost"

def is_win(player, opponent):
    #return true if player wins
    if (player=='r' and opponent=='s') or (player=='s' and opponent== 'p')or (player =='p' and opponent=='r'):
        return True