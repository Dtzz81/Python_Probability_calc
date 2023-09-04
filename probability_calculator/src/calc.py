import copy
import random

class Hat:
    def __init__(self, **balls):
        self.ball_list = []
        counter = 0
        for colour, number in balls.items():
            for i in range(number):
                counter += 1
                self.ball_list.append(colour)

        self.contents = self.ball_list

    def draw(self, number_of_draw_balls):
        if number_of_draw_balls > len(self.contents):
            return self.contents.copy()
        # number_of_draw_balls is always the minimum between number_of_draw_balls and len(self.contents)
        return random.sample(self.contents, number_of_draw_balls)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiment = 0

    for _ in range(num_experiments):
        drawn_balls = hat.draw(num_balls_drawn)
        counts = {}

        # transform drawn balls list into a dictionary
        for ball in drawn_balls:
            # if ball in counts.keys():
            #     counts[ball] += 1
            # else:
            #     counts[ball] = 1
            counts[ball] = counts.get(ball, 0) + 1

        # are all drawn balls into expected? (same number)
        compare = all(expected_balls.get(color, 0) <= counts.get(color, 0)
                        for color in expected_balls.keys())

        # compare = True
        # for color in expected_balls.keys():
        #     compare = compare and expected_balls.get(color, 0) <= counts.get(color, 0)

        if compare:
            successful_experiment += 1

    probability = successful_experiment / num_experiments
    return probability

# inilise result, compute the result and return result
#output   list = ("black", "red", "blue")
#input   dictionary = {"black": 2, "red": 1, "blue": 1}


        #colours = balls.colours
