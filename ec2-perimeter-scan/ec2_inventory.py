from collections import defaultdict
import boto3

def get_all_pub_ips():
    # Get information for all running instances
    ec2 = boto3.resource('ec2')
    all_regions = client.describe_regions()['Regions']
    ips_and_names_mapping = {}

    # Iterate all regions to get a complete view of all possible EC2s running in the account
    for region in all_regions:
        if DEBUG_MODE:
            print(f'Currently sweeping over region {region}')

        ec2 = boto3.resource('ec2', region_name=region)
        running_instances = ec2.instances.filter(Filters=[{
            'Name': 'instance-state-name',
            'Values': ['running']}])

        # Initialize name to an empty string - will be needed in later conditional logic
        name = ''
        ec2info = defaultdict()

        for instance in running_instances:
            # Handle case for when an EC2 does not have a name
            if instance.tags == None:
                name = "Server is not named/labeled"
            else:
                for tag in instance.tags:
                    if 'Name'in tag['Key']:
                        name = tag['Value']

            if instance.public_ip_address == None:
                if DEBUG_MODE:
                    print(f'No public ip found for instance {instance.id}...skipping')
                continue
            ips_and_names_mapping[name] = instance.public_ip_address

    return ips_and_names_mapping