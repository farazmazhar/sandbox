package com.farazmazhar.kafka.tutorial;

import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.kafka.common.serialization.StringSerializer;

public class test {
    public static void main(String[] args) {
        System.out.println(StringSerializer.class.getName());
        System.out.println(StringDeserializer.class.getName());
    }
}
