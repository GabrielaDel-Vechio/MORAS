def _parse_macros(self):
    """Iterira kroz linije koda i procesira makro naredbe."""
    self._iter_lines(self._parse_macro)

def _mv(self, A, B):
    """Kopira vrijednost iz A u B."""
    return [
        "@" + A, "D=M", 
        "@" + B, "M=D"
    ]

def _swp(self, A, B):
    """Zamjenjuje sadržaj između A i B."""
    return [
        "@temp", "M=0", 
        "@" + A, "D=M", 
        "@temp", "M=D", 
        "@" + B, "D=M", 
        "@" + A, "M=D", 
        "@temp", "D=M", 
        "@" + B, "M=D"
    ]

def _add(self, A, B, D):
    """Zbraja A i B i sprema rezultat u D."""
    return [
        "@" + A, "D=M", 
        "@" + B, "D=D+M", 
        "@" + D, "M=D"
    ]

def _while(self, A):
    """Pokreće WHILE petlju koja se ponavlja dok RAM[A] nije 0."""
    self._nest += 1
    return [
        "(WHILE" + str(self._nest) + ")", 
        "@" + A, "D=M", 
        "@END" + str(self._nest), "D;JEQ"
    ]

def _parse_macro(self, line, o, p):
    """Razdvaja makro naredbe i pretvara ih u asemblerski kod."""
    if line[0] == "$":
        command = line[1:].split("(")
        macro = command[0]

        if len(command) > 1:
            args = command[1]
            args_list = args.replace(")", "").split(",")
            
            if macro == "MV":
                return self._mv(args_list[0], args_list[1])
            
            elif macro == "SWP":
                return self._swp(args_list[0], args_list[1])
            
            elif macro == "ADD":
                return self._add(args_list[0], args_list[1], args_list[2])

            elif macro == "WHILE":
                return self._while(args_list[0])

            else:
                self._flag = False
                self._line = o
                self._errm = "No command named '" + macro + "'"
                return ""
        
        if macro == "END":
            lines = [
                "@WHILE" + str(self._nest), 
                "0;JMP",
                "(END" + str(self._nest) + ")"
            ]
            self._nest -= 1
            return lines
    else:
        return line
