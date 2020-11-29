package com.farazmazhar.kafka.tutorial;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.StringSerializer;

import java.util.Properties;

public class ProducerDemo {
    public static void main(String[] args) {

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
        producer.send(record1);
        producer.send(record2);
        producer.send(record3);

        // Execute
        producer.flush();
        producer.close();
    }
}
