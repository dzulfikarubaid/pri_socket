#!/bin/bash
gunicorn -k uvicorn.workers.UvicornWorker new:app --bind 0.0.0.0:8000