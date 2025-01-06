@32767
D=A
@najmanji
M=D

// Postavljanje brojača brojac na 0
@0
D=A
@brojac
M=D

(LOOP_START)
// Ako je brojac >= 5, završi petlju
@brojac
D=M
@5
D=D-A
@END
D;JGE

@brojac
A=M
D=M

@SKIP
D;JLE

@najmanji
D=D-M
@SKIP
D;JGE
@brojac
A=M
D=M
@najmanji
M=D

(SKIP)
// brojac++
@brojac
M=M+1
@LOOP_START
0;JMP

(END)
@najmanji
D=M
@5
M=D

// Beskonačna petlja
(LOOP)
@LOOP
0;JMP
