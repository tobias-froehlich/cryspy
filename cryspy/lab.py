import cryspy.numbers
import cryspy.geo

class Goniometer:
    def __init__(self, motiontype, axis, direction, parametername):
        assert motiontype in ["translation", "rotation"], \
            "First parameter for creating a Goniometer " \
            "must be one of the strings " \
            "'translation' or 'rotation'."
        assert axis in ["x", "y", "z"], \
            "Second parameter for creating a Goniometer " \
            "must be one of the strings 'x', 'y' or 'z'"
        if motiontype == "translation":
            assert direction in ["positive", "negative"], \
                "Third parameter for creating a Goniometer " \
                "for translation must be one of the strings " \
                "'positive' or 'negative'"
        elif motiontype == "rotation":
            assert direction in ["clockwise", "counterclockwise"], \
                "Third parameter for creating a Goniometer for " \
                "rotation must be one of the strings "\
                "'clockwise' or 'counterclockwise'"
        assert isinstance(parametername, str), \
            "Fourth parameter for creating a Goniometer must be " \
            "of type str. You can use any string."

        self.composed = False
        self.motiontype = motiontype
        self.axis = axis
        self.direction = direction
        self.parameternames = [parametername]


    def operator(self, parameters):
        assert isinstance(parameters, dict), \
            "Parameter of cryspy.lab.Goniometer.operator() must be a " \
            "dictionary"
 
        if not self.composed:
#            assert len(parameters) == 1, \
#                "A Goniometer which is not composed can have only one " \
#                "parameter."
#            parametername = list(parameters.keys())[0]
            assert self.parameternames[0] in parameters.keys(), \
                "You must specify the parameter called '%s'."\
                %(self.parameternames[0])
            parameter = parameters[self.parameternames[0]]                
            if self.motiontype == "translation":
                if self.direction == "negative":
                    parameter = -parameter
                if self.axis == "x":
                    return cryspy.geo.Operator(
                        cryspy.numbers.Matrix(
                            [[1, 0, 0, parameter],
                             [0, 1, 0, 0],
                             [0, 0, 1, 0],
                             [0, 0, 0, 1]
                            ]
                        )
                    )
                if self.axis == "y":
                    return cryspy.geo.Operator(
                        cryspy.numbers.Matrix(
                            [[1, 0, 0, 0],
                             [0, 1, 0, parameter],
                             [0, 0, 1, 0],
                             [0, 0, 0, 1]
                            ]
                        )
                    )
                if self.axis == "z":
                    return cryspy.geo.Operator(
                        cryspy.numbers.Matrix(
                            [[1, 0, 0, 0],
                             [0, 1, 0, 0],
                             [0, 0, 1, parameter],
                             [0, 0, 0, 1]
                            ]
                        )
                    )
            elif self.motiontype == "rotation":
                if self.direction == "clockwise":
                    parameter = -parameter
                cos = cryspy.numbers.dcos(parameter)
                sin = cryspy.numbers.dsin(parameter)
                if self.axis == "x":
                     return cryspy.geo.Operator(
                         cryspy.numbers.Matrix(
                             [[1,   0,    0, 0],
                              [0, cos, -sin, 0],
                              [0, sin,  cos, 0],
                              [0,   0,    0, 1]
                             ]
                         )
                     )
                if self.axis == "y":
                     return cryspy.geo.Operator(
                         cryspy.numbers.Matrix(
                             [[ cos,   0,  sin, 0],
                              [   0,   1,    0, 0],
                              [-sin,   0,  cos, 0],
                              [   0,   0,    0, 1]
                             ]
                         )
                     )
                if self.axis == "z":
                     return cryspy.geo.Operator(
                         cryspy.numbers.Matrix(
                             [[cos, -sin, 0, 0],
                              [sin,  cos, 0, 0],
                              [  0,    0, 1, 0],
                              [  0,    0, 0, 1]
                             ]
                         )
                     )
        else:
            return cryspy.geo.Operator(
                self.lower_gonio.operator(parameters).value
              * self.upper_gonio.operator(parameters).value
            )
           

    def __str__(self):
        if not self.composed:
            if self.motiontype == "translation":
                return    " /    translate by   \\ \n" \
                          "| %16s    |\n" \
                          "|        along        |\n" \
                          "|        %s-axis       |\n" \
                          " \\     %8s      / "\
                          %(self.parameternames[0], self.axis, self.direction)
            elif self.motiontype == "rotation":
                return    " /     rotate by    \\ \n" \
                          "| %16s   |\n" \
                          "|        around      |\n" \
                          "|        %s-axis      |\n" \
                          " \\ %16s / "\
                          %(self.parameternames[0], self.axis, self.direction)
        else:
            return cryspy.blockprint.block([[str(self.lower_gonio), " \n \n*\n \n", str(self.upper_gonio)]])



    def __mul__(self, right):
        if isinstance(right, Goniometer):
            for parametername in right.parameternames:
                 assert parametername not in self.parameternames, \
                     "Cannot multiply two Goniometers which have " \
                     "both the parameter '%s'."%(parametername)
                    
            result = Goniometer("translation", "x", "positive", "dummy")
            result.composed = True
            result.motiontype = None
            result.axis = None
            result.direction = None
            result.parameternames = self.parameternames + right.parameternames
            result.lower_gonio = self
            result.upper_gonio = right
            return result
        else:
            return NotImplemented
            
