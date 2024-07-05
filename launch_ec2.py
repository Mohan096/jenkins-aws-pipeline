import boto3

def launch_ec2_instance():
    ec2 = boto3.resource('ec2')

    # Create a new EC2 instance
    instances = ec2.create_instances(
        ImageId='ami-01376101673c89611',  # Amazon Linux 2 AMI
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='your-key-pair-name'
    )

    print(f'Launched EC2 Instance: {instances[0].id}')

if __name__ == "__main__":
    launch_ec2_instance()
