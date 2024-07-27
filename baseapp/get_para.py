
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError




def get_parameter(name):
    ssm = boto3.client('ssm', region_name='ap-south-1')  # Replace 'your-region' with your actual AWS region
    try:
        response = ssm.get_parameter(Name=name, WithDecryption=True)
        return response['Parameter']['Value']
    except (NoCredentialsError, PartialCredentialsError):
        # Handle the case where AWS credentials are not available
        raise RuntimeError("AWS credentials not found.")
    except ssm.exceptions.ParameterNotFound:
        # Handle the case where the parameter is not found
        raise RuntimeError(f"Parameter {name} not found.")

