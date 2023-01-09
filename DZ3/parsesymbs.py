def _parse_symbols(self):
    self._init_labels()
    self._iter_lines(self._parse_symbol)
    self._counter = 16
    self._iter_lines(self._parse_variable)


def _parse_symbol(self, line, p, o):
    if line[0] != "(":
        return line
    else:
        
        lineSplit = line[1:].split(")")
        label = lineSplit[0] 
        rest = lineSplit[1:]
        
        cond = [r.strip("\n\t\r") for r in rest]

        if len(rest) != 0 and any(cond): 
            self._flag = False
            self._line = o
            self._errm = "No text allowed after the label"
            
        elif len(label) == 0:
            self._flag = False
            self._line = o
            self._errm = "Invalid label"

        else:
            self._labels[label] = str(p)
    return ""

def _parse_variable(self, line, p, o):
    if line[0] != "@":
        return line
    else:
        var = line[1:]

        if var.isdigit() == True:
            return line
        
        if var in self._labels.keys():
            return "@" + self._labels[var]
        elif var in self._variables.keys():
            return "@" + self._variables[var]
        else:
            self._variables[var] = str(self._counter)
            self._counter += 1
            return "@" + str(self._counter - 1)



def _init_labels(self):
    self._labels = {
        "SCREEN": "16384",
        "KBD": "24576",
        "SP": "0",
        "LCL": "1",
        "ARG": "2",
        "THIS": "3",
        "THAT": "4"
    }

    for i in range(0, 16):
        self._labels["R" + str(i)] = str(i)