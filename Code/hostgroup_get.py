# Criado em 15/02/2023 - 19:00
# @author: Mike Fortes

# Importando a classe ZabbixAPI da biblioteca zabbix_api
from pyzabbix  import ZabbixAPI

# Fazer conexão com a API
zapi = ZabbixAPI(server="http://192.168.15.13/zabbix")

# Fazendo logon
zapi.login("api_user","zabbix")

# Get a list of all issues (AKA tripped triggers)
triggers = zapi.trigger.get(
    only_true=1,
    skipDependent=1,
    monitored=1,
    active=1,
    output="extend",
    expandDescription=1,
    selectHosts=["host"],
)

# Do another query to find out which issues are Unacknowledged
unack_triggers = zapi.trigger.get(
    only_true=1,
    skipDependent=1,
    monitored=1,
    active=1,
    output="extend",
    expandDescription=1,
    selectHosts=["host"],
    withLastEventUnacknowledged=1,
)
unack_trigger_ids = [t["triggerid"] for t in unack_triggers]
for t in triggers:
    t["unacknowledged"] = True if t["triggerid"] in unack_trigger_ids else False

# Print a list containing only "tripped" triggers
for t in triggers:
    if int(t["value"]) == 1:
        print(
            "{} - {} {}".format(
                t["hosts"][0]["host"],
                t["description"],
                "(Unack)" if t["unacknowledged"] else "",
            )
        )