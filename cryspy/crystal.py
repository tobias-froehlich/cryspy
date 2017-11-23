import hashlib
import numpy as np
from cryspy import numbers as nb
from cryspy import geo as geo
from cryspy import blockprint as bp
from cryspy import tables

class Drawable():
    def __init__(self, name, pos):
        assert isinstance(name, str), \
            "First argument of crystal.Drawable.__init__(...) must be " \
            "of type str."
        assert isinstance(pos, geo.Pos), \
            "Second argument of crystal.Drawable.__init__(...) must be " \
            "of type geo.Pos."
        self.name = name
        self.pos = pos
        self.has_color = False
        self.color = None
    
    def set_color(self, color):
        assert isinstance(color, tuple), \
            "Argument of crystal.Momentum.set_color(color) must be of type " \
            " tuple."
        assert (len(color) == 3), \
            "Argument of crystal.Momentum.set_color(color) must be of type "\
            "tuple and must have three items."
        for item in color:
            assert isinstance(item, float) or isinstance(item, int) \
                or isinstance(item, nb.Mixed), \
                "Argument of crystal.Momentum.set_color(color) must be of " \
                "type tuple with three numbers in it."
        self.has_color = True
        self.color = (float(color[0]), float(color[1]), float(color[2]))
    

class Atom(Drawable):
    def __init__(self, name, typ, pos):
        assert isinstance(name, str), \
            "First argument must be of type str."
        assert isinstance(typ, str), \
            "Second argument must be of type str."
        assert isinstance(pos, geo.Pos), \
            "Third argument must be of type Pos."
        Drawable.__init__(self, name, pos)
        self.typ = typ
        self.pos = pos

    def __str__(self):
        return bp.block([["Atom", " " + self.name,
                          " " + self.typ, " " + self.pos.__str__()], ])

    def __eq__(self, right):
        return hash(self) == hash(right)

    def __add__(self, right):
        if isinstance(right, geo.Dif):
            return Atom(self.name, self.typ, self.pos + right)
        elif isinstance(right, str):
            return Atom(self.name + right, self.typ, self.pos)
        else:
            return NotImplemented

    def __rpow__(self, left):
        assert isinstance(left, geo.Operator) \
            or isinstance(left, geo.Coset), \
            "I cannot apply an object of type %s " \
            "to an object of type Atom." % (type(left))
        return Atom(self.name, self.typ, left ** self.pos)

    def __mod__(self, right):
        assert isinstance(right, geo.Transgen), \
            "I cannot take an object of type Atom " \
            "modulo an object of type %s" % (type(right))
        return Atom(self.name, self.typ, self.pos % right)

    def __hash__(self):
        string = "atom%s%i" % (
            self.typ,
            hash(self.pos))
        return int(hashlib.sha1(string.encode()).hexdigest(), 16)


class Momentum(Drawable):
    def __init__(self, name, pos, direction):
        assert isinstance(pos, geo.Pos), \
            "First argument of crystal.Momentum(pos, dir) must be of type " \
            " geo.Pos ."
        assert isinstance(direction, geo.Dif), \
            "Second argument of crystal.Momentum(pos, dir) must be of type" \
            " geo.Dif ."
        Drawable.__init__(self, name, pos)
        self.direction = direction
        self.has_plotlength = False
        self.plotlength = None

    def set_plotlength(self, plotlength):
        assert isinstance(plotlength, float) or isinstance(plotlength, int) \
            or isinstance(plotlength, nb.Mixed), \
            "Argument of crystal.Momentum.set_plotlength(plotlength) must " \
            "be of type float or int or numbers.Mixed."
        self.has_plotlength = True
        self.plotlength = float(plotlength)

    def __str__(self):
        return "Momentum"

    def __eq__(self, right):
        if isinstance(right, Momentum):
            if (self.pos == right.pos) and (self.direction == right.direction):
                return True
            else:
                return False
        else:
            return False

    def __add__(self, right):
        if isinstance(right, geo.Dif):
            result = Momentum(self.name, self.pos + right, self.direction)
            if self.has_color:
                result.set_color(self.color)
            if self.has_plotlength:
                result.set_plotlength(self.plotlength)
            return result
        elif isinstance(right, str):
            return Momentum(self.name + right, self.pos, self.direction)
        else:
            return NotImplemented

    def __rpow__(self, left):
        if isinstance(left, geo.Operator) \
            or isinstance(left, geo.Coset):
            result = Momentum(self.name, left ** self.pos, self.direction)
            if self.has_color:
                result.set_color(self.color)
            if self.has_plotlength:
                result.set_plotlength(self.plotlength)
            return result
        else:
            return NotImplemented

    def __mod__(self, right):
        assert isinstance(right, geo.Transgen), \
            "I cannot take an object of type Atom " \
            "modulo an object of type %s" % (type(right))
        return Momentum(self.name, self.pos % right, self.direction)


    def __hash__(self):
        string = "momentum%i,%i" \
            % (hash(self.pos), hash(self.direction))
        return int(hashlib.sha1(string.encode()).hexdigest(), 16)


