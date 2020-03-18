#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os

import requests
from project import settings


class LineApi:

    def __init__(self):
        self.json_root_path = settings.LINE_JSON_DIR
        self.client_id = settings.CLIENT_ID
        self.client_secret = settings.CLIENT_SECRET
    
    def json_read(self, file_name):
        # jsonファイルパス生成
        json_path = os.path.join(self.json_root_path, file_name)
        # json読み込み        
        with open(json_path) as f:
            json_data = json.load(f)
        
        return json_data

    def execute_request(self, endpoint, header, body, method="GET"):
        #json_body = json.dumps(body)
        if method == "GET":
            pass
        elif method == "POST":
            response = requests.post(url=endpoint, headers=header, data=body)

        #return json.load(response.text)
        return response
    
    def execute_auth(self):
        # auth 情報
        json_name = "auth.json"
        endpoint = "https://api.line.me/v2/oauth/accessToken"
        method = "POST"

        # リクエスト用ヘッダー、ボディ作成 
        json_data = self.json_read(file_name=json_name)
        header = json_data['header'][0]
        body =json_data['body'][0]
        body['client_id'] = self.client_id
        body['client_secret'] = self.client_secret
        
        # API実行
        response = self.execute_request(endpoint=endpoint, header=header, body=body, method=method)
        content = json.loads(response.content)
        # レスポンスの中身を返却
        return content
