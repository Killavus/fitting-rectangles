from overlaps import in_ribbon_bound, rect_overlaps

class BoundingRibbon:
    def __init__(self, max_width):
        self.max_width = max_width 
        self.contents = dict()
        self._pos_in_order = []

    def place_rectangle(self, pos, rect):
        if not self._placement_invariant(pos, rect):
            return False

        self.contents[pos] = rect
        self._pos_in_order.append(pos)
        return True

    def bound(self):
        return self.max_width

    def height(self):
        height = float('-inf')

        for (x, y) in self.contents:
            height = max(
                self.contents[(x, y)].h() + y,
                height 
            )

        return height

    def area(self):
        return self.bound() * self.height()

    def debug(self):
        for pos in self._pos_in_order:
            print "Rectangle (%02f, %02f) placed on x = %02f, y = %02f" % (self.contents[pos].w(), self.contents[pos].h(), pos[0], pos[1])

    def _placement_invariant(self, pos, rect):
        rect_overlap = False
        for snd_pos in self.contents:
            if rect_overlap:
                break
            
            snd_rect = self.contents[snd_pos]
            rect_overlap = rect_overlaps(
                pos, 
                snd_pos, 
                rect, 
                snd_rect
            )

        in_bound = in_ribbon_bound(self, pos, rect)

        return not rect_overlap and in_bound 
