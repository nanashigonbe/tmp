#!/usr/bin/env python

#
# Licence by TYOBFQIV Co., Ltd.
# 2021/6/16
#

import logging
import boto3
from botocore.exceptions import ClientError

aws_access_key = "T1YOB680FQIVF1MM3441"
aws_secret_key = "4v/oYc7k3m3bIUb3y44yTW24rZleEu/L0T0IlHEs"

def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name

    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
    
if __name__ == "__main__":
    upload_file("secret.txt", "test_bucket")