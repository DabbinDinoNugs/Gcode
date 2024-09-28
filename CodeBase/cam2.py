#
# cam2.py
#
#THIS INFO HAS MODIFIED
# usage: python cam2.py [infile] [xoffset yoffset] [display size] [outfile] [undercut]
#
# input:
#     *.dxf: DXF (polylines)
#     *.cmp,*.sol,*.plc: Gerber
#         RS-274X format, with 0-width trace defining board boundary
#     *.drl: Excellon drill file, with tool defitions
# output:
#     *.rml: Roland Modela RML mill
#     *.camm: Roland CAMM cutter
#     *.jpg,*.bmp: images
#     *.epi: Epilog lasercutter
#     *.g: G codes
# toolpath modes: 1D path, contour, raster
# keys: q to quit
# originally by:
# (C)BA Neil Gershenfeld
# commercial sale licensed by MIT
#
# modified by
# tedgrosch
# on Apr 2, 2017
#
# Updated
# 9/12/2024
import sys



if __name__ == "__main__":
    infileDirectoryPath = sys.argv[1]
    outfileDirectoryPath = sys.argv[2]

    # Create new config object for global slicer settings.
    # Create new Input object for each infile.
    # Create new Output object that inherits output_parent.
    # IF GUI = TRUE in config,
    # Create new GUI object walk through steps that way.
    # ELSE, do the work automaticaly...

