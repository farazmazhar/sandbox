package com.farazmazhar.kafka.tutorial;

import org.apache.kafka.clients.producer.*;
import org.apache.kafka.common.serialization.StringSerializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Properties;

public class ProducerDemoWithCallback {
    public static void main(String[] args) {

        final Logger logger = LoggerFactory.getLogger(ProducerDemoWithCallback.class);

        // Create Producer properties.
        Properties properties = new Properties();
        properties.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "127.0.0.1:9092");
        // Tells Producer how to 'serialize' the data.
        properties.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        properties.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());

        // Create the Producer.
        // kaProducer<Key,    Value>
        KafkaProducer<String, String> producer = new KafkaProducer<String, String>(properties);

        // Create a producer.
        ProducerRecord<String, String> record1 =
                new ProducerRecord<String, String>("FirstTopic", "hello world");
        ProducerRecord<String, String> record2 =
                new ProducerRecord<String, String>("FirstTopic", "This message is from Java");
        ProducerRecord<String, String> record3 =
                new ProducerRecord<String, String>("FirstTopic", "break_the_loop");

        // Send data.
        producer.send(record1, new Callback() {
            public void onCompletion(RecordMetadata recordMetadata, Exception e) {
                // Executes every time a record is successfully sent or an exception is thrown.
                if (e == null) {
                    logger.info("Received metadata. \n" +
                            "Topic: " + recordMetadata.topic() + "\n" +
                            "Partition: " + recordMetadata.partition() + "\n" +
                            "Offset: " + recordMetadata.offset() + "\n" +
                            "Timestamp: " + recordMetadata.timestamp() + "\n");
                } else {
                    logger.error("Error while producing", e);
                }
            }
        });
        producer.send(record2, new Callback() {
            public void onCompletion(RecordMetadata recordMetadata, Exception e) {
                // Executes every time a record is successfully sent or an exception is thrown.
                if (e == null) {
                    logger.info("Received metadata. \n" +
                            "Topic: " + recordMetadata.topic() + "\n" +
                            "Partition: " + recordMetadata.partition() + "\n" +
                            "Offset: " + recordMetadata.offset() + "\n" +
                            "Timestamp: " + recordMetadata.timestamp() + "\n");
                } else {
                    logger.error("Error while producing", e);
                }
            }
        });
        producer.send(record3, new Callback() {
            public void onCompletion(RecordMetadata recordMetadata, Exception e) {
                // Executes every time a record is successfully sent or an exception is thrown.
                if (e == null) {
                    logger.info("Received metadata. \n" +
                            "Topic: " + recordMetadata.topic() + "\n" +
                            "Partition: " + recordMetadata.partition() + "\n" +
                            "Offset: " + recordMetadata.offset() + "\n" +
                            "Timestamp: " + recordMetadata.timestamp() + "\n");
                } else {
                    logger.error("Error while producing", e);
                }
            }
        });

        // Execute
        producer.flush();
        producer.close();
    }
}
