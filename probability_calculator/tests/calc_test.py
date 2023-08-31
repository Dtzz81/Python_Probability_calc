from src.calc import Hat

def test_hat_has_one_ball():
    hat = Hat(black=1)
    actual = hat.contents
    expected = ["black"]
    assert actual == expected

def test_hat_has_different_colours_of_balls():
    hat = Hat(black=1, red=2)
    actual = hat.contents
    expected = ["black", "red", "red"]
    assert actual == expected

def test_hat_class_contents_their_test():
    hat = Hat(red=3, blue=2)
    actual = hat.contents
    expected = ["red", "red", "red", "blue", "blue"]
    assert actual == expected

def test_probability_is_fifty_fifty():
    hat = Hat(blue=1, green=1)
    probability_green = hat.probability("green")
    actual = probability_green
    expected = 0.5
    assert actual == expected

def test_draw_number_exceeds_original_number_of_balls():
    hat = Hat(blue=1, green=1)
    hat.draw(3)
    probability_green = hat.probability("green")
    actual = probability_green
    expected = 0.5
    assert actual == expected


""" def test_probability_count():
    hat = Hat(blue=3, red=2, green=6)
    probability = hat.experiment(expected_balls={"blue": 2, "green": 1}, num_balls_drawn=4, num_experiments=1000)
    actual = probability
    expected = 0.272
    assert abs(actual - expected) < 0.01 """


# Their tests:
"""
probability_calculator.random.seed(95)

def test_hat_class_contents():
    hat = prob_calculator.Hat(red=3, blue=2)
    actual = hat.contents
    expected = ["red", "red", "red", "blue", "blue"]
    assert actual == expected, 'Expected creation of hat object to add correct contents.'

def test_hat_draw():
    hat = prob_calculator.Hat(red=5, blue=2)
    actual = hat.draw(2)
    expected = ['blue', 'red']
    assert actual == expected, 'Expected hat draw to return two random items from hat contents.'
    actual = len(hat.contents)
    expected = 5
    assert actual == expected, 'Expected hat draw to reduce number of items in contents.'

def test_prob_experiment():
    hat = prob_calculator.Hat(blue=3, red=2, green=6)
    probability = prob_calculator.experiment(hat=hat, expected_balls={"blue": 2, "green": 1}, num_balls_drawn=4, num_experiments=1000)
    actual = probability
    expected = 0.272
    assert abs(actual - expected) < 0.01, 'Expected experiment method to return a different probability.'

    hat = prob_calculator.Hat(yellow=5, red=1, green=3, blue=9, test=1)
    probability = prob_calculator.experiment(hat=hat, expected_balls={"yellow": 2, "blue": 3, "test": 1}, num_balls_drawn=20, num_experiments=100)
    actual = probability
    expected = 1.0
    assert abs(actual - expected) < 0.01, 'Expected experiment method to return a different probability.'

 """