class Bond(Drawable):
    def __init__(self, name, start, target):
        assert isinstance(start, geo.Pos), \
            "The start position of an object of type Bond " \
            "must be of type geo.Position."
        assert isinstance(target, geo.Pos), \
            "The target position of an object of type Bond " \
            "must be of type geo.Position."
        Drawable.__init__(self, name, geo.centre_of_gravity([start, target]))
        self.start = start
        self.target = target
        self.has_thickness = False
        self.thickness = None

    def set_color(self, color):
        assert isinstance(color, tuple), \
            "Argument of crystal.Bond.set_color(color) must be of type " \
            " tuple."
        assert (len(color) == 3), \
            "Argument of crystal.Bond.set_color(color) must be of type "\
            "tuple and must have three items."
        for item in color:
            assert isinstance(item, float) or isinstance(item, int) \
                or isinstance(item, nb.Mixed), \
                "Argument of crystal.Bond.set_color(color) must be of " \
                "type tuple with three numbers in it."
        self.has_color = True
        self.color = (float(color[0]), float(color[1]), float(color[2]))

    def set_thickness(self, thickness):
        assert isinstance(thickness, float) or isinstance(thickness, int) \
            or isinstance(thickness, nb.Mixed), \
            "Argument of crystal.Bond.set_thickness(...) must be of type " \
            "float, int or Mixed."
        self.thickness = thickness
        self.has_thickness = True

    def __str__(self):
        return "Bond"

    def __eq__(self, right):
        if isinstance(right, Bond):
            if   (self.start == right.start) and (self.target == right.target) \
              or (self.start == right.target) and (self.target == right.start):
                return True
            else:
                return False
        else:
            return False

    def __add__(self, right):
        if isinstance(right, geo.Dif):
            result = Bond(self.name, self.start + right, self.target + right)
            if self.has_color:
                result.set_color(self.color)
            if self.has_thickness:
                result.set_thickness(self.thickness)
            return result
        elif isinstance(right, str):
            result = Bond(self.name + right, self.start, self.target)
            if self.has_color:
                result.set_color(self.color)
            if self.has_thickness:
                result.set_thickness(self.thickness)
            return result
        else:
            return NotImplemented

    def __rpow__(self, left):
        if isinstance(left, geo.Operator) \
            or isinstance(left, geo.Coset):
            result = Bond(self.name, left ** self.start, left ** self.target)
            if self.has_color:
                result.set_color(self.color)
            if self.has_thickness:
                result.set_thickness(self.thickness)
            return result
        else:
            return NotImplemented

    def __mod__(self, right):
        assert isinstance(right, geo.Transgen), \
            "Cannot apply object of type %s to object of type " \
            "cryspy.crystal.Bond."%(str(type(left)))
        if isinstance(right, geo.Transgen):
            pos_new = self.pos % right
            correct = (pos_new - self.pos).to_Symmetry()
            new_bond = Bond(
                self.name, correct ** self.start, correct ** self.target
            )
            if self.has_color:
                new_bond.set_color(self.color)
            if self.has_thickness:
                new_bond.set_thickness(self.thickness)
            return new_bond


    def __hash__(self):
        # The order of start and target does not matter.
        # This is why I hash the sum and the product of the hashes.
        string = "bond%i,%i" \
            % (hash(self.start)+hash(self.target),
               hash(self.start) * hash(self.target))
        return int(hashlib.sha1(string.encode()).hexdigest(), 16)


