from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    location='media'
    file_overwrite = False
    default_acl = 'private'


#create CORS and policy or serve media file from s3
