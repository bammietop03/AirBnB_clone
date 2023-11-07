#!/usr/bin/python3
"""Creating a unique FIleStorage for the application."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
