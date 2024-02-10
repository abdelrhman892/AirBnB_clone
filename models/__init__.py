#!/usr/bin/python3
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()

# make storage accessable
__all__ = ['storage']
