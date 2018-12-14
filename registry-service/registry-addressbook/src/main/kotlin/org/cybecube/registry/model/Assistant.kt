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

import javax.persistence.*

/**
 * 
 * @param id 
 * @param title 
 * @param name 
 * @param state 
 * @param location 
 * @param date_of_birth 
 * @param gender 
 * @param &#x60;class&#x60; 
 * @param alive 
 */
@Entity
@Table(name = "assistant")
data class Assistant (
        @Id @GeneratedValue(strategy= GenerationType.AUTO)
        val id: Long? = null,

        @Basic(optional = false) @Column(name = "title", nullable = false, length = 10)
        val title: String? = null,

        @Basic(optional = false) @Column(name = "name", nullable = false, length = 30)
        val name: String? = null,

        @JoinColumn(name = "state", nullable = false, updatable = true)
        @ManyToOne(optional = false, fetch = FetchType.EAGER)
        val state: State? = null,

        @JoinColumn(name = "location", nullable = false, updatable = false)
        @ManyToOne(optional = false, fetch = FetchType.EAGER)
        val location: Location? = null,

        @Basic(optional = false) @Column(name = "date_of_birth", nullable = false, length = 12)
        val date_of_birth: String? = null,

        @Basic(optional = false) @Column(name = "gender", nullable = false, length = 1)
        val gender: String? = null,

        @Basic(optional = false) @Column(name = "class", nullable = false, length = 7)
        val `class`: String? = null,

        @Basic(optional = false) @Column(name = "alive", nullable = false)
        val alive: Boolean? = null
) {

}

