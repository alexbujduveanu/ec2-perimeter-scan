import requests
import json

# Where to modify webhook settings: https://my.slack.com/services/new/incoming-webhook/
def post_to_slack(results_map, webhook_url):
    msg = 'The purpose of this automation is to continuously scan our AWS public IP space for unwanted port exposures. Runs on a cron schedule.\n\n```'
    
    for name in results_map.keys():
        appended = f'Host Label: {name}\nPublic IP:{results_map[name][0]}\nOpen Port: {results_map[name][1]}\n\n'
        msg += appended

    # Close the block of formatted text after for loop is over
    msg += '```'

    # Post message to channel associated with webhook URL
    slack_data = {'text': msg}
    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )

    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )