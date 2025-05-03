import os

S3_BUCKET                 = 'bucket_name'
S3_KEY                    = 'key'
S3_SECRET                 = 'secret_key'
S3_LOCATION               = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)

SECRET_KEY                = os.urandom(32)
DEBUG                     = True
PORT                      = 5000
