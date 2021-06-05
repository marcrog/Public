import items as i
import roba.coord as c

class Cell:
    def __init__(self, left_coord, top_coord, tab_coord):
        self.l_c = left_coord
        self.t_c = top_coord
        self.tab_c = tab_coord

    def findValue(self):

