import numpy as np
import parsers

from utils import operators

class AtomicStructure(object):

    def __init__(self, header: str = "structure", unitcell: list = None, elements: list = None,
                 coord_cart: bool = False, coords: list = None, seldyn: list = None, others: dict = None):
        self.header = header
        self.unitcell = unitcell
        self.elements = elements
        self.coord_cart = coord_cart
        self.coords = coords
        self.seldyn = seldyn
        self.others = others

    def read_list(self, inlist):
        return

    def read_dict(self, indict):
        return

    def read_file(self, infile):
        return