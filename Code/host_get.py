# Criado em 15/02/2023 - 19:30
# @author: Mike Fortes

from zabbix_api import ZabbixAPI

# Cabeçalho de conexão
zapi = ZabbixAPI(server="http://192.168.10.103/zabbix")
zapi.login("api_user","zabbix")


hosts = zapi.host.get({"output":["hostid","host"]})
print(hosts)