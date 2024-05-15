import requests
from fastapi.exceptions import HTTPException
from ..envs import ENV
from .client import Client
def create_client(client: Client):
    json_content = client.__dict__
    if get_client_by_cpf_cnpj(client.cpfCnpj)["totalCount"] != 0:
        raise HTTPException(409)
    headers_content = {
        "access_token": ENV["APIKEY"],
    }
    response = requests.post(
        f"{ENV["URL"]}/customers",
        json=json_content,
        headers=headers_content,
    )
    
    return response.json()

def get_client_by_cpf_cnpj(cpf_cnpj):
    headers_content = {
        "access_token": ENV["APIKEY"],
    }
    response = requests.get(
        f"{ENV['URL']}/customers?cpfCnpj={cpf_cnpj}",
        headers=headers_content,
    )
    return response.json()