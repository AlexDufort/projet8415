import logging
import random
from flask import Blueprint, request
from typing import Dict, List
import pymysql
import pymysql.cursors
#import requests
#import utils
from sshtunnel import open_tunnel



def load_private_key(name: str) -> paramiko.RSAKey:
    '''
    Loads a private key from a local keypair file.
        Parameters:
            name (str): The keypair name
        
        Returns:
            key (RSAKey): The private key
    '''

    if not os.path.isfile(f'../ssh_key.pem'):
        return None
    keypair = None
    with open(f'../ssh_key.pem') as file:
        keypair = json.load(file)
    return paramiko.RSAKey.from_private_key(file)

PRIVATE_KEY = load_private_key()

@proxy_bp.route("/direct", methods=["POST"])
def direct_proxy():
    '''
    The /direct route implementation.
    This will perform the query request on the master node.
    pymysql -> master (sshtunnel) -> master mysqld
    '''

    data = request.get_json()
    query: str = data['query']
    try:
        output, rowcount, dbname = make_query(query, 'direct')
    except Exception as e:
        return str(e), 500
    return {
        'output': output,
        'rowcount': rowcount,
        'node': dbname
    }, 200