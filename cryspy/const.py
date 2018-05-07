blender__thickness_of_axis_shaft = 0.05
blender__num_of_segments_of_axis_shaft = 6  # 4...32: rough...fine
blender__thickness_of_axis_tip = 0.2
blender__height_of_axis_tip = 0.5
blender__num_of_segments_of_axis_tip = 24  # 4...32: rough...fine
blender__axes_color = (0, 0, 0)
blender__atom_icosphere_subdivisions = 3  # 1...4: rough...fine
blender__thickness_of_momentum_shaft = 0.1
blender__num_of_segments_of_momentum_shaft = 32  # 4...128: rough...fine
blender__thickness_of_momentum_tip = 0.3
blender__height_of_momentum_tip = 0.6
blender__num_of_segments_of_momentum_tip = 32  # 4...128: rough...fine
blender__std_momentum_plotlength = 1
blender__std_momentum_color = (0, 0, 1)
blender__thickness_of_bond_arrow_tip = 0.5
blender__height_of_bond_arrow_tip = 1.0
blender__num_of_segments_of_bond = 32 # 4...128: rough...fine
blender__std_bond_thickness = 0.05
blender__std_bond_color = (0.5, 0.5, 0.5)
blender__std_face_color = (0.7, 0.7, 0.7)
blender__std_face_opacity = 0.7 # 0: fully transparent, 1: fully opaque
blender__background_color = (1, 1, 1)
blender__location_of_lamp1 = (5, -5, 10)
blender__diffuse_light = 0.5

# Difference of the cases, whether you make segments 4 or 128,
# is for the *.blend-file a difference of ca. 50 KB per arrow.

povray__thickness_of_axis_shaft = blender__thickness_of_axis_shaft
povray__axes_color = blender__axes_color
povray__thickness_of_axis_tip = blender__thickness_of_axis_tip
povray__height_of_axis_tip = blender__height_of_axis_tip
povray__std_bond_thickness = blender__std_bond_thickness
povray__std_bond_color = blender__std_bond_color
povray__std_face_color = blender__std_face_color
povray__std_face_opacity = blender__std_face_opacity
povray__legend_spacing = 0.2 # spacing between legend atoms relativ to image height
povray__legend_horizontal_margin = 0.1 # spacing left of legend to egde relative to image width
povray__legend_vertical_margin = 0.2 # spacing below legend to edge relative to image height
povray__thickness_of_momentum_shaft = blender__thickness_of_momentum_shaft
povray__thickness_of_momentum_tip = blender__thickness_of_momentum_tip
povray__height_of_momentum_tip = blender__height_of_momentum_tip
povray__std_momentum_plotlength = blender__std_momentum_plotlength
povray__std_momentum_color = blender__std_momentum_color
povray__thickness_of_bond_arrow_tip = blender__thickness_of_bond_arrow_tip
povray__height_of_bond_arrow_tip = blender__height_of_bond_arrow_tip


