.686
.MODEL FLAT, STDCALL
.STACK 4096
.DATA
.CODE
PUBLIC convert, DllMain

; Точка входа для DLL
DllMain PROC hinstDLL:DWORD, fdwReason:DWORD, lpvReserved:DWORD
    mov eax, 1         ; Возвращаем TRUE (успешная загрузка)
    ret
DllMain ENDP

convert PROC num:DWORD, radix:DWORD, buf:DWORD
    push edi
    mov edi, buf
    cmp radix, 2
    jl bad
    cmp radix, 36
    jg bad
    mov eax, num
    xor ecx, ecx
    test eax, eax
    jns @@m1a
    neg eax
@@m1a:
    xor edx, edx
    div radix
    push edx
    inc ecx
    test eax, eax
    jnz @@m1a
    cmp num, 0
    jnl @@m2a
    push -3
    inc ecx
@@m2a:
    pop eax
    add al, '0'
    cmp al, '9'
    jbe @@m2
    add al, 7
@@m2:
    stosb
    loop @@m2a
    mov al, 0
    stosb
    mov eax, 1
ex:
    pop edi
    ret
bad:
    mov eax, 0
    jmp ex
convert ENDP

END
