import random

from yournumbersup import stats


class OzLottoDraw(object):
    max_ball = 45
    max_combs = [None, None, None, 12, 6, 3, 2, 2, 1, 1]

    def __init__(self):
        self.combs_counts = {}

    def parse_previous_draw(self, data):
        balls = set([int(x) for x in data[2:11]])

        draw_combs = stats.powerset(balls)
        for draw_comb in draw_combs:
            comb_count = self.combs_counts.get(draw_comb, 0)
            self.combs_counts[draw_comb] = comb_count + 1

    def valid_draw(self, balls, sups):
        while not self._is_valid_draw(balls):
            balls = random.sample(range(1, OzLottoDraw.max_ball + 1), 7)

        return sorted(balls), sups

    def _is_valid_draw(self, balls):

        if balls is None:
            return False

        balls_combs = stats.powerset(balls)

        for ball_comb in balls_combs:
            if len(ball_comb) > 7:
                continue

            comb_count = self.combs_counts.get(ball_comb, -1)
            if comb_count >= OzLottoDraw.max_combs[len(ball_comb)]:
                print(ball_comb, comb_count, " - Skipping already draw too many times")
                return False

        return True

        return sorted(balls), sups
