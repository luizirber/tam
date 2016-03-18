from hypothesis import strategies as st
from hypothesis import given

import tam
from tam import Direction, Glue

glue_strength_st = st.integers(min_value=0, max_value=2)

def test_main():
    assert tam  # use your library here


def test_opposite_directions():
    assert Direction.North.opposite() is Direction.South
    assert Direction.South.opposite() is Direction.North
    assert Direction.West.opposite() is Direction.East
    assert Direction.East.opposite() is Direction.West


def test_glue_strength_defaults():
    test_tile = tam.new_tile("test")

    assert tam.northbind(test_tile) == 0
    assert tam.southbind(test_tile) == 0
    assert tam.eastbind(test_tile) == 0
    assert tam.westbind(test_tile) == 0


def test_glue_label_defaults():
    test_tile = tam.new_tile("test")

    assert tam.northlabel(test_tile) == ""
    assert tam.southlabel(test_tile) == ""
    assert tam.eastlabel(test_tile) == ""
    assert tam.westlabel(test_tile) == ""


@given(st.fixed_dictionaries({
  Direction.North: st.builds(Glue, label=st.text(), strength=glue_strength_st),
  Direction.South: st.builds(Glue, label=st.text(), strength=glue_strength_st),
  Direction.West: st.builds(Glue, label=st.text(), strength=glue_strength_st),
  Direction.East: st.builds(Glue, label=st.text(), strength=glue_strength_st)
}))
def test_glue_properties(g):
    test_tile = tam.new_tile("test", glues=g)

    assert tam.northbind(test_tile) == g[Direction.North].strength
    assert tam.southbind(test_tile) == g[Direction.South].strength
    assert tam.westbind(test_tile) == g[Direction.West].strength
    assert tam.eastbind(test_tile) == g[Direction.East].strength

    assert tam.northlabel(test_tile) == g[Direction.North].label
    assert tam.southlabel(test_tile) == g[Direction.South].label
    assert tam.westlabel(test_tile) == g[Direction.West].label
    assert tam.eastlabel(test_tile) == g[Direction.East].label
