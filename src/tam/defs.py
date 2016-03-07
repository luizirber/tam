from collections import namedtuple
from enum import Enum

import toolz


class Direction(Enum):
    North = 1
    South = 2
    East = 3
    West = 4

    def opposite(self):
        if self == Direction.North:
            return Direction.South
        elif self == Direction.South:
            return Direction.North
        elif self == Direction.West:
            return Direction.East
        elif self == Direction.East:
            return Direction.West
        else:
            raise TypeError("Invalid direction")


Glue = namedtuple("Glue", ('label', 'strength'))


Tile = namedtuple("Tile", ("name", "label", "tilecolor", "textcolor", "concentration", "glues"))


def dirbind(tile, direction=Direction.North):
    return tile.glues[direction].strength


def dirlabel(tile, direction=Direction.North):
    return tile.glues[direction].label


northbind = toolz.partial(dirbind, direction=Direction.North)
southbind = toolz.partial(dirbind, direction=Direction.South)
eastbind = toolz.partial(dirbind, direction=Direction.East)
westbind = toolz.partial(dirbind, direction=Direction.West)


northlabel = toolz.partial(dirlabel, direction=Direction.North)
southlabel = toolz.partial(dirlabel, direction=Direction.South)
eastlabel = toolz.partial(dirlabel, direction=Direction.East)
westlabel = toolz.partial(dirlabel, direction=Direction.West)


def new_tile(name, label="", tilecolor="white", textcolor="black", concentration=1, glues=None):
    if glues is None:
        glues = {
            Direction.North: Glue("", 0),
            Direction.South: Glue("", 0),
            Direction.West: Glue("", 0),
            Direction.East: Glue("", 0),
        }
    # TODO: validate
    return Tile(name, label, tilecolor, textcolor, concentration, glues)


def format_tile(tile):
    return ("TILENAME {t.name}\n"
            "LABEL {t.label}\n"
            "TILECOLOR {t.tilecolor}\n"
            "TEXTCOLOR {t.textcolor}\n"
            "CONCENTRATION {t.concentration}\n"
            "NORTHBIND {northbind}\n"
            "SOUTHBIND {southbind}\n"
            "WESTBIND {westbind}\n"
            "EASTBIND {eastbind}\n"
            "NORTHLABEL {northlabel}\n"
            "SOUTHLABEL {southlabel}\n"
            "WESTLABEL {westlabel}\n"
            "EASTLABEL {eastlabel}\n"
            "CREATE".format(t=tile,
                            northbind=northbind(tile),
                            southbind=southbind(tile),
                            eastbind=eastbind(tile),
                            westbind=westbind(tile),
                            northlabel=northlabel(tile),
                            southlabel=southlabel(tile),
                            eastlabel=eastlabel(tile),
                            westlabel=westlabel(tile),
                            ))
