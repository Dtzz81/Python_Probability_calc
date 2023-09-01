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
        if number_of_draw_balls >= len(self.contents):
            drawn_balls = self.contents
            self.contents = []
        else:
            drawn_balls = random.sample(self.contents, number_of_draw_balls)
            for ball in drawn_balls:
                self.contents.remove(ball)
        return drawn_balls

    def probability (self, ball_colour):
        balls_total = len(self.contents)
        colours_total = self.contents.count(ball_colour)
        return colours_total / balls_total

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_balls_matching_result = 0

    for i in range(num_experiments):
        new_hat = Hat()
        new_hat = copy.deepcopy(hat)
        drawn_balls = new_hat.draw(num_balls_drawn)
        counts = {}
        for ball in drawn_balls:
            counts[ball] = counts.get(ball, 0) + 1

        compare = all(expected_balls.get(color, 0) <= counts.get(color, 0)
                        for color in expected_balls.keys())

        if compare:
            expected_balls_matching_result += 1

    probability = expected_balls_matching_result / num_experiments
    return probability

