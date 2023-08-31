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



    def draw (self, number_of_draw_balls):
        if len(self.ball_list) <= number_of_draw_balls:
            self.contents = self.ball_list
            return self.contents

        drawn_balls = random.sample(self.contents, number_of_draw_balls)
        self.contents = [ball for ball in self.contents if ball not in drawn_balls]
        return drawn_balls

def experiment(self, expected_balls, num_balls_drawn, num_experiments):
    expected_balls_matching_result = 0

    for i in range(num_experiments):
        new_contents = copy.deepcopy(self)
        drawn_balls = new_contents.draw(num_balls_drawn)
        counts = {}
        for ball in drawn_balls:
            counts[ball] = counts.get(ball, 0) + 1

        compare = all(expected_balls.get(color, 0) <= counts.get(color, 0)
                        for color in expected_balls.keys())

        if compare:
            expected_balls_matching_result += 1

    probability = expected_balls_matching_result / num_experiments
    return probability




# inilise result, compute the result and return result
#output   list = ("black", "red", "blue")
#input   dictionary = {"black": 2, "red": 1, "blue": 1}


        #colours = balls.colours

