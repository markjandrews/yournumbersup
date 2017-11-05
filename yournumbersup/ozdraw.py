import random

from . import stats
from .common import BaseDraw


class OzLottoDraw(BaseDraw):
    BaseDraw.max_ball = 45
    BaseDraw. max_combs = [None, None, None, 12, 6, 3, 2, 2, 1, 1]

    def parse_previous_draw(self, data):
        balls = set([int(x) for x in data[2:11]])

        super().parse_previous_draw(balls)

    def valid_draw(self, balls, sups):
        if sups is None:
            sups = []

        if balls is None or not super().is_valid_draw(balls + sups):
            print('Picking New Entry')
            picked_balls = list(super().pick_balls(BaseDraw.max_ball, 9))
            balls = picked_balls[:-2]
            sups = picked_balls[-2:]

        while not self.is_valid_draw(balls + sups):
            print('Re-picking an invalid entry')
            picked_balls = list(super().pick_balls(BaseDraw.max_ball, 9))
            balls = picked_balls[:-2]
            sups = picked_balls[-2:]

        return sorted(balls), sups
