from yournumbersup.pbdraw import PowerBallDraw
from yournumbersup.ozdraw import OzLottoDraw
from yournumbersup.pbphdraw import PowerBallPHDraw


class Config(object):
    def __init__(self, uri, cost_per_game, draw_klass):
        self.uri = uri
        self.cost_per_game = cost_per_game
        self.draw_klass = draw_klass


configs = {'pb': Config('https://tatts.com/DownloadFile.ashx?product=Powerball', 0.92, PowerBallDraw),
           'pbph': Config('https://tatts.com/DownloadFile.ashx?product=Powerball', 18.6, PowerBallPHDraw),
           'oz': Config('https://tatts.com/DownloadFile.ashx?product=OzLotto', 1.30, OzLottoDraw)}
