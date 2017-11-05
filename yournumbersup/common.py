import random
from collections import Counter

from . import stats


class BaseDraw(object):
    max_ball = 0
    max_combs = []

    def __init__(self):
        self.combs_counts = {}
        self.black_list = {}
        self.lowest_max = BaseDraw.max_ball
        self.highest_min = 1

    def parse_previous_draw(self, balls):

        min_ball = min(balls)
        max_ball = max(balls)

        if min_ball > self.highest_min:
            self.highest_min = min_ball

        if max_ball < self.lowest_max:
            self.lowest_max = max_ball

        self.update_draw_combs(balls)

    def update_draw_combs(self, balls):
        draw_combs = stats.powerset(balls)
        for draw_comb in draw_combs:
            comb_count = self.combs_counts.get(draw_comb, 0)
            self.combs_counts[draw_comb] = comb_count + 1

            if self.combs_counts[draw_comb] >= BaseDraw.max_combs[len(draw_comb)]:
                self.black_list.setdefault(len(draw_comb), set()).add(draw_comb)

    def is_valid_draw(self, balls):

        draw_combs = stats.powerset(balls)
        for draw_comb in draw_combs:
            if draw_comb in self.black_list.get(len(draw_comb), set()):
                return False

        return True

    def pick_balls(self, max_ball, pick_count):
        available_balls = list(range(1, max_ball + 1))
        picked_balls = set()
        while pick_count > 0:
            while True:
                picked_ball = random.choice(available_balls)
                picked_balls.add(picked_ball)
                available_balls.remove(picked_ball)

                if picked_balls in self.black_list.get(len(picked_balls), set()):
                    print('YAY')
                    exit(0)

                if len(available_balls) <= 0:
                    print('OK')
                    exit(0)

                pick_count -= 1
                break

        return picked_balls

    def summarize_stats(self):
        pass
