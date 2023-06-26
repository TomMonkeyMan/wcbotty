#!/bin/bash

set -e

crontab cron_jobs.txt

echo "`crontab -l`"
echo "`service cron status`"

