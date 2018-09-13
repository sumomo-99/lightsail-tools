import boto3
import datetime
import requests
import argparse

parser = argparse.ArgumentParser(
            description='This script send message to ChatWork which Lightsail instances name and snapshots.'
            )
parser.add_argument('room_id',
                    help='ChatWork Room ID',
                    metavar='room_id')
parser.add_argument('token',
                    help='ChatWork API Token',
                    metavar='token')
args = parser.parse_args()

# ChatWork API Endpoint
URL = 'https://api.chatwork.com/v2/rooms/' + args.room_id + '/messages'

# ChatWork API Token
CHATWORK_TOKEN = args.token

client = boto3.client('lightsail')


"""Return Lightsail instances name and snapshots.
The return message is formatted for ChatWork.
"""
def get_instance_information():

    instances = client.get_instances()
    snapshots = client.get_instance_snapshots()

    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %Z')
    message = 'AWS Lightsail稼動状況\n' + now + '\n'

    for instance in instances['instances']:
        instance_name = instance['name']
        message += '[info][title]' + instance_name + '[/title]'\
                 + '# State\n' + instance['state']['name'] + '\n\n'\
                 + '# Snapshots'

        for snapshot in filter(lambda x: x['fromInstanceName'] == instance_name,
                               snapshots['instanceSnapshots']):
            message += '\n* File Name: ' + snapshot['name'] + '    '\
                     + 'CreateAt: '\
                     + snapshot['createdAt'].strftime('%Y-%m-%d %H:%M:%S %Z')

        message += '[/info]'

        return message


"""Send message to ChatWork.
"""
def send_chatwork(body):
    response = requests.post(URL,
                             data={'body': body},
                             headers={'X-ChatWorkToken': CHATWORK_TOKEN})


if __name__ == '__main__':
    send_chatwork(get_instance_information())
