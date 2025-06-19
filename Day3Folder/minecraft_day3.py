# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER

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



#### Day 2


def Choptree(steps):
    for count in range(steps):
        agent.destroy(FORWARD)
        agent.move(UP, 1)

    agent.move(DOWN, steps)
    agent.collect_all()
player.on_chat("Chop", Choptree)


def on_chat():
    for count in range(23):
        agent.move(FORWARD, 1)
        agent.destroy(FORWARD)
player.on_chat("stone", on_chat)

def on_chat2():
    for count in range(11):
        agent.move(FORWARD, 1)
        agent.destroy(BACK)
        agent.destroy(FORWARD)
        agent.destroy(DOWN)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
player.on_chat("break", on_chat2)

def on_chat4():
    pass
player.on_chat("jump", on_chat4)

def on_chat3():
    for count in range(9):
        agent.place(FORWARD)
        agent.move(LEFT, 1)
player.on_chat("Wall", on_chat3)

#### Day 3


def on_chat5():
    for count in range(6):
        agent.move(UP, 1)
        agent.place(DOWN)
player.on_chat("pillar", on_chat5)










