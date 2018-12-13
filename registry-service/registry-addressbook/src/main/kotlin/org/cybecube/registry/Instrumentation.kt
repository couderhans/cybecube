package org.cybecube.registry

import org.springframework.jmx.export.annotation.ManagedOperation
import org.springframework.jmx.export.annotation.ManagedOperationParameter
import org.springframework.jmx.export.annotation.ManagedOperationParameters
import org.springframework.jmx.export.annotation.ManagedResource
import org.springframework.stereotype.Component
import javax.annotation.Resource
import javax.management.MBeanServer
import kotlin.reflect.KProperty0
import kotlin.reflect.full.staticProperties

@Component
@ManagedResource(objectName = "AddressingInstrumentation.OBJECT_NAME")
class AddressingInstrumentation(private val repository: AcademyRepository) {

    private val platformMBeanServer: MBeanServer? = null

    @Resource
    private val lookupService: RestController? = null

    @ManagedOperation(description = "Look up the attributes of an MP")
    @ManagedOperationParameters(ManagedOperationParameter(name = "dn", description = "distinguished name of the MP to look up"))
    @Throws(Exception::class)
    fun lookup(dn: String): MutableList<KProperty0<*>> {
        val academy =  repository.findAllByOrderByDidDesc()
        return academy!!::class.staticProperties.toMutableList()
    }

}
