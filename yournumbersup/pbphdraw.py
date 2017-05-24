import random

from . import stats
from .common import BaseDraw


class PowerBallPHDraw(BaseDraw):
    max_ball = 40
    max_combs = [None, None, None, 7, 3, 2, 1]

    def parse_previous_draw(self, data):

        balls = set([int(x) for x in data[2:7]])
        if data[7] != '-' and data[8] != '-':
            balls.add(int(data[7]))

        self.update_draw_combs(balls)

    def valid_draw(self, balls, sups):
        while not self._is_valid_draw(balls):
            balls = random.sample(range(1, PowerBallPHDraw.max_ball + 1), 6)

        return sorted(balls), sups

    def _is_valid_draw(self, balls):

        if balls is None:
            return False

        balls_combs = stats.powerset(balls)

        for ball_comb in balls_combs:
            comb_count = self.combs_counts.get(ball_comb, -1)
            if comb_count >= PowerBallPHDraw.max_combs[len(ball_comb)]:
                print(ball_comb, comb_count, " - Skipping already draw too many times")
                return False

        self.update_draw_combs(balls)

        return True
