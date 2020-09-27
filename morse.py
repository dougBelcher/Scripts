from time import sleep

speed = 0.1

def signal(duration, symbol):
    sleep(duration)
    print(symbol, end='', flush=True)

dot = lambda: signal(speed, '·\a')
dash = lambda: signal(3*speed, '−\a')
symbol_space = lambda: signal(speed, '')
letter_space = lambda: signal(3*speed, '')
word_space = lambda: signal(7*speed, ' ')