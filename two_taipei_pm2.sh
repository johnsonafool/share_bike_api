#!/bin/bash
pm2 start "uvicorn two_taipei_api:app --reload --host 0.0.0.0 --port 8887" --name "gbfs_two_taipei_api"