import sys
sys.path.append('../cmdgraph')

from .shared_defs import SineWave

#------------------------------------------------------------------------------

def test_io() -> None:
    assert SineWave is not None
