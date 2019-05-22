org 0x7c00
call load

mov ah,0
mov al,0x13
int 0x10
jmp 0:0x8000

ret

load:
	mov ah,2
	mov al,3
	mov bx,0x8000
	mov ch,0
	mov cl,2
	mov dh,0
	mov dl,0x80
	int 0x13
ret