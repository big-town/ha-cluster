#Проверка кластера rabbit
rabbitmqctl cluster_status

#Вывод команды
rabbitmqctl cluster_status
Cluster status of node rabbit@pp_services_1 ...
Basics

Cluster name: rabbit@uzdev

Disk Nodes

rabbit@pp_services_1
rabbit@pp_services_2
rabbit@pp_services_3

Running Nodes

rabbit@pp_services_1
rabbit@pp_services_2
rabbit@pp_services_3

Versions

rabbit@pp_services_1: RabbitMQ 3.8.14 on Erlang 23.3.1
rabbit@pp_services_2: RabbitMQ 3.8.14 on Erlang 23.3.1
rabbit@pp_services_3: RabbitMQ 3.8.14 on Erlang 23.3.1

Maintenance status

Node: rabbit@pp_services_1, status: not under maintenance
Node: rabbit@pp_services_2, status: not under maintenance
Node: rabbit@pp_services_3, status: not under maintenance

Alarms

(none)

Network Partitions

(none)

Listeners

Node: rabbit@pp_services_1, interface: [::], port: 25672, protocol: clustering, purpose: inter-node and CLI tool communication
Node: rabbit@pp_services_1, interface: [::], port: 15672, protocol: http, purpose: HTTP API
Node: rabbit@pp_services_1, interface: [::], port: 5672, protocol: amqp, purpose: AMQP 0-9-1 and AMQP 1.0
Node: rabbit@pp_services_2, interface: [::], port: 25672, protocol: clustering, purpose: inter-node and CLI tool communication
Node: rabbit@pp_services_2, interface: [::], port: 15672, protocol: http, purpose: HTTP API
Node: rabbit@pp_services_2, interface: [::], port: 5672, protocol: amqp, purpose: AMQP 0-9-1 and AMQP 1.0
Node: rabbit@pp_services_3, interface: [::], port: 25672, protocol: clustering, purpose: inter-node and CLI tool communication
Node: rabbit@pp_services_3, interface: [::], port: 15672, protocol: http, purpose: HTTP API
Node: rabbit@pp_services_3, interface: [::], port: 5672, protocol: amqp, purpose: AMQP 0-9-1 and AMQP 1.0

Feature flags

Flag: drop_unroutable_metric, state: disabled
Flag: empty_basic_get_metric, state: disabled
Flag: implicit_default_bindings, state: enabled
Flag: maintenance_mode_status, state: enabled
Flag: quorum_queue, state: enabled
Flag: user_limits, state: enabled
Flag: virtual_host_metadata, state: enabled
