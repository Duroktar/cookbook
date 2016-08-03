import pytronlinks as pytron  # Import Pytron
import time


def main():

    while True:
        try:
            query = AI.listen('Pytron')
            if query == 'quit':
                break
            elif query == "Play music":
                # This part gets the confirmation.
                var_name = "Answer"  # The variable where
                if AI.GetConfirmation(var_name,
                                      conf_speech="Do you want to play music?",
                                      speech_on_yes="Right away",
                                      speech_on_no="Cancelled"):
                    # If confirmation returns true from a yes response, this gets called. 
                    AI.emulate_speech('play music')

        except Exception as e:
            AI.talk(str(e))
            break


    AI.talk('Goodbye.')

if __name__ == '__main__':
    AI = pytron.Client()   # Initialize Links
    main()
