import boto3
region = 'us-east-1'
instances = ['i-0ba5d1130d303ed38', 'i-05c85075d353710aa']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print("Stopped your instances: " + str(instances))