from CodeBase.fileIO.Input.InputTypes.input_parent import InputParent


# DFX NOT SUPPORTED RN.

class ReadDxf(InputParent):
    def __init__(self, dxf_config, common_form):
        super().__init__()
        self.readfile(filepath)

    def parse_into_cf(self):
        #
        # DXF parser
        #
        print("DXF NOT SUPPORTED")
        '''
        segment = -1
        path = []
        xold = []
        yold = []
        line = 0
        nlines = len(self.file_by_line_list)
        polyline = 0
        vertex = 0
        while line < nlines:
            if self.file_by_line_list[line] == "POLYLINE\n":
                segment += 1
                polyline = 1
                path.append([])
            elif self.file_by_line_list[line] == "VERTEX\n":
                vertex = 1
            elif (self.file_by_line_list[line] == "10") & (vertex == 1) & (polyline == 1):
                line += 1
                x = float(self.file_by_line_list[line])
            elif (self.file_by_line_list[line] == "20") & (vertex == 1) & (polyline == 1):
                line += 1
                y = float(self.file_by_line_list[line])
                if (x != xold) | (y != yold):
                    #
                    # add to path if not zero-length segment
                    #
                    path[segment].append([float(x), float(y), []])
                    xold = x
                    yold = y
            elif self.file_by_line_list[line] == "SEQEND\n":
                polyline = 0
                vertex = 0
            line += 1
        return path
        '''
