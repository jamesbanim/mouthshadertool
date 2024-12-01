# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 
# MOUTH SHADER TOOL (mouthShader_tool.py)
# Version 1.2.1 / 29/11/24
#
# Tool created by James Boyle (@JamesBAnim)
# Original idea inspired by Charles Icay (@IkHandle)
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# LICENSE MIT
#
# Copyright (c) 2024 James Boyle
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# INSTALLATION
# Copy this file into your maya scripts directory, for example:
#
# WIN - C:/Documents and Settings/user/My Documents/maya/scripts/mouthShader_tool.py
# MACOS - /Users/user/Library/Preferences/Autodesk/maya/scripts/mouthShader_tool.py
#
# Run the tool from python command line or shelf button by 
# importing the module, and then calling the primary function:
# 
#     import mouthShader_tool
#     mouthShader_tool.run()
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# ICON
# Copy the icon JPG (mouthShader_tool.jpg) to the icon folder in your maya prefs, for example:
#
# WIN - C:/Documents and Settings/user/My Documents/maya/2024/prefs/icons/mouthShader_tool.jpg
# MACOS - /Users/name/Library/Preferences/Autodesk/maya/2024/prefs/icons/mouthShader_tool.jpg
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# COMPATIBILITY
# Python 3
# Maya 2022 - 2024
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# DESCRIPTION
# This tool creates a simple gradient shader material and assigns it to a plane. 
# The plane can be placed at the back of a characters mouth (behind the tongue), 
# to help create depth when the mouth is open.
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import maya.cmds as cmds
import maya.OpenMaya as om

__author__ = 'James Boyle'
__license__ = 'MIT'
__version__ = '1.2.1'

title = 'Mouth Shader Tool'
version = 'v1.2.1'
status = 'release'
date = '29/11/24'
height = 100
width = 180
shader_color = (0, 0, 0)
ramp_start = 0.1
ramp_end = 0.7
maintain_offset = False
current_selection = None

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Define groups for parenting
groups = [
    'mouthShader_GRP_01',
    'mouthShader_GRP_02',
    'mouthShader_GRP_03',
    'mouthShader_GRP_04',
    'mouthShader_GRP_05',
    'mouthShader_GRP_06',
    'mouthShader_GRP_07',
]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def run():
    create_ui('Mouth Shader Tool')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Store the current selection
