from src.calc import experiment
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
    probability_green = experiment(hat, {"green": 1}, 1, 10000)
    actual = probability_green
    expected = 0.5
    assert (actual - expected) < 0.01

def test_draw_number_exceeds_original_number_of_balls():
    hat = Hat(blue=1, green=1)
    hat.draw(3)
    assert len(hat.contents) == 2

def test_probability_count():
    probability = experiment(Hat(blue=3, red=2, green=6), expected_balls={"blue": 2, "green": 1}, num_balls_drawn=4, num_experiments=10000)
    actual = probability
    print(actual)
    expected = 0.272
    print(actual - expected)
    assert (actual - expected) < 0.01

def test_hat_class_contents():
    hat = Hat(red=3, blue=2)
    actual = hat.contents
    expected = ["red", "red", "red", "blue", "blue"]
    assert actual == expected
