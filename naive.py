from common.bounding_ribbon import BoundingRibbon

class NaiveRectangleFit:
    def __init__(self, rectangles):
        self.rectangles = rectangles
        self.lower_bound = max(map(lambda r: r.w(), self.rectangles))
        self.upper_bound = float(sum(map(lambda r: r.w(), self.rectangles)))

    def initial_guess(self):
        return self.upper_bound / 2

    def last_height(self):
        return self.last_ribbon.height()

    def __call__(self, max_width, debug = False):
        if max_width < self.lower_bound or max_width > self.upper_bound:
            return float('inf')

        self.last_ribbon = BoundingRibbon(max_width)
        ribbon = self.last_ribbon
        current_level_h = 0.0
        current_level_x = 0.0
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
                current_level_x = 0.0
                maximum_h_for_level = float('-inf')

        if debug:
            ribbon.debug()

        return ribbon.area()
