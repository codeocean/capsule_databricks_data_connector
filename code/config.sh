#!/usr/bin/env bash

if [ $# -eq 0 ]; then
    echo "No arguments supplied"
fi

if [ -z "${1}" ]; then
  hostname="dbc-2a6017bc-079e.cloud.databricks.com"
else
  hostname="${1}"
fi

if [ -z "${2}" ]; then
  httppath="/sql/1.0/warehouses/0c7a8dff9ad0e63c"
else
  httppath="${2}"
fi

if [ -z "${3}" ]; then
  catalog="hive_metastore"
else
  catalog="${3}"
fi

if [ -z "${4}" ]; then
  SQL_query="SELECT * FROM default.diamonds LIMIT 2"
else
  SQL_query="${4}"
fi

if [ -z "${5}" ]; then
  file_name="output"
else
  file_name="${5}"
fi

if [ -z "${6}" ]; then
  output_format="csv"
else
  output_format="${6}"
fi