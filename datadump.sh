#!/bin/bash
mysqldump --host=mysql --port=3306 --user=root --password sales sales_data > sales_data.sql