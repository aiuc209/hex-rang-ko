import pytest
from your_module import hex_to_hsl, hex_colors

def test_hex_to_hsl():
    assert hex_to_hsl("#ffffff") == (0, 0, 100)
    assert hex_to_hsl("#000000") == (0, 0, 0)
    assert hex_to_hsl("#ff0000") == (0, 100, 50)

def test_map_hex_to_hsl():
    hsl_colors = list(map(hex_to_hsl, hex_colors))
    assert len(hsl_colors) == len(hex_colors)
    for hsl in hsl_colors:
        assert isinstance(hsl, tuple)
        assert len(hsl) == 3

def test_invalid_hex():
    with pytest.raises(ValueError):
        hex_to_hsl("invalid_hex")

def test_empty_hex_list():
    assert list(map(hex_to_hsl, [])) == []
