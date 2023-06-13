from time import sleep
from prefect_aws import S3Bucket, AwsCredentials


def create_aws_creds_block():
    my_aws_creds_obj = AwsCredentials(
        aws_access_key_id="AKIAZJWGWT7ZHJLYDJMV", aws_secret_access_key="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"
    )
    my_aws_creds_obj.save(name="my-aws-creds", overwrite=True)


def create_s3_bucket_block():
    aws_creds = AwsCredentials.load("my-aws-creds")
    my_s3_bucket_obj = S3Bucket(
        bucket_name="test_bucket", credentials=aws_creds # s3://mlops-zcamp/data/
    )
    my_s3_bucket_obj.save(name="s3-bucket-test", overwrite=True)


if __name__ == "__main__":
    create_aws_creds_block()
    sleep(5)
    create_s3_bucket_block()


# AKIAZJWGWT7ZENTY4QWV
# CgO5qoV6FNcnnV95MYKVAvPCgIEwVk51SG4RbeZr