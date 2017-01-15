from numpy import random
from common.rectangle import Rectangle
import sys

def generate_test_case(w, h, exp):
    xs, ys = random.uniform(0.0, 1.0, (2, int(exp)))
    xs *= w
    ys *= h

    xs = [0.0] + list(sorted(xs)) + [w]
    ys = [0.0] + list(sorted(ys)) + [h]

    result = []

    for xindex in range(len(xs) - 1):
        startx = xs[xindex]

        for yindex in range(len(ys) - 1):
            starty = ys[yindex]
            width = xs[xindex + 1] - startx
            height = ys[yindex + 1] - starty

            result.append(Rectangle(width, height))

    return result

w, h, exp = map(float, sys.argv[1:])

samples = generate_test_case(w, h, exp)
random.shuffle(samples)

area = 0.0
for sample in samples:
    area += sample.w() * sample.h()
    print "%f %f" % (sample.w(), sample.h())
