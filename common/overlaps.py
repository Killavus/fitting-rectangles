def rect_overlaps(fst_pos, snd_pos, fst_rect, snd_rect):
    fst_x, fst_y = fst_pos
    snd_x, snd_y = snd_pox
    fst_w, fst_h = fst_rect.w(), fst_rect.h()
    snd_w, snd_h = snd_rect.w(), snd_rect.h()

    return not (
        (fst_x + fst_w <= snd_x) or 
        (snd_x + snd_w <= fst_x) or
        (snd_y + snd_h <= fst_y) or
        (fst_y + fst_h <= snd_y)
    )

def in_ribbon_bound(box, pos, rect):
    x = pos[0]
    bound = box.bound()

    return 0 <= x <= (bound - rect.w())

