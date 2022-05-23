import time
import src.chat as chat

class test:
    def go():
        start = time.asctime()
        chat.startBot()
        end = time.asctime()

        print(start)
        print(end)