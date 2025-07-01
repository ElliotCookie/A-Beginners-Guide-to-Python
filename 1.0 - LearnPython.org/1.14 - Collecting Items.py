import player

# Add a number at the end of the function to walk forward

player.move_forward(2)
player.turn_right()

# Continue writing your code here:
player.move_forward(2)
for _ in range(3):
    player.turn_left()
    player.move_forward(4)
