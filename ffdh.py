from common.bounding_ribbon import BoundingRibbon

class FirstDecreasingRectangleFit:
    def __init__(self, rectangles):
        self.rectangles = list(reversed(sorted(rectangles, key=lambda r: r.h())))
        self.lower_bound = max(map(lambda r: r.w(), self.rectangles))
        self.upper_bound = float(sum(map(lambda r: r.w(), self.rectangles)))

    def initial_guess(self):
        return self.upper_bound / 2

    def __call__(self, max_width, debug = False):
        if max_width < self.lower_bound or max_width > self.upper_bound:
            return float('inf')

        level_xs = [0.0]
        heights = [0.0]
        current_index = 0
        open_level_maximum_h = float('-inf')
        ribbon = BoundingRibbon(max_width)

        while current_index < len(self.rectangles):
            rectangle = self.rectangles[current_index]

            placed = False
            for level_index in range(len(level_xs)):
                placed = ribbon.place_rectangle(
                    (level_xs[level_index], heights[level_index]),
                    rectangle
                )

                if placed:
                    current_index += 1
                    level_xs[level_index] += rectangle.w()
                    if level_index == len(level_xs) - 1:
                        open_level_maximum_h = max(rectangle.h(), open_level_maximum_h)
                    break

            if not placed:
                level_xs.append(0.0)
                heights.append(heights[-1] + open_level_maximum_h)
                open_level_maximum_h = float('-inf')
        
        if debug:
            ribbon.debug()

        return ribbon.area()
