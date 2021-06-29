from random import choice

class RandomWalk():
    """Generate a random-walk with direction and distance."""

    # Keyword argument contains 1,000 steps as default.
    def __init__(self, steps=1000):
        self.steps = steps

    # Main method to create data of a random walk.
    def fill_walk(self):
        # Points first start at 0, 0 and are stored in current_x and current_y.
        current_x, current_y = 0, 0
        # List containing walk data.
        walk = [(current_x, current_y)]

        # For-loop running for however many steps.
        for i in range(self.steps):
            x_direction = choice([1, -1]) # 1 is right, -1 is left.
            x_distance = choice([0, 1, 2, 3, 4, 5])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1]) # 1 is down, -1 is up.
            y_distance = choice([0, 1, 2, 3, 4, 5])
            y_step = y_direction * y_distance

            if x_step and y_step == 0: # Reject positions that move nowhere.
                pass
            
            # Add x/y to previous x/y position. Start of program is (0, 0).
            x_pos = current_x + x_step 
            y_pos = current_y + y_step 

            # Create new checkpoint by assigning current_x/y to x/y_pos.
            current_x = x_pos 
            current_y = y_pos

            xy_tuple = (x_pos, y_pos)
            
            walk.append(xy_tuple)

        return walk