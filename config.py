from yournumbersup.pbdraw import PowerBallDraw
from yournumbersup.ozdraw import OzLottoDraw


class Config(object):
    def __init__(self, uri, output, draw_klass):
        self.uri = uri
        self.output = output
        self.draw_klass = draw_klass

configs = {'pb': Config('https://tatts.com/DownloadFile.ashx?product=Powerball', 'pb_output', PowerBallDraw),
           'oz': Config('https://tatts.com/DownloadFile.ashx?product=OzLotto', 'oz_output', OzLottoDraw)}
