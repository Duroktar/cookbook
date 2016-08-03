import pytronlinks as pytron
from cleverbot import Cleverbot as Bot


def main():

    while True:
        try:
            query = AI.listen('Cleverbot')
        except Exception as e:
            AI.talk(str(e) + ". Cuz errors Happen ")
            break
        if query == 'quit':
            break
        try:
            result = str(BOT.ask(query))
            AI.talk(result)
        except Exception as e:
            AI.talk(str(e))

    AI.talk('Shutting down clever bot session. Goodbye.')

if __name__ == '__main__':
    AI = pytron.Client()
    BOT = Bot()
    AI.talk("Clever bot chat started")
    main()
