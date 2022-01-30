#!/bin/bash

PROJECT=$(gcloud config get-value project)
REGION=us-central1

python -m pipeline \
  --runner=DataflowRunner \
  --project=$PROJECT \
  --region=$REGION \
  --setup_file=./setup.py \
  --job_name=utils-file