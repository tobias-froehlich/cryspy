//START_CAM
camera {
    location <20.000000, 5.000000, 20.000000>
    angle 50.000000
    sky <0.000000, 1.000000, 0.000000>
    look_at <0.000000, 0.000000, 0.000000>
    right <600, 0, 0>
    up <0, 400, 0>
}
background {color rgb <1, 1, 1>}

global_settings { ambient_light rgb <7, 7, 7> }
//END_CAM
cylinder {
    <0.000000, 0.000000, 0.000000>,
    <9.941600, 0.000000, 0.000000>,
    0.050000
    pigment {
        color rgb <0.000000, 0.000000, 0.000000>
    }
}
cone {
    <9.941600, 0.000000, 0.000000>,
    0.200000
    <10.441600, 0.000000, 0.000000>,
    0
    pigment {
        color rgb <0.000000, 0.000000, 0.000000>
    }
}
cylinder {
    <0.000000, 0.000000, 0.000000>,
    <-4.970800, 0.000000, 8.609678>,
    0.050000
    pigment {
        color rgb <0.000000, 0.000000, 0.000000>
    }
}
cone {
    <-4.970800, 0.000000, 8.609678>,
    0.200000
    <-5.220800, 0.000000, 9.042691>,
    0
    pigment {
        color rgb <0.000000, 0.000000, 0.000000>
    }
}
cylinder {
    <0.000000, 0.000000, 0.000000>,
    <0.000000, 5.843200, 0.000000>,
    0.050000
    pigment {
        color rgb <0.000000, 0.000000, 0.000000>
    }
}
cone {
    <0.000000, 5.843200, 0.000000>,
    0.200000
    <0.000000, 6.343200, 0.000000>,
    0
    pigment {
        color rgb <0.000000, 0.000000, 0.000000>
    }
}

