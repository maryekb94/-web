__requires__ = 'TestProject==0.0'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('TestProject==0.0', 'console_scripts', 'initialize_TestProject_db')()
    )
