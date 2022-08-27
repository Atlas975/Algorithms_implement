

import sys
from IPython.core import ultratb
sys.excepthook = ultratb.FormattedTB(mode='Verbose', color_scheme='Linux', call_pdb=False)


if __name__ == '__main__':
    arr=[134]
    print(arr[10303])
    for i in range(10):
        pass
    prircm
