import random

from yournumbersup import stats


class PowerBallDraw(object):
    max_ball = 40
    max_combs = [None, None, None, 7, 3, 2, 1]

    min_pball = 10
    max_pball = 20

    def parse_previous_draw(self, data):

        balls = set([int(x) for x in data[2:7]])
        if data[7] != '-' and data[8] != '-':
            balls.add(int(data[7]))

        draw_combs = stats.powerset(balls)
        for draw_comb in draw_combs:
            comb_count = self.combs_counts.get(draw_comb, 0)
            self.combs_counts[draw_comb] = comb_count + 1

    def __init__(self):
        self.combs_counts = {}

    def valid_draw(self, balls, sups):
        while not self._is_valid_draw(balls):
            balls = random.sample(range(1, PowerBallDraw.max_ball + 1), 6)

        while not self._is_valid_powerball(sups):
            sups = [random.randint(PowerBallDraw.min_pball, PowerBallDraw.max_pball)]

        return sorted(balls), sorted(sups)

    def _is_valid_draw(self, balls):

        if balls is None:
            return False

        balls_combs = stats.powerset(balls)

        for ball_comb in balls_combs:
            comb_count = self.combs_counts.get(ball_comb, -1)
            if comb_count >= PowerBallDraw.max_combs[len(ball_comb)]:
                print(ball_comb, comb_count, " - Skipping already draw too many times")
                return False

        return True

    def _is_valid_powerball(self, sups):
        if sups is None:
            return False

        powerball = sups[0]

        if powerball < PowerBallDraw.min_pball or powerball > PowerBallDraw.max_pball:
            return False

        return True
