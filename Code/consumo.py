from zabbix_api import ZabbixAPI
zapi = ZabbixAPI(server="http://192.168.15.5/zabbix")
zapi.login("Admin","zabbix")
print ("Versão da API do Zabbix: ", zapi.api_version())