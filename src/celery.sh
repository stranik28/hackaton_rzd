#!/bin/bash

if [[ "${1}" == "celery" ]]; then
  python3 -m celery --app=emails.email:celery worker -l INFO
elif [[ "${1}" == "flower" ]]; then
  python3 -m celery --app=emails.email:celery flower
fi