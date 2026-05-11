#!/bin/bash
echo "Runner called with args: $@" >> runner_log.txt
DJANGO_SETTINGS_MODULE=settings_for_test venv/bin/pytest repositories/ "$@" >> runner_log.txt 2>&1
exit_code=$?
echo "Exit code: $exit_code" >> runner_log.txt
exit $exit_code
