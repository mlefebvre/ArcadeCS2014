from pump import Pump
from game import Game

PUMP_PORT = "COM3"

if __name__ == "__main__":
    pump = Pump(PUMP_PORT)
    with pump:
        try:
            pump.start()
            game = Game(pump)
            game.start()
        except Exception as e:
            print e