package org.cybecube.registry

import com.cybecube.academy.registry.Academy
import org.springframework.data.repository.CrudRepository

interface AcademyRepository : CrudRepository<Academy, Long> {
    fun findAllByOrderByDidDesc() : Iterable<Academy>
}

