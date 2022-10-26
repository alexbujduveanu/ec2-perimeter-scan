from slack import *
from perimeter_scan import *
from ec2_inventory import *
import boto3

# Flag to toggle additional print statements when needed for troubleshooting
# Longer term should also be moved to a separate conf file
DEBUG_MODE = False

def main():
    ip_to_name_map = get_all_pub_ips()
    ret = nmap_scan(ip_to_name_map)

    if DEBUG_MODE:
        print(f'IPs to names map is {ip_to_name_map}\n')
        print(f'Message to post to slack is {ret}')

    post_to_slack(ret)

if __name__ == '__main__':
    main()

                