class Face(Drawable):
    def __init__(self, name, corners):
        assert isinstance(corners, list), \
            "Face must be created by a list of objects of type geo.Pos."
        for corner in corners:
            assert isinstance(corner, geo.Pos), \
                "Face must be created by a list of objects of type geo.Pos."
        Drawable.__init__(self, name, geo.centre_of_gravity(corners))
        self.corners = corners
        self.has_opacity = False
        self.opacity = None
 
    def set_color(self, color):
        assert isinstance(color, tuple), \
            "Argument of crystal.Bond.set_color(color) must be of type " \
            " tuple."
        assert (len(color) == 3), \
            "Argument of crystal.Bond.set_color(color) must be of type "\
            "tuple and must have three items."
        for item in color:
            assert isinstance(item, float) or isinstance(item, int) \
                or isinstance(item, nb.Mixed), \
                "Argument of crystal.Bond.set_color(color) must be of " \
                "type tuple with three numbers in it."
        self.has_color = True
        self.color = (float(color[0]), float(color[1]), float(color[2]))

    def set_opacity(self, opacity):
        assert isinstance(opacity, nb.Mixed) or isinstance(opacity, float) \
            or isinstance(opacity, int), \
            "Opacity must be a number."
        assert 0 <= float(opacity) <= 1, \
            "Opacity must be between 0 and 1."
        self.has_opacity = True
        self.opacity = opacity 

    def flip(self):
    # Flips the orientation, i.e. reverses the order of the corners.
        liste = []
        for corner in self.corners:
            liste.append(corner)
        n = len(liste)
        liste = [liste[n-i-1] for i in range(n)]
        result = Face(self.name, liste)
        if self.has_color:
            result.set_color(self.color)
        if self.has_opacity:
            result.set_opacity(self.opacity)
        return result

    def __str__(self):
        return "Face"

    def __eq__(self, right):
        return hash(self) == hash(right)

    def __add__(self, right):
        if isinstance(right, geo.Dif):
            liste = []
            for corner in self.corners:
                liste.append(corner + right)
            result = Face(self.name, liste)
            if self.has_color:
                result.set_color(self.color)
            if self.has_opacity:
                result.set_opacity(self.opacity)
            return result
        elif isinstance(right, str):
            return Face(self.name + right, self.corners)
        else:
            return NotImplemented

    def __rpow__(self, left):
        print("+++++++++++++++++", type(left))
        if isinstance(left, geo.Operator) \
            or isinstance(left, geo.Coset):
            must_flip = False
            if isinstance(left, geo.Operator):
                if float(left.value.det()) < 0:
                    must_flip = True
                result = Face(self.name, [left ** corner for corner in self.corners])
            elif isinstance(left, geo.Coset):
                if float(left.symmetry.value.det()) < 0:
                    must_flip = True
                correct = (left**self.pos - left.symmetry**self.pos).to_Symmetry()
                result = Face(
                    self.name,
                    [correct ** (left.symmetry ** corner)
                        for corner in self.corners]
                )
            if self.has_color:
                result.set_color(self.color)
            if self.has_opacity:
                result.set_opacity(self.opacity)
            if must_flip:
                result = result.flip()
            return result
        else:
            return NotImplemented

    def __hash__(self):
        summe = 0
        sum_of_products = 0
        for i in range(len(self.corners) - 1):
            summe += hash(self.corners[i])
            sum_of_products += hash(self.corners[i]) * hash(self.corners[i+1])**2
        summe += hash(self.corners[-1])
        sum_of_products += hash(self.corners[-1]) * hash(self.corners[0])**2

        string = "face%i,%i" % \
                 (summe, sum_of_products)
        return int(hashlib.sha1(string.encode()).hexdigest(), 16)


class Bitmapface(Drawable):
    def __init__(self, name, southwest, southeast, northwest, northeast, bitmap, format):
        # Corners:
        #            northwest                         northeast
        #                       ----------------------
        #                      |                      |
        #                      | bitmap 1. index      |
        #                      | ^                    |
        #                      | |                    |
        #                      |  -> bitmap 0. index  |
        #                       ----------------------
        #            southwest                         southeast
        #
        # Parameter format must be "RGBA", but in future more possibilities
        # can be implemented.
        #
        # 3. index of bitmap depends on format. Eg. for format = "RGBA" the
        # index counts through red, green, blue, opacity.

        assert isinstance(name, str), \
           "Error: First argument for creating cryspy.crystal.Bitmapface must " \
           "be of type str ."

        assert  isinstance(southwest, geo.Pos) \
            and isinstance(southeast, geo.Pos) \
            and isinstance(northwest, geo.Pos) \
            and isinstance(northeast, geo.Pos), \
            "Error: 2. to 5. arguments for creating cryspy.crystal.Bitmapface must be " \
            "of type cryspy.geo.Pos ."
        
        assert isinstance(bitmap, np.ndarray), \
            "Error: 6. argument for creating cryspy.crystal.Bitmapface must be " \
            "of type numpy.array ."

        assert len(bitmap.shape) == 3, \
            "Error: 6. argument for creating cryspy.crystal.Bitmapface must be " \
            "of type numpy.array with three indices ."

        assert isinstance(format, str), \
            "Error: 7. argument for creating cryspy.crystal.Bitmapface must be " \
            "of type str ."

        assert format in ["RGBA"], \
            "Error: 7. argument for creating cryspy.crystal.Bitmapface must be " \
            "the string 'RGBA' ."

        if format == "RGBA":
            assert bitmap.shape[2] == 4, \
                 "Error creating an object of type cryspy.crystal.Bitmapface:\n" \
                 "In the case format = 'RGBA', bitmap must be " \
                 "of shape (*, *, 4) ."
        self.name = name
        self.southwest = southwest
        self.southeast = southeast
        self.northwest = northwest
        self.northeast = northeast
        self.bitmap = bitmap
        self.format = format 


