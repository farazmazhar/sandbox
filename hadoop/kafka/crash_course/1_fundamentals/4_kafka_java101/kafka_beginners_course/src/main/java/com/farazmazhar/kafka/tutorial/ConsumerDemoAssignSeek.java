package com.farazmazhar.kafka.tutorial;

import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.TopicPartition;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.time.Duration;
import java.util.Collections;
import java.util.Properties;

public class ConsumerDemoAssignSeek {
    public static void main(String[] args) {
        // Logger.
        Logger logger = LoggerFactory.getLogger(ConsumerDemoAssignSeek.class.getName());

        // Consumer properties.
        Properties properties = new Properties();
        properties.setProperty(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "127.0.0.1:9092");
        properties.setProperty(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName()); // Consumer is De
        properties.setProperty(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        properties.setProperty(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest"); // earliest / latest

        // Create a consumer.
        KafkaConsumer<String, String> consumer = new KafkaConsumer<String, String>(properties);

        // Assign and Seek are mostly used to replay data or fetch a specific message.

        // Assign
        TopicPartition partitionToReadFrom = new TopicPartition("FirstTopic", 0);
        long offsetToReadFrom = 15L;
        consumer.assign(Collections.singleton(partitionToReadFrom));

        // Seek
        consumer.seek(partitionToReadFrom, offsetToReadFrom);

        int messagesToRead = 5;
        boolean keepOnReading = true;
        int numberOfMessagesReadSoFar = 0;

        // Poll for new data.
        while(true) {
            ConsumerRecords<String, String> records =
                    consumer.poll(Duration.ofMillis(100));

            for (ConsumerRecord<String, String> record: records) {
                numberOfMessagesReadSoFar += 1;

                logger.info("Key: " + record.key());
                logger.info("Value: " + record.value());
                logger.info("Offset: " + record.offset());
                logger.info("Partition: " + record.partition());

                if (numberOfMessagesReadSoFar >= messagesToRead) {
                    keepOnReading = false;
                    break;
                }
            }
        }
    }
}
