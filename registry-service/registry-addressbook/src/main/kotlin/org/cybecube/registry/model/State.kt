/**
* CybeCube Gate
* This is the api for the cybecube gate.  The cybecube gate is an way to access programmatically cybecube's virtual assistents.
*
* OpenAPI spec version: 1.0.0
* Contact: info@cybecube.org
*
* NOTE: This class is auto generated by the swagger code generator program.
* https://github.com/swagger-api/swagger-codegen.git
* Do not edit the class manually.
*/
package com.cybecube.academy.registry.model

import javax.persistence.Entity
import javax.persistence.Table


/**
 * 
 * @param id 
 * @param state 
 */
@Entity
@Table(name = "state")
data class State (
    val id: Long? = null,
    val state: State? = null
) {
    /**
    * 
    * Values: available,learning,working,alive,stopped
    */
    enum class State(val value: kotlin.Any){
        available("available"),
        learning("learning"),
        working("working"),
        alive("alive"),
        stopped("stopped");
    }
}

