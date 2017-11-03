from collections import Counter

from . import stats


class BaseDraw(object):
    def __init__(self):
        self.combs_counts = {}
        self.max_lowest_ball = 0
        self.min_ball_distribution = []
        self.max_ball_distribution = []
        self.min_ball_counts = None
        self.max_ball_counts = None

    def parse_previous_draw(self, balls):
        lowest_ball = sorted(balls)[0]

        if lowest_ball > self.max_lowest_ball:
            self.max_lowest_ball = lowest_ball

        self.update_draw_combs(balls)

    def update_draw_combs(self, balls):
        draw_combs = stats.powerset(balls)
        for draw_comb in draw_combs:
            comb_count = self.combs_counts.get(draw_comb, 0)
            self.combs_counts[draw_comb] = comb_count + 1

        min_ball = min(balls)
        self.min_ball_distribution.append(min_ball)

        max_ball = max(balls)
        self.max_ball_distribution.append(max_ball)

    def summarize_stats(self):
        self.min_ball_distribution.sort()
        self.max_ball_distribution.sort()
        self.min_ball_counts = Counter(self.min_ball_distribution)
        self.max_ball_counts = Counter(self.max_ball_distribution)
