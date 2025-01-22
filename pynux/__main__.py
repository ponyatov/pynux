import sys

import pynux

cmd = {'about': pynux.about, 'install': pynux.install}

print(cmd[sys.argv[1]]())
