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
        if len(self.contents) == 0:
            if len(self.ball_list) < number_of_draw_balls:
                self.contents = self.ball_list
                return self.contents


        drawn_balls = random.sample(self.contents, number_of_draw_balls)
        self.contents = [ball for ball in self.contents if ball not in drawn_balls]
        return drawn_balls

    def experiment(self, expected_balls, num_balls_drawn, num_experiments):
        total_draws = 0

        for i in range(num_experiments):
            new_contents = self.contents.copy()
            drawn_balls = new_contents.draw(num_balls_drawn)
            counts = {}
            for ball in drawn_balls:
                counts[ball] = counts =+ 1
                

     """    count = 0
        for i in range(num_experiments):
            new_contents = self.contents.copy()
            drawn_balls = self.draw_balls(new_contents, num_balls_drawn)

            if self.check_expected(drawn_balls, expected_balls):
                count += 1

        return count / num_experiments """

""" def probability(self, ball_colour):
        balls_total = len(self.ball_list)
        colours_total = self.ball_list.count(ball_colour)
        if
        return colours_total / balls_total """







# inilise result, compute the result and return result
#output   list = ("black", "red", "blue")
#input   dictionary = {"black": 2, "red": 1, "blue": 1}


        #colours = balls.colours

