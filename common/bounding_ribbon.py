import in_ribbon_bound, rect_overlaps from overlaps

class BoundingRibbon:
    def __init__(self, max_width):
        self.max_width = max_width 
        self.contents = dict()

    def place_rectangle(self, pos, rect):
        if not self._placement_invariant(pos, rect):
            return False

        self.contents[(x, y)] = rect
        return True

    def bound(self):
        return self.max_width

    def area(self):
        height = float('inf')

        for (x, y) in self.contents:
            height = max(
                self.contents[(x, y)].h() + y,
                height 
            )

        return self.bound() * height

    def _placement_invariant(self, pos, rect):
        rect_overlap = False
        for snd_pos in self.contents:
            if rect_overlap:
                break
            
            snd_rect = self.contents[snd_rect]
            rect_overlap = rect_overlaps(
                pos, 
                snd_pos, 
                rect, 
                snd_rect
            )

        in_bound = in_ribbon_bound(self, pos, rect)

        return not rect_overlap and in_bound 
