__author__ = 'tomasskopal'

from IO import IO
from Bot import Bot

if __name__ == '__main__':
    io = IO()
    bot = Bot(io)
    bot.run()