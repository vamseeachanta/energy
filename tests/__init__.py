# Test package initialization
"""
Energy project test suite.

This package contains all tests for the energy project:
- unit/: Unit tests for individual components
- integration/: Integration tests for component interaction
"""

import sys
import os

# Add the src directory to the Python path for test imports
test_dir = os.path.dirname(__file__)
project_root = os.path.dirname(test_dir)
src_dir = os.path.join(project_root, 'src')

if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

# Set testing environment
os.environ['TESTING'] = 'true'