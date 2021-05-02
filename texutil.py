"""
PyTeXutil => Get your Python TeXgeather
"""

import win32clipboard
import sympy as sp


def setClipboard(inp):
    """ Inserts inp into clipboard """
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(inp)
    win32clipboard.CloseClipboard()


def symMatrixToTex(sym_matrix, clipboard=True):
    """ Converts symbolic matrix to TeX array format"""
    out = ""
    for i in range(sym_matrix.shape[0]):
        arr = [j.__str__() for j in sym_matrix[i, :]]
        out_str = ' & '.join(arr).replace(
            '**', '^').replace('*', ' ') + ' \\\\'
        out += out_str + '\n'

    if clipboard:
        setClipboard(out)
    else:
        return out


class texTex:
    """ Class for TeX data storing """

    def __init__(self) -> None:
        """ Creates/opens the file and zeroes the counter """
        self.f = open("./textex.tex", 'w')
        self.ct = 0

    def addLine(self, line, title=None) -> None:
        """ Adds line to file """

        if title is not None:
            self.f.writelines(['\n\n',
                               'Line[{}]: {}.'.format(self.ct, title)])

        self.f.writelines('\n\n' + str(line))
        self.ct += 1

    def addMatrix(self, matrix, name = None, title=None, rename_dict=None) -> None:
        """ Adds matrix to file """

        line = symMatrixToTex(matrix, clipboard=False)

        if rename_dict is not None:
            for key, value in rename_dict.items():
                line.replace(key, value)

        if title is not None:
            self.f.writelines(['\n\n',
                               'Line[{}]: {}.'.format(self.ct, title)])

        if name is not None:
            self.f.writelines('\n\n' + name + ' = ' +  line)
        else:
            self.f.writelines('\n\n' + line)
        self.ct += 1

    def closeFile(self):
        self.f.close()
