// Inicijalizacija vrijednosti R0 i R1
@7
D=A;
@R0
M=D;

@3
D=A;
@R1
M=D;

// Provjera i zamjena vrijednosti R0 i R1 ako je R0 > R1
@R0
D=M;
@R1
D=M-D;

@skip
D;JGE // Ako je R0 <= R1, preskoči zamjenu

// Zamjena vrijednosti R0 i R1
@R0
D=M;
@tmp
M=D;

@R1
D=M;
@R0
M=D;

@tmp
D=M;
@R1
M=D;

(skip)

// Postavljanje rezultata u R2 na 0
@R2
M=0;

// Početak petlje za zbrajanje
(pocetak)
@R0
D=M;
@R1
D=M-D;

@kraj
D;JGT // Ako je R0 > R1, završi petlju

// Dodavanje trenutne vrijednosti R0 u R2
@R0
D=M;
@R2
M=M+D;

// Povećanje R0 za 1
@R0
M=M+1;

@pocetak
0;JMP // Povratak na početak petlje

// Kraj programa
(kraj)
(END)
@END
0;JMP
