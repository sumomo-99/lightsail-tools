# lightsail-tools
---
**AWS Lightsail**のインスタンスステータスとスナップショットの情報を取得します。
取得した情報は**ChatWork**にメッセージ送信します。

## Demo
```
$ python3 get_instances.py 12345678 abcdefghijklmnopqrstuvwxyz123456
```
ChatWorkにLightsailインスタンスごとのステータスおよびスナップショット名が、メッ>セージ送信されます。
![lightsail-chatwork](https://github.com/sumomo-99/lightsail-tools/blob/images/lightsail-chatwork.PNG)

## Usage
**python3** **get_instances.py** *room_id* *token*

    *room_id*: ChatWorkの送信先Room ID
    *token*: ChatWork APIトークン

## Install
AWS SDK for Pythonとrequestsライブラリが必要です。
```
$ pip install boto3
$ pip install requests
```
