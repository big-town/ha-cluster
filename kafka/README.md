###Полезные команды
#Создать тему
/home/kafka/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 2 --partitions 3 --topic events
#Удалить тему
/home/kafka/kafka/bin/kafka-topics.sh --delete --zookeeper localhost:2181 --topic events

#Диагностика
/home/kafka/kafka/bin/zookeeper-shell.sh 127.0.0.1:2181 ls /brokers/ids
/home/kafka/kafka/bin/zookeeper-shell.sh 127.0.0.1:2181 get /brokers/ids/1
/home/kafka/kafka/bin/zookeeper-shell.sh 127.0.0.1:2181 ls /brokers/topics
/home/kafka/kafka/bin/kafka-topics.sh --describe --bootstrap-server localhost:9092
/home/kafka/kafka/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --all-groups --describe
/home/kafka/kafka/bin/kafka-configs.sh --bootstrap-server localhost:9092 --entity-type topics --entity-name events --describe --all

#Принять сообщение
/home/kafka/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic events --from-beginning

#Отправить сообщение
echo "Hello, World" | /home/kafka/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic events > /dev/null


#Очистить все записи во всех партициях
/home/kafka/kafka/bin/kafka-delete-records.sh --bootstrap-server localhost:9092 --offset-json-file delete.json
#delete.json
{"partitions": [ 
    { "topic": "events", "partition": 0, "offset": -1 },
    { "topic": "events", "partition": 1, "offset": -1 },
    { "topic": "events", "partition": 2, "offset": -1 } ], "version": 1 }