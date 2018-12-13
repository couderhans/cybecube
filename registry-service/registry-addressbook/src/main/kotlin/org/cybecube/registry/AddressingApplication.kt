package org.cybecube.registry

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import org.springframework.jms.annotation.EnableJms
import org.springframework.transaction.annotation.EnableTransactionManagement
import org.springframework.web.servlet.config.annotation.EnableWebMvc

@EnableJms
@EnableWebMvc
@EnableTransactionManagement
@SpringBootApplication
class RegistryAddressbookApplication

fun main(args: Array<String>) {
    runApplication<RegistryAddressbookApplication>(*args)
}
