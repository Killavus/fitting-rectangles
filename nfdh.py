from naive import NaiveRectangleFit

class NextDecreasingRectangleFit:
    def __init__(self, rectangles):
        self.naive = NaiveRectangleFit(
            list(reversed(sorted(rectangles, key=lambda r: r.h())))
        )

    def initial_guess(self):
        return self.naive.initial_guess()

    def __call__(self, max_width, debug=False):
        return self.naive(max_width, debug)