class Atomset():
    def __init__(self, menge):
        assert isinstance(menge, set), \
            "Argument must be of type set."
        for item in menge:
            assert isinstance(item, Atom) or isinstance(item, Momentum) \
                or isinstance(item, Bond) or isinstance(item, Face) \
                or isinstance(item, Subset) or isinstance(item, Bitmapface), \
                "Argument must be a set of "\
                "objects of type Atom, Momentum, Bond or Face."
        self.menge = menge
        self.names = set([])
        for item in menge:
            self.names.add(item.name)

    def __eq__(self, right):
        if isinstance(right, Atomset):
            return (self.menge == right.menge)
        else:
            return False

    def __str__(self):
        # The Atoms are printed in alphabetically order with regard to
        # the name, and if name is equal, with regard to the type.
        strings = [["Atomset\n"
                    "-------"], ]
        liste = [atom for atom in self.menge]
        atomliste = []
        momentumliste = []
        bondliste = []
        faceliste = []
        subsetliste = []
        for item in self.menge:
            if isinstance(item, Atom):
                atomliste.append(item)
            elif isinstance(item, Momentum):
                momentumliste.append(item)
            elif isinstance(item, Bond):
                bondliste.append(item)
            elif isinstance(item, Face):
                faceliste.append(item)
            elif isinstance(item, Subset):
                subsetliste.append(item)
        types = [atom.typ for atom in atomliste]
        indexes = [i for (j, i) in sorted(zip(types, range(len(atomliste))))]
        names = [atomliste[i].name for i in indexes]
        indexes = [i for (j, i) in sorted(zip(names, indexes))]
        print(indexes)
        for i in indexes:
            strings.append(["", atomliste[i].__str__()])
            strings.append([""])
        for momentum in momentumliste:
            strings.append(["", str(momentum)])
        for bond in bondliste:
            strings.append(["", str(bond)])
        for face in faceliste:
            strings.append(["", str(face)])
        for subset in subsetliste:
            strings.append(["", str(subset)])
        return bp.block(strings)

    def add(self, item):
        if not (item in self.menge):
            self.menge.add(item)
            self.names.add(item.name)

    def __add__(self, right):
        if isinstance(right, geo.Dif):
            return Atomset({atom + right for atom in self.menge})
        elif isinstance(right, str):
            menge = set([])
            for item in self.menge:
                if isinstance(item, Atom):
                    menge.add(item + right)
                else:
                    menge.add(item)
            return Atomset(menge)

        elif isinstance(right, Atomset):
            return Atomset(self.menge.union(right.menge))
        else:
            return NotImplemented

    def __radd__(self, left):
        if isinstance(left, geo.Dif):
            return self + left
        else:
            return NotImplemented

    def __rpow__(self, left):
        assert isinstance(left, geo.Operator) \
            or isinstance(left, geo.Spacegroup), \
            "Argument must be of type Operator."
        if isinstance(left, geo.Operator):
            menge = set([])
            return Atomset({left ** item for item in self.menge})
        if isinstance(left, geo.Spacegroup):
            atomset = Atomset(set([]))
            for item in self.menge:
                for coset in left.liste_cosets:
                    new_item = coset ** item
                    new_item.name = atomset.nextname(new_item.name)
                    atomset.add(new_item)
            return atomset

    def nextname(self, name):
        if name in self.names:
            words = name.split('_')
            if words[-1].isdigit():
                return self.nextname('_'.join(words[:-1] + [str(int(words[-1])+1)]))
            else:
                return self.nextname(name + '_1')
        else:
            return name

    def __mod__(self, right):
        assert isinstance(right, geo.Transgen), \
            "I cannot take an object of type Atomset " \
            "modulo an object of type" % (type(right))
        atoms = set([])
        for atom in self.menge:
            atoms |= set([atom % right])
        return Atomset(atoms)

    def get_atom(self, atomname):
        for atom in self.menge:
            if atom.name == atomname:
                return atom
        return None

    def unpack_subsets(self):
        menge_new = set([])
        for item in self.menge:
            if not isinstance(item, Subset):
                menge_new.add(item)
            else:
                for subitem in item.atomset.menge:
                    subitem.name = item.name + '.' + subitem.name
                    menge_new.add(subitem)
                    
        return Atomset(menge_new)


