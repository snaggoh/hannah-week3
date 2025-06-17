# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################

def teleport():
    agent.teleport_to_player()
player.on_chat("c", teleport)

def turnleft():
    agent.turn(LEFT)
player.on_chat("tl", turnleft)

def turnright():
    agent.turn(RIGHT)
player.on_chat("tr", turnright)

def movef(steps):
    agent.move(FORWARD, steps)
player.on_chat("f", movef)

def moveb(steps):
    agent.move(BACK, steps)
player.on_chat("b", moveb)

def moveu(steps):
    agent.move(UP, steps)
player.on_chat("u", moveu)

def moved(steps):
    agent.move(DOWN, steps)
player.on_chat("d", moved)


def obby1():
    agent.move(FORWARD, 4)
    agent.turn(LEFT)
    agent.move(FORWARD, 4)
    agent.turn(RIGHT)
    agent.move(FORWARD, 3)

player.on_chat("obby1", obby1)

def obby2():
    agent.move(UP, 1)
    agent.move(FORWARD, 1) 
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 3)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
player.on_chat("obby2", obby2)











################## On Chat Commands Section #####################
