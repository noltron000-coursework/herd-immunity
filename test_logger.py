import pytest
import logger

def test_logger_init():
	# It seems there is not a lot of ways to test outputs without getting in-depth
	log = logger.Logger("new_file")
	assert log.file_name == "new_file"