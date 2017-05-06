neg_array: li $t0 0
loop:      beq $t0 $a1 exit
	   sll $t1 $t0 2
	   addu $t2 $a0 $t1
	   lw $t3 0($t2)
	   neg $t3 $t3
	   sw $t3 0($t2)
	   addiu $t0 $t0 1
	   j loop
exit:      jr $ra
