import random

from . import stats
from .common import BaseDraw


class PowerBallPHDraw(BaseDraw):
    max_ball = 40
    max_combs = [None, None, None, 7, 3, 2, 1]
    min_min_count = 4

    def parse_previous_draw(self, data):

        balls = set([int(x) for x in data[2:7]])
        if data[7] != '-' and data[8] != '-':
            balls.add(int(data[7]))

        super().parse_previous_draw(balls)

    def valid_draw(self, balls, sups):
        if sups is None:
            sups = []

        if balls is None or not super().is_valid_draw(balls + sups):
            print('Picking New Entry')
            balls = list(super().pick_balls(BaseDraw.max_ball, 6))

        while not self.is_valid_draw(balls + sups):
            print('Re-picking an invalid entry')
            balls = list(super().pick_balls(BaseDraw.max_ball, 6))

        return sorted(balls), sorted(sups)
