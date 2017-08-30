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
        self.parametername = parametername

    def operator(self, parameters):
        assert isinstance(parameters, dict), \
            "Parameter of cryspy.lab.Goniometer.operator() must be a " \
            "dictionary"
 
        if not self.composed:
            assert len(parameters) == 1, \
                "A Goniometer which is not composed can have only one " \
                "parameter."

            parametername = list(parameters.keys())[0]
            parameter = parameters[parametername]
            assert parametername == self.parametername, \
                "The Goniometer has no parameter called '%s'." \
                %(list(parameters.keys())[0])
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
        else:
            pass
           
       
