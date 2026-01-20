import boto3

ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
    ImageId='ami-0c55b159cbfafe1f0',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro'
)

print("Created instance:", instances[0].id)
