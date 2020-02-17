#!/usr/bin/python3
"""creates instance for FileStorage application"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
