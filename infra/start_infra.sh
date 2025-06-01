#!/bin/bash

export $(grep -v '^#' ../.env | xargs -0)

docker compose up -d