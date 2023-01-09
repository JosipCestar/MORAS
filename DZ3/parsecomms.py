def _parse_commands(self):
    self._init_comms()
    self._iter_lines(self._parse_command)


def _parse_command(self, line, p, o):

    if line[0] == "@":
        bin_num = "{0:b}".format(int(line[1:]))
        return "0" * (16 - len(bin_num)) + bin_num
    else:
    
        dest = ""
        comp = ""
        jump = ""

        l = line.split("=")
        if len(l) == 2:
            dest = l[0]
            l = l[1]
        else:
            l = l[0]

        l = l.split(";")
        if len(l) == 2:
            jump = l[1]
        comp = l[0]

        if dest not in self._dest.keys():
            self._flag = False
            self._line = o
            self._errm = "Invalid destination" + dest + "."

        if comp not in self._op.keys():
            self._flag = False
            self._line = o
            self._errm = "Invalid operator " + comp + "."

        if jump not in self._jmp.keys():
            self._flag = False
            self._line = o
            self._errm = "Invalid jump " + jump + "."

        return "111" + self._op[comp] + self._dest[dest] + self._jmp[jump]




def _init_comms(self):
    self._op = {
        "0": "0101010",
        "1": "0111111",
        "-1": "0111010",
        "D": "0001100",
        "A": "0110000",
        "!D": "0001101",
        "!A": "0110001",
        "-D": "0001111",
        "-A": "0110011",
        "D+1": "0011111",
        "A+1": "0110111",
        "D-1": "0001110",
        "A-1": "0110010",
        "D+A": "0000010",
        "A+D": "0000010",
        "D-A": "0010011",
        "A-D": "0000111",
        "D&A": "0000000",
        "A&D": "0000000",
        "D|A": "0010101",
        "A|D": "0010101",
        "M": "1110000",
        "!M": "1110001",
        "-M": "1110011",
        "M+1": "1110111",
        "M-1": "1110010",
        "D+M": "1000010",
        "M+D": "1000010",
        "D-M": "1010011",
        "M-D": "1000111",
        "D&M": "1000000",
        "M&D": "1000000",
        "D|M": "1010101",
        "M|D": "1010101"
    }
    self._jmp = {
        "": "000",
        "JGT": "001",
        "JEQ": "010",
        "JGE": "011",
        "JLT": "100",
        "JNE": "101",
        "JLE": "110",
        "JMP": "111"
    }
    self._dest = {
        "": "000",
        "M": "001",
        "D": "010",
        "MD": "011",
        "A": "100",
        "AM": "101",
        "AD": "110",
        "AMD": "111"
    }