class Subset(Drawable):
    def __init__(self, name, pos, menge):
        assert isinstance(name, str), \
            "First argument must be of type str."
        assert isinstance(pos, geo.Pos), \
            "Second argument must be of type cryspy.geo.Pos."
        assert isinstance(menge, set), \
            "Third argument must be of type set."
        for item in menge:
            assert isinstance(item, Atom) or isinstance(item, Momentum) \
                or isinstance(item, Bond) or isinstance(item, Face), \
                "Third argument must be a set of "\
                "objects of type Atom, Momentum, Bond or Face."
        Drawable.__init__(self, name, pos)
        self.atomset = Atomset(menge)
        self.has_hash = False
        self.hash = 0

    def __eq__(self, right):
        return hash(self) == hash(right)

    def __str__(self):
        return "Subset"

    def __rpow__(self, left):
        assert isinstance(left, geo.Symmetry) \
            or isinstance(left, geo.Transformation) \
            or isinstance(left, geo.Coset), \
            "Cannot apply object of type %s to object of type " \
            "cryspy.crystal.Subset."%(str(type(left)))
        if isinstance(left, geo.Symmetry):
            return Subset(self.name, left**self.pos,
                          {left ** item for item in self.atomset.menge})
        elif isinstance(left, geo.Transformation):
            return Subset(self.name, left**self.pos,
                          {left ** item for item in self.atomset.menge})
        elif isinstance(left, geo.Coset):
            pos = left ** self.pos
            correct = (pos - left.symmetry ** self.pos).to_Symmetry()
            return Subset(self.name, pos,
                          {correct ** (left.symmetry ** item)
                           for item in self.atomset.menge})
   
    def __mod__(self, right):
        assert isinstance(right, geo.Transgen), \
            "Cannot apply object of type %s to object of type " \
            "cryspy.crystal.Subset."%(str(type(left)))
        if isinstance(right, geo.Transgen):
            pos = self.pos % right
            correct = (pos - self.pos).to_Symmetry()
            return Subset(self.name, pos,
                          {correct ** item
                           for item in self.atomset.menge})


    def __add__(self, right):
        assert isinstance(right, geo.Dif) \
            or isinstance(right, str), \
            "Cannot add object of type %s to object of type Subset." \
            %(str(type(right)))
        if isinstance(right, geo.Dif):
            return right.to_Symmetry() ** self
        elif isinstance(right, str):
            return Subset(self.name + right, self.pos, self.atomset.menge)
        else:
            return NotImplemented



    def __hash__(self):
        print("hash")
        if self.has_hash:
            return self.hash
        else:
            print("neues hash")
            h = 0
            for item in self.atomset.menge:
                h += hash(item)
            string = "%s%i%i%i%i" % (
                "Subset",
                hash(self.pos.x()),
                hash(self.pos.y()),
                hash(self.pos.z()),
                h)
            ha = int(hashlib.sha1(string.encode()).hexdigest(), 16)
            self.hash = ha
            self.has_hash = True
            return ha

def structurefactor(atomset, metric, q, wavelength):
    assert isinstance(atomset, Atomset), \
        "atomset must be of type Atomset."
    assert isinstance(metric, geo.Metric), \
        "metric must be of type geo.Metric."
    assert isinstance(q, geo.Rec), \
        "q (scattering vector) must be of type geo.Rec."
    wavelength = nb.Mixed(wavelength)
    assert isinstance(wavelength, nb.Mixed), \
        "wavelength must be of type numbers.Mixed or a type " \
        "that can be converted to this."

    sintl = 0.5 * metric.length(q)
    i2pi = np.complex(0, 1) * 2.0 * np.pi
    F = 0
    for atom in atomset.menge:
        F += tables.formfactor(atom.typ, sintl) \
           * np.exp(i2pi * float(q * (atom.pos - geo.origin)))

    return F


