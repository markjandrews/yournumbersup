import random

from . import stats
from .common import BaseDraw


class OzLottoDraw(BaseDraw):
    max_ball = 45
    max_combs = [None, None, None, 12, 6, 3, 2, 2, 1, 1]
    min_min_count = 5

    def parse_previous_draw(self, data):
        balls = set([int(x) for x in data[2:11]])

        super().parse_previous_draw(balls)

    def valid_draw(self, balls, sups):
        while not self._is_valid_draw(balls):
            while True:
                min_ball = random.choice(self.min_ball_distribution)
                max_ball = random.choice(self.max_ball_distribution)

                if max_ball - min_ball >= 7:
                    break;

            balls = random.sample(range(min_ball, max_ball + 1), 7)

        return sorted(balls), sups

    def _is_valid_draw(self, balls):

        if balls is None:
            return False

        if sorted(balls)[0] > self.max_lowest_ball:
            return False

        min_ball = self.min_ball_counts.get(min(balls), 0)
        if min_ball < self.min_min_count:
            return False

        balls_combs = stats.powerset(balls)

        for ball_comb in balls_combs:
            if len(ball_comb) > 7:
                continue

            comb_count = self.combs_counts.get(ball_comb, -1)
            if comb_count >= OzLottoDraw.max_combs[len(ball_comb)]:
                print(ball_comb, comb_count, " - Skipping already draw too many times")
                return False

        self.update_draw_combs(balls)

        return True
