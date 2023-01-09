class Parser:
    def __init__(self, filename):
        try:
            self._file = open(filename + ".asm", "r")
        except:
            Parser._error("File", -1, "Cannot open file.")
            return


        #varijable vezane uz greske
        self._flag = True
        self._line = -1
        self._errm = ""

        self._labels = {}
        self._variables = {}

        #lista linija kodova u fileu
        self._origlines = []
        self._lines = []
        self._read_lines()
        self._origlines = self._lines

        self._parse_lines()
        if self._flag == False:
            Parser._error("S&C", self._line, self._errm)
            return


        self._nested = 0

        self._parse_macros()
        if self._flag == False:
            Parser._error("MACRO", self._line, self._errm)
            return


        self._parse_symbols()
        if self._flag == False:
            Parser._error("SYM", self._line, self._errm)
            return

        self._parse_commands()
        if self._flag == False:
            Parser._error("COM", self._line, self._errm)
            return


        print("Oznake")
        print(self._labels)
        print("Varijable")
        print(self._variables)
        
        

        try:
            self._outfile = open(filename + ".hack", "w")
        except:
            Parser._error("File", -1, "Cannot open output file.")
            return

        try:
            self._write_file()
        except:
            Parser._error("File", -1, "Cannot write to output file.")
            return

        for line in self._lines:
            print(line)



    from parselines import _parse_lines, _parse_line
    from parsesymbs import _parse_symbols, _parse_symbol, _parse_variable, _init_labels
    from parsecomms import _parse_commands, _parse_command, _init_comms
    from parsemacros import _parse_macros, _parse_macro, _create_while, _create_mv, _create_swp, _create_sum



    def _read_lines(self):
        n = 0
        for line in self._file:
            self._lines.append((line, n, n))
            n += 1



    def _write_file(self):
        for (line, p, o) in self._lines:
            self._outfile.write(line)
            if line[-1] != "\n":
                self._outfile.write("\n")



    def _iter_lines(self, func):
        i = 0
        newlines = []

        for (line, p, o) in self._lines:

            funcReturn = func(line, p, o)

            if isinstance(funcReturn, list):

                for l in funcReturn:
                    if len(l) > 0:
                        newlines.append((l, i, o))
                        if l[0] != "(":
                            i += 1
            else:
                newline = funcReturn

                if len(newline) > 0:
                    newlines.append((newline, i, o))
                    if newline[0] != "(":
                        i += 1

        self._lines = newlines


    @staticmethod
    def _error(src, line, msg):
        if len(src) > 0 and line > -1:
            print("[" + src + ", " + str(line) + "] " + msg)
        elif len(src) > 0:
            print("[" + src + "] " + msg)
        else:
            print(msg)



if __name__ == "__main__":
    Parser("test")