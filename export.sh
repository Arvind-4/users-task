#!/bin/bash
poetry export --without-hashes -f requirements.txt -o requirements.txt
poetry export --without-hashes --with dev -f requirements.txt -o requirements-dev.txt