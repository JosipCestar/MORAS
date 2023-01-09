def _parse_macros(self):
    self._iter_lines(self._parse_macro)

def _parse_macro(self, line, o, p):
    if line[0] == "$":
        macrostr = line[1:]
        macro = macrostr.split("(")

        comm = macro[0]
        #print(comm)
        print(macro)

        argsstr = []
        args = []
        if len(macro) > 1:
            argsstr = macro[1]
            argsstr = argsstr.replace(")", "")
            args = argsstr.split(",")

        if comm == "MV":
            block = self._create_mv(args[0], args[1])
            return block

        elif comm == "SWP":
            block = self._create_swp(args[0], args[1])
            return block

        elif comm == "SUM":
            block = self._create_sum(args[0], args[1], args[2])
            return block

        elif comm == "WHILE":
            block = self._create_while(args[0])
            return block

        elif comm == "END":
            block = ["@WHILE" + str(self._nested), "0;JMP","(END" + str(self._nested) + ")"]
            self._nested -= 1
            return block

        else:
            self._flag = False
            self._line = p
            self._errm = "No such command: " + comm
            return ""  
        
    else:
        return line




def _create_mv(self, a, b):
    block = ["@" + a, "D=M", "@" + b, "M=D"]
    return block

def _create_swp(self, a, b):
    block = ["@temp", "M=0", "@" + a, "D=M", "@temp", "M=D", "@" + b, "D=M", "@" + a, "M=D", "@temp", "D=M", "@" + b, "M=D"]
    return block

def _create_sum(self, a, b, d):
    block = ["@" + a, "D=M", "@" + b, "D=D+M", "@" + d, "M=D"]
    return block

def _create_while(self, arg):
    self._nested += 1
    block = ["(WHILE" + str(self._nested) + ")", "@" + arg, "D=M", "@END" + str(self._nested), "D;JEQ"]
    return block