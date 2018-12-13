package org.cybecube.registry

import org.springframework.web.bind.annotation.*
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RestController

@RestController
@RequestMapping("/registry")
class RestController(private val repository: AcademyRepository) {

    @GetMapping("/addressbook")
    fun findAll() = repository.findAllByOrderByDidDesc()

}