import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend")))

from app.database import Base  # Change 'app.database' to just 'database'
target_metadata = Base.metadata
