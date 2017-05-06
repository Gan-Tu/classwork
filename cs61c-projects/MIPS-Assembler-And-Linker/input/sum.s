sum:  addiu $sp $sp -8
      sw $a0 0($sp)
      sw $ra 4($sp)
      li $v0 0
      beq $a0 $0 exit
      addiu $a0 $a0 -1
      jal sum
      lw $a0 0($sp)
      addu $v0 $v0 $a0
exit: lw $ra 4($sp)
      addiu $sp $sp 8
      jr $ra
