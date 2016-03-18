from enum import Enum

from pyrsistent import field, PRecord, pmap_field
import toolz

try:
    basestring
except NameError:
    basestring = str

__all__ = ["Direction", "Glue",
           "add_transition", "join",
           "Tile", "format_tile", "new_tile",
           "dirbind", "eastbind", "westbind", "northbind", "southbind",
           "dirlabel", "eastlabel", "westlabel", "northlabel", "southlabel"]


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


class Glue(PRecord):
    label = field(basestring, initial="")
    strength = field(int, initial=0,
                     invariant=lambda x: (x in (0, 1, 2), "invalid strength"))


class Tile(PRecord):
    name = field(basestring)
    label = field(basestring)
    tilecolor = field(basestring)  # TODO: enum for colors?
    textcolor = field(basestring)
    concentration = field(int)
    glues = pmap_field(key_type=(Direction, type(Direction.North)),
                       value_type=Glue)  # TODO: invariant?


def join(tt1, tt2):
    pass


def add_transition():
    pass


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
            Direction.North: Glue(label="", strength=0),
            Direction.South: Glue(label="", strength=0),
            Direction.West: Glue(label="", strength=0),
            Direction.East: Glue(label="", strength=0),
        }
    # TODO: validate
    return Tile(name=name,
                label=label,
                tilecolor=tilecolor,
                textcolor=textcolor,
                concentration=concentration,
                glues=glues)


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
