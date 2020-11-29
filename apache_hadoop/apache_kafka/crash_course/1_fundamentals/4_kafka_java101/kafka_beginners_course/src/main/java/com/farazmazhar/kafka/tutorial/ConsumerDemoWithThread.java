package com.farazmazhar.kafka.tutorial;

import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.errors.WakeupException;
import org.apache.kafka.common.protocol.types.Field;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.time.Duration;
import java.util.Collections;
import java.util.Properties;
import java.util.concurrent.CountDownLatch;

public class ConsumerDemoWithThread {
    public static void main(String[] args) {
        new ConsumerDemoWithThread().run();
    }

    private ConsumerDemoWithThread() {

    }

    public void run() {
        CountDownLatch latch = new CountDownLatch(1);

        Runnable myConsumerThread = new ConsumerThread(
                "127.0.0.1:9092",
                "very_cool_group",
                "FirstTopic",
                latch
        );

        Thread myThread = new Thread(myConsumerThread);
        myThread.start();

        Runtime.getRuntime().addShutdownHook(new Thread( () -> {
            // Caught shutdown hook.
            ((ConsumerThread) myConsumerThread).shutdown();
            try {
                latch.await();
            } catch (InterruptedException e) {
                e.printStackTrace();
            } // Application has exited.
        }));


    }

    public class ConsumerThread implements Runnable {

        // Logger.
        private Logger logger = LoggerFactory.getLogger(ConsumerDemoWithThread.class.getName());
        private KafkaConsumer<String, String> consumer;
        private CountDownLatch latch;

        public ConsumerThread(String bootstrapServers,
                              String groupId,
                              String topic,
                              CountDownLatch latch) {

            this.latch = latch;

            Properties properties = new Properties();
            properties.setProperty(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
            properties.setProperty(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName()); // Consumer is De
            properties.setProperty(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
            properties.setProperty(ConsumerConfig.GROUP_ID_CONFIG, groupId);
            properties.setProperty(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest"); // earliest / latest

            consumer = new KafkaConsumer<>(properties);
            consumer.subscribe(Collections.singleton(topic));

        }

        @Override
        public void run() {

            // Poll for new data.
            try {
                while(true) {
                    ConsumerRecords<String, String> records =
                            consumer.poll(Duration.ofMillis(100));

                    for (ConsumerRecord<String, String> record: records) {
                        logger.info("Key: " + record.key());
                        logger.info("Value: " + record.value());
                        logger.info("Offset: " + record.offset());
                        logger.info("Partition: " + record.partition());
                    }
                }
            } catch (WakeupException e) {
                logger.info("Received shutdown signal.");
            } finally {
                // Closing the consumer.
                consumer.close();

                // Tell the main code that we're done with consumer.
                latch.countDown();
            }
        }

        public void shutdown() {
            // The wakeup() method is special method to interrup consumer.poll().
            // It will throw the exception WakeUpException.
            consumer.wakeup();
        }
    }
}
