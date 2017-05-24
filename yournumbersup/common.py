from . import stats


class BaseDraw(object):

    def __init__(self):
        self.combs_counts = {}

    def update_draw_combs(self, balls):
        draw_combs = stats.powerset(balls)
        for draw_comb in draw_combs:
            comb_count = self.combs_counts.get(draw_comb, 0)
            self.combs_counts[draw_comb] = comb_count + 1

            print(draw_comb, self.combs_counts[draw_comb])
