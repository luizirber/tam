import hypothesis

import tam
import tam.defs
from tam.defs import Direction
from tam.defs import Glue
from tam.defs import Tile


def test_main():
    assert tam  # use your library here


def test_opposite_directions():
    assert Direction.North.opposite() is Direction.South
    assert Direction.South.opposite() is Direction.North
    assert Direction.West.opposite() is Direction.East
    assert Direction.East.opposite() is Direction.West


def test_glue_strength_defaults():
    test_tile = tam.defs.new_tile("test")

    assert tam.defs.northbind(test_tile) == 0
    assert tam.defs.southbind(test_tile) == 0
    assert tam.defs.eastbind(test_tile) == 0
    assert tam.defs.westbind(test_tile) == 0


def test_glue_label_defaults():
    test_tile = tam.defs.new_tile("test")

    assert tam.defs.northlabel(test_tile) == ""
    assert tam.defs.southlabel(test_tile) == ""
    assert tam.defs.eastlabel(test_tile) == ""
    assert tam.defs.westlabel(test_tile) == ""


def test_glue_strength():
    test_tile = tam.defs.new_tile("test", glues={
        Direction.North: Glue("", 1),
        Direction.South: Glue("", 2),
        Direction.West: Glue("", 3),
        Direction.East: Glue("", 4),
    })

    assert tam.defs.northbind(test_tile) == 1
    assert tam.defs.southbind(test_tile) == 2
    assert tam.defs.westbind(test_tile) == 3
    assert tam.defs.eastbind(test_tile) == 4


def test_glue_label():
    test_tile = tam.defs.new_tile("test", glues={
        Direction.North: Glue("a", 1),
        Direction.South: Glue("b", 2),
        Direction.West: Glue("c", 3),
        Direction.East: Glue("d", 4),
    })

    assert tam.defs.northlabel(test_tile) == "a"
    assert tam.defs.southlabel(test_tile) == "b"
    assert tam.defs.westlabel(test_tile) == "c"
    assert tam.defs.eastlabel(test_tile) == "d"
