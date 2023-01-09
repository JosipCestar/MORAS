def _parse_lines(self):
    self._comment = False
    self._iter_lines(self._parse_line)

def _parse_line(self, line, p, o):
    i = 0
    l = ""

    while i < len(line) - 1:
        p = line[i] + line[i + 1]

        if self._comment == False and p == "*/":
            self._flag = False
            self._line = o
            self._errm = "Unbalanced comment delimiter"

        elif (p == "/*" and self._comment == False) or (p == "*/" and self._comment == True):
            self._comment = not self._comment
            i += 1
        elif p == "//":
            break
        elif line[i].isspace() == False and self._comment == False:
            l += line[i]
        i += 1

    return l