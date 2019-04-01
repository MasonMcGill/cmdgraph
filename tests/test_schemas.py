import sys
sys.path.append('../cmdgraph')

from .shared_defs import SineWave

#------------------------------------------------------------------------------

def test_schemas() -> None:
    assert SineWave is not None
