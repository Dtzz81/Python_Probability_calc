class Hat:
    def __init__(self, **balls):
        self.ball_list = []
        counter = 0
        for colour, number in balls.items():
            for i in range(number):
                counter += 1
                self.ball_list.append(colour)

        self.contents = self.ball_list

    def probability(self, ball_colour):
        balls_total = len(self.ball_list)
        colours_total = self.ball_list.count(ball_colour)
        return colours_total / balls_total

    def draw (self, ball_list):
        self.ball_list = []
        
        counter = 0
        for colour, number in balls.items():
            for i in range(number):
                counter += 1
                self.ball_list.append(colour)

        self.contents = self.ball_list

    """ def experiment(self, expected_balls, num_balls_drawn, num_experiments):
        count = 0
        for i in range(num_experiments):
            new_contents = self.contents.copy()
            drawn_balls = self.draw_balls(new_contents, num_balls_drawn)

            if self.check_expected(drawn_balls, expected_balls):
                count += 1

        return count / num_experiments """





# inilise result, compute the result and return result
#output   list = ("black", "red", "blue")
#input   dictionary = {"black": 2, "red": 1, "blue": 1}


        #colours = balls.colours

