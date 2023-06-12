from time import sleep
from prefect_aws import S3Bucket, AwsCredentials


def create_aws_creds_block():
    my_aws_creds_obj = AwsCredentials(
        aws_access_key_id="AKIAZJWGWT7ZENTY4QWV", aws_secret_access_key="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"
    )
    my_aws_creds_obj.save(name="my-aws-creds", overwrite=True)


def create_s3_bucket_block():
    aws_creds = AwsCredentials.load("my-aws-creds")
    my_s3_bucket_obj = S3Bucket(
        bucket_name="https://mlops-zcamp.s3.amazonaws.com/data/", credentials=aws_creds # s3://mlops-zcamp/data/
    )
    my_s3_bucket_obj.save(name="s3-bucket-example", overwrite=True)


if __name__ == "__main__":
    create_aws_creds_block()
    sleep(5)
    create_s3_bucket_block()
