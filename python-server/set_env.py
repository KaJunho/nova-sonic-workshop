import boto3

session = boto3.Session(region_name="us-east-1")

credentials = session.get_credentials().get_frozen_credentials()
ak = credentials.access_key
sk = credentials.secret_key
st = credentials.token
print(f"export AWS_ACCESS_KEY_ID={ak}")
print(f"export AWS_SECRET_ACCESS_KEY={sk}")
print(f"export AWS_SESSION_TOKEN={st}")
print(f"export AWS_DEFAULT_REGION=us-east-1")