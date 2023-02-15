# Criado em 15/02/2023 - 19:00
# @author: Mike Fortes

# Importando a classe ZabbixAPI da biblioteca zabbix_api
from zabbix_api import ZabbixAPI

# Fazer conexão com a API
zapi = ZabbixAPI(server="http://192.168.10.103/zabbix")

# Fazendo logon
zapi.login("api_user","zabbix")

# Imprimir versão da API
print("Versão da API do Zabbix: ", zapi.api_version())

