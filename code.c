asm(".code16gcc\n");

void print(char,char,int,int);

void putPixel(int, int, char);

void FillScreen(int);

int start(){
	
	int i;
	for (i = 0; i < 80; i++)
		
		putPixel(i, i, 4);
	
	FillScreen(1);
}

void print(char c, char color, int x, int y){
	
	char *p = (char*)0xB8000;
	p += ((y*80)+x)*2;
	*p = c;
	p++;
	*p = color;
}

void putPixel(int x, int y, char color){
	
	char *p=(char*)0xA0000;
	p += (y * 320) + x;
	*p = color;
	
}

void FillScreen(int color){  //320 на 200
	
	int x, y;
	for (x = 0; x < 320; x++){
		for( y = 0; y < 200; y++){
			putPixel(x,y,color);
		}
	}
}

