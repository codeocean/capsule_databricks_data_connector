from databricks import sql
import os
import logging
from pathlib import Path
import argparse
import pandas as pd
import sys

logger = logging.getLogger(__name__)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def main():
    parser = argparse.ArgumentParser(description='Databricks SQL Connector')
    parser.add_argument('--hostname', required=True, help="Connections Details - Hostname", type=str)
    parser.add_argument('--httppath', required=True, help="Connections Details - HTTPPath", type=str)
    parser.add_argument('--catalog', required=True, help="Catalog Name", type=str)
    parser.add_argument('--SQLQuery', required=True, help="Provide your SQL Query", type=str)
    parser.add_argument('--file_name', default='output', help="Output file name.", type=str)
    parser.add_argument('--output_format', default='csv', help="Output format", choices=['csv', 'tsv','parquet','json','excel'], type=str)

    args = parser.parse_args()

    try: 
        with sql.connect(server_hostname = args.hostname,
                    http_path       = args.httppath,
                    access_token    = os.environ['API_SECRET'],
                    catalog = args.catalog) as connection:
            
            logger.info(f"Executing SQL Query : {args.SQLQuery}")

            with connection.cursor() as cursor:
                cursor.execute(args.SQLQuery)
                result = cursor.fetchall()
    except sql.exc.RequestError:
        logger.error(f"Unable to access Databricks")
        return 1
    except sql.exc.ServerOperationError:
        logger.error(f"Unable to execute SQL query")
        return 1
    except Exception as e: 
        logger.error(f"Unable to execute SQL query {e}")
        return 1

    output_frame = pd.DataFrame(result)

    output_file = Path("../results") / Path(args.file_name + '.' + args.output_format)

    match args.output_format: 
        case 'tsv': 
            output_frame.to_csv(output_file, sep='\t')
        case 'csv': 
            output_frame.to_csv(output_file, sep=',')
        case 'parquet':
            output_frame.to_parquet(output_file)
        case 'json':
            output_frame.to_json(output_file)
        case 'excel':
            output_frame.to_excel(output_file)        

    return 0

if __name__ == '__main__':
    sys.exit(main())