#declare Atom_O = sphere {
    <0, 0, 0>, 0.200000
    pigment {
        color rgb <1.000000, 0.051000, 0.051000>
    }
}
#declare Atom_Mn = sphere {
    <0, 0, 0>, 0.292400
    pigment {
        color rgb <0.611800, 0.478400, 0.780400>
    }
}
#declare Atom_Ca = sphere {
    <0, 0, 0>, 0.271400
    pigment {
        color rgb <0.239200, 1.000000, 0.000000>
    }
}
//START_LEGEND
//END_LEGEND
object {
    Atom_O
    translate <1.689451, 4.745136, 4.015558>
}
object {
    Atom_Mn
    translate <-2.610400, 5.286000, 7.535576>
}
object {
    Atom_O
    translate <0.847231, 2.163031, 4.721189>
}
object {
    Atom_O
    translate <-4.373569, 4.277431, 7.735419>
}
object {
    Atom_O
    translate <4.512285, 4.180169, 1.626871>
}
object {
    Atom_Mn
    translate <-5.220800, 3.171600, 9.042691>
}
object {
    Atom_Mn
    translate <5.220800, 3.171600, 0.000000>
}
object {
    Atom_O
    translate <6.910251, 2.630736, 1.001327>
}
object {
    Atom_Mn
    translate <-2.610400, 6.343200, 4.521345>
}
object {
    Atom_O
    translate <4.373569, 4.180169, 4.321502>
}
object {
    Atom_O
    translate <6.776546, 4.180169, 3.094318>
}
object {
    Atom_O
    translate <6.068031, 6.391831, 1.706959>
}
object {
    Atom_O
    translate <6.119300, 2.630736, 5.483789>
}
object {
    Atom_O
    translate <2.587951, 3.712464, 6.485116>
}
object {
    Atom_Ca
    translate <5.220800, 6.343200, 9.042691>
}
object {
    Atom_O
    translate <3.665054, 0.048631, 2.934142>
}
object {
    Atom_Ca
    translate <10.441600, 0.000000, 0.000000>
}
object {
    Atom_Ca
    translate <-5.220800, 6.343200, 9.042691>
}
object {
    Atom_Mn
    translate <7.831200, 0.000000, 4.521345>
}
object {
    Atom_O
    translate <2.587951, 5.826864, 0.456656>
}
object {
    Atom_Mn
    translate <2.610400, 0.000000, 4.521345>
}
object {
    Atom_O
    translate <0.898500, 0.516336, 2.469559>
}
object {
    Atom_O
    translate <2.632849, 2.630736, 2.557574>
}
object {
    Atom_Mn
    translate <2.610400, 4.228800, 1.507115>
}
object {
    Atom_Ca
    translate <10.441600, 6.343200, 0.000000>
}
object {
    Atom_O
    translate <-0.898500, 3.712464, 3.558902>
}
object {
    Atom_O
    translate <6.068031, 4.277431, 7.735419>
}
object {
    Atom_Mn
    translate <2.610400, 6.343200, 4.521345>
}
object {
    Atom_O
    translate <0.898500, 4.745136, 8.498019>
}
object {
    Atom_O
    translate <-3.531349, 0.516336, 7.029788>
}
object {
    Atom_Mn
    translate <5.220800, 3.171600, 9.042691>
}
object {
    Atom_Mn
    translate <7.831200, 6.343200, 4.521345>
}
object {
    Atom_O
    translate <1.555746, 2.065769, 0.080088>
}
object {
    Atom_Mn
    translate <0.000000, 0.000000, 9.042691>
}
object {
    Atom_Ca
    translate <0.000000, 4.228800, 6.028461>
}
object {
    Atom_O
    translate <3.665054, 6.391831, 2.934142>
}
object {
    Atom_O
    translate <4.322300, 5.826864, 6.573132>
}
object {
    Atom_O
    translate <-1.555746, 2.163031, 5.948372>
}
object {
    Atom_O
    translate <-0.708515, 6.294569, 4.641101>
}
object {
    Atom_O
    translate <1.555746, 6.294569, 6.108549>
}
object {
    Atom_O
    translate <3.531349, 1.598064, 5.027133>
}
object {
    Atom_Mn
    translate <-2.610400, 0.000000, 4.521345>
}
object {
    Atom_Mn
    translate <7.831200, 1.057200, 1.507115>
}
object {
    Atom_Mn
    translate <7.831200, 4.228800, 1.507115>
}
object {
    Atom_O
    translate <-2.587951, 4.745136, 5.571805>
}
object {
    Atom_Mn
    translate <0.000000, 3.171600, 0.000000>
}
object {
    Atom_Mn
    translate <2.610400, 3.171600, 4.521345>
}
object {
    Atom_O
    translate <5.929315, 0.048631, 4.401590>
}
object {
    Atom_O
    translate <9.594369, 2.065769, 1.307272>
}
object {
    Atom_O
    translate <4.322300, 1.598064, 0.544671>
}
object {
    Atom_O
    translate <2.632849, 0.516336, 8.586035>
}
object {
    Atom_O
    translate <-0.847231, 6.294569, 7.335732>
}
object {
    Atom_Mn
    translate <0.000000, 5.286000, 3.014230>
}
object {
    Atom_Mn
    translate <5.220800, 6.343200, 0.000000>
}
object {
    Atom_Mn
    translate <5.220800, 1.057200, 6.028461>
}
object {
    Atom_O
    translate <3.665054, 4.277431, 8.962603>
}
object {
    Atom_O
    translate <8.752149, 5.826864, 2.012903>
}
object {
    Atom_Ca
    translate <0.000000, 0.000000, 0.000000>
}
object {
    Atom_Mn
    translate <0.000000, 2.114400, 3.014230>
}
object {
    Atom_O
    translate <-1.689451, 3.712464, 8.041364>
}
object {
    Atom_O
    translate <0.708515, 2.163031, 7.415820>
}
object {
    Atom_Mn
    translate <5.220800, 4.228800, 6.028461>
}
object {
    Atom_Mn
    translate <2.610400, 5.286000, 7.535576>
}
object {
    Atom_Ca
    translate <5.220800, 0.000000, 9.042691>
}
object {
    Atom_Mn
    translate <7.831200, 3.171600, 4.521345>
}
object {
    Atom_Mn
    translate <10.441600, 3.171600, 0.000000>
}
object {
    Atom_O
    translate <5.929315, 6.391831, 4.401590>
}
object {
    Atom_Mn
    translate <5.220800, 0.000000, 0.000000>
}
object {
    Atom_Mn
    translate <0.000000, 1.057200, 6.028461>
}
object {
    Atom_Ca
    translate <0.000000, 6.343200, 0.000000>
}
object {
    Atom_Ca
    translate <-5.220800, 0.000000, 9.042691>
}
object {
    Atom_Mn
    translate <-2.610400, 2.114400, 7.535576>
}
object {
    Atom_Mn
    translate <2.610400, 1.057200, 1.507115>
}
object {
    Atom_Mn
    translate <0.000000, 6.343200, 9.042691>
}
object {
    Atom_Mn
    translate <5.220800, 5.286000, 3.014230>
}
object {
    Atom_O
    translate <0.708515, 4.277431, 1.387360>
}
object {
    Atom_O
    translate <7.808751, 1.598064, 3.470886>
}
object {
    Atom_Ca
    translate <5.220800, 2.114400, 3.014230>
}
object {
    Atom_Mn
    translate <2.610400, 2.114400, 7.535576>
}
object {
    Atom_O
    translate <-3.665054, 2.065769, 9.122779>
}
object {
    Atom_O
    translate <4.512285, 2.065769, 7.655331>
}
object {
    Atom_O
    translate <6.068031, 0.048631, 1.706959>
}
object {
    Atom_Mn
    translate <-2.610400, 3.171600, 4.521345>
}
object {
    Atom_Mn
    translate <0.000000, 3.171600, 9.042691>
}
cylinder {
    <0.000000, 0.000000, 0.000000>,
    <2.610400, 0.000000, 4.521345>,
    0.050000
    pigment {
        color rgb <0.500000, 0.500000, 0.500000>
    }
}
mesh2 {
    vertex_vectors {3, <0.000000, 0.000000, 0.000000>, <10.441600, 0.000000, 0.000000>, <-5.220800, 0.000000, 9.042691>}
    face_indices {1, <0, 1, 2>}
    pigment {
        color rgbt <0.700000, 0.700000, 0.700000, 0.300000>
    }
}
cylinder {
    <-54.749197, 3.171600, -28.595233>,
    <59.450382, 3.171600, 37.337924>,
    0.100000
    pigment {
        color rgb <0.000000, 0.000000, 1.000000>
    }
}
cone {
    <59.450382, 3.171600, 37.337924>,
    0.300000
    <59.969997, 3.171600, 37.637924>,
    0
    pigment {
        color rgb <0.000000, 0.000000, 1.000000>
    }
}
cylinder {
    <2.610400, -91.248561, 4.521345>,
    <2.610400, 96.991761, 4.521345>,
    0.100000
    pigment {
        color rgb <0.000000, 0.000000, 1.000000>
    }
}
cone {
    <2.610400, 96.991761, 4.521345>,
    0.300000
    <2.610400, 97.591761, 4.521345>,
    0
    pigment {
        color rgb <0.000000, 0.000000, 1.000000>
    }
}
cylinder {
    <2.610400, 3.171600, -61.711812>,
    <2.610400, 3.171600, 70.154503>,
    0.100000
    pigment {
        color rgb <0.000000, 0.000000, 1.000000>
    }
}
cone {
    <2.610400, 3.171600, 70.154503>,
    0.300000
    <2.610400, 3.171600, 70.754503>,
    0
    pigment {
        color rgb <0.000000, 0.000000, 1.000000>
    }
}

