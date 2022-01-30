#!/bin/bash

PROJECT=$(gcloud config get-value project)
REGION=us-central1

python -m pipeline \
  --runner=DataflowRunner \
  --project=$PROJECT \
  --region=$REGION \
  --job_name=single-file