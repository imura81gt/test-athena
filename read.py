import ConfigParser
import os
import yaml
import boto3

s3 = boto3.client('s3')

bucketname = 'test-athena-parquet'

os.path.expanduser('~')
config = ConfigParser.ConfigParser()
config.read(os.path.expanduser('~/.aws/credentials'))

aws_access_key_id = config.get('default', 'aws_access_key_id')
aws_secret_access_key = config.get('default', 'aws_secret_access_key')

dic = {
    'out': {
        'type': 'parquet',
        'path_prefix': 's3a://' + bucketname + '/titanic/',
        'extra_configurations': {
            'fs.s3a.access.key': aws_access_key_id,
            'fs.s3a.secret.key': aws_secret_access_key
        }
    }
}

with open('_outs3.yml.liquid', 'w') as f:
    yaml.dump(dic, f, default_flow_style=False)
