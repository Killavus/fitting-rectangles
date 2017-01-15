from common.bounding_ribbon import *

class NaiveRectangleFit:
    def __init__(self, rectangles):
        self.rectangles = rectangles
        self.minimum_width = max(map(lambda r: r.w(), self.rectangles))

    def initial_guess(self):
        return self.minimum_width

    def __call__(self, max_width, debug = False):
        if max_width < self.minimum_width:
            return float('inf')

        ribbon = BoundingRibbon(max_width)
        current_level_h = 0
        current_level_x = 0
        current_index = 0
        maximum_h_for_level = float('-inf')

        while current_index < len(self.rectangles):
            rectangle = self.rectangles[current_index]
            success = ribbon.place_rectangle(
                        (current_level_x, current_level_h),
                        rectangle)

            if success:
                current_index += 1
                current_level_x += rectangle.w()
                maximum_h_for_level = max(rectangle.h(), maximum_h_for_level)
            else:
                current_level_h += maximum_h_for_level
                current_level_x = 0
                maximum_h_for_level = float('-inf')

        if debug:
            ribbon.debug()

        return ribbon.area()