current_selection = cmds.ls(selection=True)
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Get current viewport list, turn on textures and smooth shading
def update_textures():
    
    for vp in cmds.getPanel(type="modelPanel"):
        # check if current viewport.
        if cmds.modelEditor(vp, query=True, activeView=True):
            cmds.modelEditor(vp, edit=True, displayAppearance="smoothShaded")
            cmds.modelEditor(vp, edit=True, displayTextures=True)
            break

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def create_plane_and_shader(*args):
    global current_selection

    if cmds.objExists('mouthShader_GRP_01'):
        om.MGlobal.displayWarning('Shader already exists, add additional?')

    elif not cmds.objExists('mouthShader_GRP_01') and cmds.objExists('mouthShader_mtlSG'):
        attach_plane_and_shader()

    else:
        # Store the current selection
        current_selection = cmds.ls(selection=True)

        # Create a plane
        cmds.polyPlane(name='mouthShader_geo_01')

        # Set attributes on the plane
        cmds.setAttr('mouthShader_geo_01.scaleY', 4)
        cmds.setAttr('mouthShader_geo_01.scaleX', 4)
        cmds.setAttr('mouthShader_geo_01.scaleZ', 4)
        cmds.setAttr('polyPlane1.subdivisionsHeight', 5)
        cmds.setAttr('polyPlane1.subdivisionsWidth', 5)

        # Group the plane
        cmds.group('mouthShader_geo_01', name='mouthShader_GRP_01')

        # Select the plane
        cmds.select("mouthShader_geo_01", replace=True)

        # Create material
        cmds.shadingNode('lambert', name="mouthShader_mtl", asShader=True)

        # Create shading group
        cmds.sets(renderable=True, empty=True, noSurfaceShader=True, name='mouthShader_mtlSG')

        # Connect the shader's outColor to the shading group's surfaceShader attribute
        cmds.connectAttr('mouthShader_mtl.outColor', 'mouthShader_mtlSG.surfaceShader', force=True)

        # Assign shading group to plane
        cmds.sets('mouthShader_geo_01', e=True, forceElement='mouthShader_mtlSG')

        # Set shader color to black
        cmds.setAttr("mouthShader_mtl.color", *shader_color, type='double3')
      
        # Create ramp texture and place2dTexture utility
        ramp = cmds.shadingNode('ramp', asTexture=True, name='rampMS')
        place2d = cmds.shadingNode('place2dTexture', asUtility=True, name='place2dTextureMS')

        # Connect place2dTexture to ramp's UV inputs
        cmds.connectAttr(f'{place2d}.outUV', f'{ramp}.uvCoord')
        cmds.connectAttr(f'{place2d}.outUvFilterSize', f'{ramp}.uvFilterSize')

        # Connect the ramp's outColor to the material's transparency
        cmds.connectAttr(f'{ramp}.outColor', 'mouthShader_mtl.transparency', force=True)

        # Set ramp transparency attributes
        cmds.setAttr('rampMS.type', 4)
        cmds.setAttr('rampMS.interpolation', 4)
        cmds.setAttr('rampMS.colorEntryList[0].color', 0, 0, 0, type='double3')
        cmds.setAttr('rampMS.colorEntryList[0].position', ramp_start)
        cmds.setAttr('rampMS.colorEntryList[1].color', 1, 1, 1, type='double3')
        cmds.setAttr('rampMS.colorEntryList[1].position', ramp_end)

        current_selection = cmds.select(clear=True)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def attach_plane_and_shader(*args):
    # Store the current selection
    current_selection = cmds.ls(selection=True)

    # Create a plane
    cmds.polyPlane(name='mouthShader_geo_01')

    # Set attributes on the plane
    cmds.setAttr('mouthShader_geo_01.scaleY', 4)
    cmds.setAttr('mouthShader_geo_01.scaleX', 4)
    cmds.setAttr('mouthShader_geo_01.scaleZ', 4)
    cmds.setAttr('polyPlane1.subdivisionsHeight', 5)
    cmds.setAttr('polyPlane1.subdivisionsWidth', 5)

    # Group the plane
    cmds.group('mouthShader_geo_01', name='mouthShader_GRP_01')

    # Select the plane
    cmds.select("mouthShader_geo_01", replace=True)

    # Assign shading group to plane
    cmds.sets('mouthShader_geo_01', e=True, forceElement='mouthShader_mtlSG')

    current_selection = cmds.select(clear=True)
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# # Duplicate plane with shader
def duplicate_plane(*args):
    if not cmds.objExists('mouthShader_GRP_01'):
        create_plane_and_shader()
    else:
        new_group = cmds.duplicate('mouthShader_GRP_01', upstreamNodes=False, inputConnections=False, renameChildren=True)
        
        new_con = cmds.listRelatives(new_group, type='constraint', allDescendents=True)
        
        print("Existing constraints:", new_con)

        cmds.delete(new_con)        

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Parent shader group to selected control
def parent_shader_to_control(*args):
    # Query the current selection, store in list
    current_selection = cmds.ls(selection=True)
    
    # Currest selecion list is empty
    if not current_selection:
        om.MGlobal.displayWarning('No objects selected. Select control and group to parent.')
        return

    # Check if at least one group exists
    if not any(cmds.objExists(group) for group in groups):
        om.MGlobal.displayWarning('Add mouth shader before parenting.')
        return

    # Check if any of the groups are in the current selection
    selected_groups = [group for group in groups if group in current_selection]
    
    # If groups aren't in selected groups
    if not selected_groups:
        om.MGlobal.displayWarning('No matching groups in selection. Select control and group to parent.')
        return

    # Apply parent constraint for matching groups
    for group in selected_groups:
        try:
            cmds.parentConstraint(current_selection[0], group, maintainOffset=maintain_offset)
            om.MGlobal.displayInfo(f'Parent constraint applied between {current_selection[0]} and {group}.')
        except Exception as e:
            om.MGlobal.displayError(f'Failed to apply parent constraint for {group}: {e}')
                
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Update parent constraint offset variable
def toggle_parent_offset(value):
    global maintain_offset
    maintain_offset = value

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Store and change shader default color
def on_color_change(*args):
    # Query the current color from the slider
    current_color = cmds.colorSliderGrp('colorSlider', q=True, rgb=True)
    print(f"Color Picked: {current_color}")
    
    # Update shader color dynamically
    if cmds.objExists("mouthShader_mtl"):
        cmds.setAttr("mouthShader_mtl.color", *current_color, type="double3")
        print(f"Updated shader color to: {current_color}")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Store and change ramp start and end positions
def on_ramp_start_change(value):
    if cmds.objExists('rampMS.colorEntryList[0].position'):
        cmds.setAttr('rampMS.colorEntryList[0].position', value)

