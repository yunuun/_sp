        .global mul3

        .text
mul3:
        mov %rdi, %rax      
        imulq %rsi, %rax    /* %rax = %rax * %rsi */
        imulq %rdx, %rax    /* %rax = %rax * %rdx */
        ret