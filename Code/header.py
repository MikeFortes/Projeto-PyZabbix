# Criado em 15/02/2023 - 19:00
# @author: Mike Fortes

# Importando a classe ZabbixAPI da biblioteca zabbix_api
from pyzabbix  import ZabbixAPI

# Fazer conexão com a API
zapi = ZabbixAPI(server="http://192.168.15.13/zabbix")

# Fazendo logon
zapi.login("api_user","zabbix")

# Imprimir versão da API
print("Versão da API do Zabbix: ", zapi.api_version())