def on_ramp_end_change(value):
    if cmds.objExists('rampMS.colorEntryList[1].position'):
        cmds.setAttr('rampMS.colorEntryList[1].position', value)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Create UI
def create_ui(window_name):

    # update viewport with textures
    update_textures()
    
    # Check if window exists
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name)
        
    # Create window
    window = cmds.window(window_name,
                title=(f'{title}'),
                toolbox=True,
                sizeable=False,
                height=height,
                width=width)

    # Create main layout     
    main_layout = cmds.columnLayout(adjustableColumn=True,
                    columnAttach=('both', 0),
                    rowSpacing=1,
                    parent=window)

    # Button - Create shader material    
    cmds.iconTextButton(label='Add Mouth Shader Group',
                        style='iconAndTextHorizontal',
                        image1='material_assign.png',
                        align='left',
                        marginWidth=10,
                        height=35,
                        backgroundColor=[0.4, 0.4, 0.4],
                        command=create_plane_and_shader,
                        parent=main_layout)

    # Button - Additional shader material    
    cmds.iconTextButton(label='Add Additional Group',
                        style='iconAndTextHorizontal',
                        image1='material_create.png',
                        align='left',
                        marginWidth=10,
                        height=35,
                        backgroundColor=[0.4, 0.4, 0.4],
                        command=duplicate_plane,
                        parent=main_layout)

    # Button - Parent group to selected
    cmds.iconTextButton(label='Parent Shader to Selected',
                        style='iconAndTextHorizontal',
                        image1='parentConstraint.png',
                        align='left',
                        marginWidth=9.5,
                        height=38,
                        backgroundColor=[0.4, 0.4, 0.4],
                        command=parent_shader_to_control,
                        parent=main_layout)     
            
    cmds.checkBoxGrp('offsetCheck',
                        label='Maintain Offset: ',
                        columnAlign2=('right', 'left'),
                        columnAttach2=('left', 'left'),
                        columnWidth2=[134,46],
                        height=25,
                        backgroundColor=[0.3, 0.3, 0.3],
                        value1=maintain_offset,
                        changeCommand=toggle_parent_offset,
                        parent=main_layout)

    cmds.separator(style='in', parent=main_layout)

    # Create slider layout
    slider_layout = cmds.columnLayout(adjustableColumn=True,
                                    columnAttach=('both', 0),
                                    rowSpacing=4,
                                    parent=window)
    
    # Change shader color - Create ramp color slider
    cmds.colorSliderGrp('colorSlider',
                        label='Color: ',
                        rgb=shader_color,
                        columnAlign3=('right', 'left', 'left'),
                        columnAttach3=('left', 'left', 'left'),
                        columnWidth3=[50,60,70],
                        changeCommand=on_color_change,
                        parent=slider_layout)

    # Adjust ramp posistion - Create ramp slider start
    cmds.floatSliderGrp('rampStart',
                        label='Start: ',
                        field=True,
                        minValue=0.0,
                        maxValue=1.0,
                        fieldMinValue=0.0,
                        fieldMaxValue=1.0,
                        value=ramp_start,
                        columnAlign3=('right', 'left', 'left'),
                        columnAttach3=('left', 'left', 'left'),
                        columnWidth3=[50,60,70],
                        dragCommand=on_ramp_start_change,
                        parent=slider_layout)

    # Create ramp slider end
    cmds.floatSliderGrp('rampEnd',
                        label='End: ',
                        field=True,
                        minValue=0.0,
                        maxValue=1.0,
                        fieldMinValue=0.0,
                        fieldMaxValue=1.0,
                        value=ramp_end,
                        columnAlign3=('right', 'left', 'left'),
                        columnAttach3=('left', 'left', 'left'),
                        columnWidth3=[50,60,70],
                        dragCommand=on_ramp_end_change,
                        parent=slider_layout)

    # Create bottom layout
    btm_layout = cmds.columnLayout(adjustableColumn=True,
                    columnAttach=('both', 0),
                    backgroundColor=[0.2, 0.2, 0.2],
                    height=23,
                    parent=window)

    # Seperator
    cmds.separator(style='in',
                parent=btm_layout)

    # Version, status and date
    cmds.text(f'{version}  /  {status}  /  {date}',
            font='smallObliqueLabelFont',
            parent=btm_layout)

    # Show UI
    cmds.showWindow(window)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
if __name__ == "__main__":
    create_ui('Mouth Shader Tool')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# REVISIONS
#
# Revision 0: 28/11/24 : First release
#
# Revision 1: 29/11/24 : Fix Parent Constraint bug. Small wording changes. Small UI fixes.
