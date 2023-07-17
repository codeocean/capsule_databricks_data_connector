#!/bin/bash

set -e

source ./config.sh

python runBricks.py --hostname "$hostname" \
             --httppath "$httppath" \
             --catalog "$catalog" \
             --SQLQuery "$SQL_query" \
             --file_name "$file_name" \
             --output_format "$output_format"