#!/bin/bash
pm2 start "uvicorn api:app --reload --host 0.0.0.0 --port 8888" --name "gbfs_taipei_api"
