"""
DIGM 131 - Assignment 2: Procedural Pattern Generator
======================================================

OBJECTIVE:
    Use loops and conditionals to generate a repeating pattern of 3D objects
    in Maya. You will practice nested loops, conditional logic, and
    mathematical positioning.

REQUIREMENTS:
    1. Use a nested loop (a loop inside a loop) to create a grid or pattern
       of objects.
    2. Include at least one conditional (if/elif/else) that changes an
       object's properties (type, size, color, or position offset) based
       on its row, column, or index.
    3. Generate at least 25 objects total (e.g., a 5x5 grid).
    4. Comment every major block of code explaining your logic.

GRADING CRITERIA:
    - [25%] Nested loop correctly generates a grid/pattern of objects.
    - [25%] Conditional logic visibly changes object properties based on
            position or index.
    - [20%] At least 25 objects are generated.
    - [15%] Code is well-commented with clear explanations.
    - [15%] Pattern is visually interesting and intentional.

TIPS:
    - A 5x5 grid gives you 25 objects. A 6x6 grid gives you 36.
    - Use the loop variables (row, col) to calculate X and Z positions.
    - The modulo operator (%) is great for alternating patterns:
          if col % 2 == 0:    # every other column
    - You can vary: primitive type, height, width, position offset, etc.

COMMENT HABITS (practice these throughout the course):
    - Add a comment before each logical section explaining its purpose.
    - Use inline comments sparingly and only when the code is not obvious.
    - Keep comments up to date -- if you change the code, update the comment.
"""

import maya.cmds as cmds

cmds.file(new=True, force=True)

def generate_pattern():
    num_rows = 5
    num_cols = 5
    spacing = 3.0

    for row in range(num_rows):
        for col in range(num_cols):
            x_pos = col * spacing
            z_pos = row * spacing

         
            if (row + col) % 4 == 0:
                obj = cmds.polyCone(name="cone", radius=1.0, height=2.0)[0]
            else:
                obj = cmds.polySphere(name="sphere", radius=1.0)[0]

            cmds.move(x_pos, 0, z_pos, obj)
            
    orb_height = 9.0
    orb = cmds.polySphere(name="orb", radius=2.0)[0]

    cmds.move(0, orb_height / 2.0, 0, orb)

    actual_height = cmds.getAttr(orb + ".scaleY") * orb_height
    print("Orb height:", actual_height)

    if actual_height > 9.0:
        print("This orb is TALL (over 9 units).")
    else:
        print("This orb is SHORT (9 units or under).")

    cmds.move(3, 6, 0, orb)

    orb_x = cmds.getAttr(orb + ".translateX")
    orb_y = cmds.getAttr(orb + ".translateY")

    if orb_x > 0 and orb_y > 10:
        print("Orb is in the upper-right area of the scene.")

    if orb_x > 10 or orb_y > 10:
        print("Orb is far from the origin on at least one axis.")
    else:
        print("Orb is reasonably close to the origin.")

generate_pattern()

cmds.viewFit(allObjects=True)
print("Pattern generated successfully!")
