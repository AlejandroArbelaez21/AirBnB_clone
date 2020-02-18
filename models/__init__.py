#!/usr/bin/python3
"""creates instance for FileStorage application"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
