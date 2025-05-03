import boto3, botocore
from config import S3_KEY, S3_SECRET, S3_BUCKET,SECRET_KEY
import boto3
from botocore.exceptions import NoCredentialsError
import logging
import os
import boto3
import io
import random
logging.getLogger('boto3').setLevel(logging.CRITICAL)
logging.getLogger('botocore').setLevel(logging.CRITICAL)
logging.getLogger('nose').setLevel(logging.CRITICAL)
logging.getLogger('s3transfer').setLevel(logging.CRITICAL)
logging.getLogger('urllib3').setLevel(logging.CRITICAL)


session = boto3.session.Session(aws_access_key_id=S3_KEY,
                                aws_secret_access_key=S3_SECRET,
                                region_name='region_name')


# def make_bucket(name, acl):
#     session = aws_session()
#     s3_resource = session.resource('s3')
#     return s3_resource.create_bucket(Bucket=name, ACL=acl)


def upload_file_to_bucket(bucket_name, file_path):
    # session = aws_session()
    s3_resource = session.resource('s3')
    file_dir, file_name = os.path.split(file_path)

    bucket = s3_resource.Bucket(bucket_name)
    bucket.upload_file(
      Filename=file_path,
      Key=file_path,
    #   ExtraArgs={'ACL': 'public-read'}
    )
    os.remove(file_path)
    s3_url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
    # os.remove(file_path)
    return s3_url

def upload_file_to_bucket_origninal(bucket_name, file_path):
    # session = aws_session()
    s3_resource = session.resource('s3')
    file_dir, file_name = os.path.split(file_path)

    bucket = s3_resource.Bucket(bucket_name)
    bucket.upload_file(
      Filename=file_path,
      Key=file_path,
    #   ExtraArgs={'ACL': 'public-read'}
    )
    os.remove(file_path)
    s3_url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
    # os.remove(file_path)
    return s3_url


#upload_file_to_bucket('', '/home/Desktop/iamges/xyz.jpeg')