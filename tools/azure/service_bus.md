# Azure Service Bus
Microsoft Azure Service Bus is a fully managed enterprise message broker with message queues and publish-subscribe topics. Service Bus is used to decouple applications and services from each other, providing the following benefits:

- Load-balancing work across competing workers
- Safely routing and transferring data and control across service and application boundaries
- Coordinating transactional work that requires a high-degree of reliability

# Specific Problems

## Python service bus messaging works in 1 machine but not another

Solution:
- explicitly specify enum 'amqp' in the python service bus definition.
- The exact code excerpt is given below

Detailed test cases are summarized below:

Summarizing the problem:
| Azure Servicebus version |  Machine |  Message Success |  Comments |
|---|---|---|---|
| 0.51.0 | Developer-1 | y |---|
| 0.51.0 | Server-Stage | y |---|
| 0.51.0 | Server-Production | y |---|
| 7.3.2 | Developer-1 | y |---|
| 7.3.2 | Server-Stage | n | ports? |

Testing the ports:
Powershell port 5671 ping test for AMQP Transport type:

tnc <yournamespacename>.servicebus.windows.net -port 5671
tnc server_name.servicebus.windows.net  -port 5671

|  Machine |  Transport Type |  Port |  pingtest |  Message Success |  Comments |
|---|---|---|---|---|---|
| Developer-1 | AmqpWebsocket | 443 | Pass | y | - |
| Server-Stage | AmqpWebsocket | 443 | Pass | n | Unable to open authentication session on connection. Please confirm target hostname exists: b'<yournamespacename>.servicebus.windows.net' |
| Developer-1 | Amqp | 5671 | Pass | ? | not applicable |
| Server-Stage | Amqp | 5671 | Fail | ? | not applicable |


# References


[https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview)

[https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-troubleshooting-guide](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-troubleshooting-guide)

[https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-amqp-overview](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-amqp-overview)

[https://azuresdkdocs.blob.core.windows.net/$web/python/azure-servicebus/latest/azure.servicebus.html#azure.servicebus.ServiceBusClient](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-servicebus/latest/azure.servicebus.html#azure.servicebus.ServiceBusClient)

[https://pypi.org/project/azure-servicebus/](https://pypi.org/project/azure-servicebus/)
