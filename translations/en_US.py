dictionary = {
    # Class.label / Class.desc (tooltip)
    # Class.property

    # Language name
    'name': 'en_US',

    # Main file
    'Main.error.restartAdmin': '\n\nFaulty CATS installation found!'
                               '\nTo fix this restart Blender as admin!     '
                               '\n',
    'Main.error.deleteFollowing': '                                                                                                                                                                                    '
                                  '                     '
                                  '\n\nFaulty CATS installation found!'
                                  '\nTo fix this delete the following files and folders inside your addons folder:'
                                  '\n',
    'Main.error.installViaPreferences': '\n\nFaulty CATS installation found!'
                                        '\nPlease install CATS via User Preferences and restart Blender!'
                                        '\n',
    'Main.error.restartAndEnable': '\n\nFaulty CATS installation was found and fixed!'
                                   '\nPlease restart Blender and enable CATS again!'
                                   '\n',
    'Main.error.unsupportedVersion': '\n\nBlender versions older than 2.79 are not supported by Cats. '
                                     '\nPlease use Blender 2.79 or later.'
                                     '\n',
    'Main.error.beta2.80': '\n\nYou are still on the beta version of Blender 2.80!'
                           '\nPlease update to the release version of Blender 2.80.'
                           '\n',
    'Main.error.restartAndEnable_alt': '\n\nPlease restart Blender and enable CATS again!'
                                       '\n',

    # UI Main
    'ToolPanel.label': 'Cats Blender Plugin',
    'ToolPanel.category': 'CATS',

    # UI Armature
    'ArmaturePanel.label': 'Model',
    'ArmaturePanel.warn.oldBlender1': 'Old Blender version detected!',
    'ArmaturePanel.warn.oldBlender2': 'Some features might not work!',
    'ArmaturePanel.warn.oldBlender3': 'Please update to Blender 2.79!',
    'ArmaturePanel.warn.noDict1': 'Dictionary not found!',
    'ArmaturePanel.warn.noDict2': 'Translations will work, but are not optimized.',
    'ArmaturePanel.warn.noDict3': 'Reinstall Cats to fix this.',
    'ArmaturePanel.ImportAnyModel.label': 'Import Model',
    'ModelSettings.label': 'Fix Model Settings',
    'ModelSettings.warn.fbtFix1': 'The Full Body Tracking Fix',
    'ModelSettings.warn.fbtFix2': 'is no longer needed for VRChat.',
    'ModelSettings.warn.fbtFix3': 'It\'s still available in Model Options.',

    # UI Manual
    'ManualPanel.label': 'Model Options',
    'ManualPanel.separateBy': 'Separate by:',
    'ManualPanel.SeparateByMaterials.label': 'Materials',
    'ManualPanel.SeparateByLooseParts.label': 'Loose Parts',
    'ManualPanel.SeparateByShapekeys.label': 'Shapes',
    'ManualPanel.joinMeshes': 'Join Meshes:',
    'ManualPanel.JoinMeshes.label': 'All',
    'ManualPanel.JoinMeshesSelected.label': 'Selected',
    'ManualPanel.mergeWeights': 'Merge Weights:',
    'ManualPanel.MergeWeights.label': 'To Parents',
    'ManualPanel.MergeWeightsToActive.label': 'To Active',
    'ManualPanel.translate': 'Translate:',
    'ManualPanel.TranslateAllButton.label': 'All',
    'ManualPanel.TranslateShapekeyButton.label': 'Shape Keys',
    'ManualPanel.TranslateObjectsButton.label': 'Objects',
    'ManualPanel.TranslateBonesButton.label': 'Bones',
    'ManualPanel.TranslateMaterialsButton.label': 'Materials',
    'ManualPanel.delete': 'Delete:',
    'ManualPanel.RemoveZeroWeightBones.label': 'Zero Weight Bones',
    'ManualPanel.RemoveConstraints': 'Constraints',
    'ManualPanel.RemoveZeroWeightGroups': 'Zero Weight Vertex Groups',
    'ManualPanel.normals': 'Normals:',
    'ManualPanel.RecalculateNormals.label': 'Recalculate',
    'ManualPanel.FlipNormals.label': 'Flip',
    'ManualPanel.fbtFix': 'Full Body Tracking Fix:',
    'ManualPanel.FixFBTButton.label': 'Add',
    'ManualPanel.RemoveFBTButton.label': 'Remove',

    # UI Custom
    'CustomPanel.label': 'Custom Model Creation',
    'CustomPanel.CustomModelTutorialButton': 'How to use',
    'CustomPanel.mergeArmatures': 'Merge Armatures:',
    'CustomPanel.warn.twoArmatures': 'Two armatures are required!',
    'CustomPanel.mergeInto': 'Base',
    'CustomPanel.toMerge': 'To Merge',
    'CustomPanel.attachToBone': 'Attach to',
    'CustomPanel.armaturesCanMerge': 'Armatures can be merged automatically!',
    'CustomPanel.attachMesh1': 'Attach Mesh to Armature:',
    'CustomPanel.attachMesh2': 'Mesh',
    'CustomPanel.warn.noArmOrMesh1': 'An armature and a mesh are required!',
    'CustomPanel.warn.noArmOrMesh2': 'Make sure that the mesh has no parent.',

    # UI Decimation
    'DecimationPanel.label': 'Decimation',
    'DecimationPanel.decimationMode': 'Decimation Mode:',
    'DecimationPanel.safeModeDesc': ' Decent results - No shape key loss',
    'DecimationPanel.halfModeDesc': ' Good results - Minimal shape key loss',
    'DecimationPanel.fullModeDesc': ' Consistent results - Full shape key loss',
    'DecimationPanel.smartModeDesc': ' Best results - Preserve shape keys',
    'DecimationPanel.customSeparateMaterials': 'Start by Separating by Materials:',
    'DecimationPanel.SeparateByMaterials.label': 'Separate by Materials',
    'DecimationPanel.customJoinMeshes': 'Stop by Joining Meshes:',
    'DecimationPanel.customWhitelist': 'Whitelisted:',
    'DecimationPanel.warn.noShapekeySelected': 'No shape key selected',
    'DecimationPanel.warn.noDecimation': 'Every mesh is selected. This equals no Decimation.',
    'DecimationPanel.warn.noMeshSelected': 'No mesh selected',
    'DecimationPanel.warn.emptyList': 'Both lists are empty, this equals Full Decimation!',
    'DecimationPanel.warn.correctWhitelist': 'Both whitelists are considered during decimation',
    'DecimationPanel.preset.excellent.label': 'Excellent',
    'DecimationPanel.preset.excellent.description': 'The maximum number of tris you can have for an Excellent rating.',
    'DecimationPanel.preset.good.label': 'Good',
    'DecimationPanel.preset.good.description': 'The maximum number of tris you can have for a Good rating.',
    'DecimationPanel.preset.quest.label': 'Quest',
    'DecimationPanel.preset.quest.description': 'The recommended number of tris for Quest avatars.\n'
                                                'A hard limit will be established in the future that will not be much more than this.',

    # UI Eye tracking
    'EyeTrackingPanel.label': 'Eye Tracking',
    'EyeTrackingPanel.error.noMesh': 'No meshes found!',
    'EyeTrackingPanel.error.noArm': 'No model found!',
    'EyeTrackingPanel.error.wrongNameArm1': 'Your armature has to be named \'Armature\'',
    'EyeTrackingPanel.error.wrongNameArm2': '      for Eye Tracking to work!',
    'EyeTrackingPanel.error.wrongNameArm3': '      (currently \'',
    'EyeTrackingPanel.error.wrongNameBody1': 'The mesh containing the eyes has to be',
    'EyeTrackingPanel.error.wrongNameBody2': '      named \'Body\' for Eye Tracking to work!',
    'EyeTrackingPanel.error.wrongNameBody3': '      (currently \'',
    'EyeTrackingPanel.warn.assignEyes1': 'Don\'t forget to assign \'LeftEye\' and \'RightEye\'',
    'EyeTrackingPanel.warn.assignEyes2': '      to the eyes in Unity!',

    # UI Visemes
    'VisemePanel.label': 'Visemes',
    'VisemePanel.error.noMesh': 'No meshes found!',

    # UI Bone_root
    'BoneRootPanel.label': 'Bone Parenting',

    # UI Optimization
    'OptimizePanel.label': 'Optimization',
    'OptimizePanel.atlasDesc': 'A greatly improved Atlas Generator.',
    'OptimizePanel.atlasAuthor': 'Made by Shotariya',
    'OptimizePanel.matCombDisabled1': 'Material Combiner is not enabled!',
    'OptimizePanel.matCombDisabled2': 'Enable it in your user preferences:',
    'OptimizePanel.matCombOutdated1': 'Your Material Combiner is outdated!',
    'OptimizePanel.matCombOutdated2': 'Please update to the latest version.',
    'OptimizePanel.matCombOutdated3': 'Update via the \'Updates\' panel',
    'OptimizePanel.matCombOutdated4': 'in the \'MatCombiner\' tab to the {location}',
    'OptimizePanel.matCombOutdated5_2.79': 'left.',
    'OptimizePanel.matCombOutdated5_2.8': 'right.',
    'OptimizePanel.matCombOutdated6': 'Or download and install it manually:',
    'OptimizePanel.matCombOutdated6_alt': 'Download and install it manually:',
    'OptimizePanel.matCombNotInstalled': 'Material Combiner is not installed!',

    # UI Copy protection
    'CopyProtectionPanel.label': 'Copy Protection',
    'CopyProtectionPanel.desc1': 'Tries to protect your avatar from Unity cache ripping.',
    'CopyProtectionPanel.desc2': 'This protection is not 100% safe!',
    'CopyProtectionPanel.desc3': 'Before use: Read the documentation!',

    # UI Settings & Updates
    'UpdaterPanel.label': 'Settings & Updates',
    'UpdaterPanel.name': 'Settings:',
    'UpdaterPanel.requireRestart1': 'Restart required.',
    'UpdaterPanel.requireRestart2': 'Some changes require a Blender restart.',

    # UI Supporter
    'SupporterPanel.label': 'Supporters',
    'SupporterPanel.desc': 'Do you like this plugin and want to support us?',
    'SupporterPanel.thanks': 'Thanks to our awesome supporters! <3',
    'SupporterPanel.missingName1': 'Is your name missing?',
    'SupporterPanel.missingName2': '     Please contact us in our discord!',

    # UI Credits
    'CreditsPanel.label': 'Credits',
    'CreditsPanel.desc1': 'Cats Blender Plugin (',
    'CreditsPanel.desc2': 'Created by Hotox and GiveMeAllYourCats',
    'CreditsPanel.desc3': 'For the awesome VRChat community <3',
    'CreditsPanel.desc4': 'Special thanks to: Shotariya and Neitri',
    'CreditsPanel.desc5': 'Do you need help or found a bug?',

    # Tools Armature
    'FixArmature.label': 'Fix Model',
    'FixArmature.desc': 'Automatically:\n'
                        '- Reparents bones\n'
                        '- Removes unnecessary bones, objects, groups & constraints\n'
                        '- Translates and renames bones & objects\n'
                        '- Merges weight paints\n'
                        '- Corrects the hips\n'
                        '- Joins meshes\n'
                        '- Converts morphs into shapes\n'
                        '- Corrects shading',
    'FixArmature.error.noMesh': ['No mesh inside the armature found!',
                                 'If there are meshes outside of the armature,',
                                 'set the armature as the parent of the meshes.'],
    # Format strings? vvvv t(str, fixed_uv_coords) -> The model was successfully fixed, but there were {} faulty UV
    'FixArmature.error.faultyUV1': 'The model was successfully fixed, but there were {uvcoord} faulty UV coordinates.',
    # 'The model was successfully fixed, but there were ' + str(fixed_uv_coords) + ' faulty UV coordinates.',
    'FixArmature.error.faultyUV2': 'This could result in broken textures and you might have to fix them manually.',
    'FixArmature.error.faultyUV3': 'This issue is often caused by edits in PMX editor.',
    'FixArmature.fixedSuccess': 'Model successfully fixed.',
    'FixArmature.bonesNotFound': 'The following bones were not found:',
    'FixArmature.cantFix1': 'Looks like you found a model which Cats could not fix!',
    'FixArmature.cantFix2': 'If this is a non modified model we would love to make it compatible.',
    'FixArmature.cantFix3': 'Report it to us in the forum or in our discord, links can be found in the Credits panel.',
    'FixArmature.notParent': ' is not parented at all, this will cause problems!',
    'FixArmature.notParentTo1': ' is not parented to ',
    'FixArmature.notParentTo2': ', this will cause problems!',

    # Tools Armature Manual
    'StartPoseMode.label': 'Start Pose Mode',
    'StartPoseMode.desc': 'Starts the pose mode.\n'
                          'This lets you test how your model will move',

    'StopPoseMode.label': 'Stop Pose Mode',
    'StopPoseMode.desc': 'Stops the pose mode and resets the pose to normal',

    'PoseToShape.label': 'Pose to Shape Key',
    'PoseToShape.desc': 'This saves your current pose as a new shape key.'
                        '\nThe new shape key will be at the bottom of your shape key list of the mesh',

    'PoseNamePopup.label': 'Give this shapekey a name:',
    'PoseNamePopup.desc': 'Sets the shapekey name. Press anywhere outside to skip',
    'PoseNamePopup.success': 'Pose successfully saved as shape key.',

    'PoseToRest.label': 'Apply as Rest Pose',
    'PoseToRest.desc': 'This applies the current pose position as the new rest position.'
                       '\n'
                       '\nIf you scale the bones equally on each axis the shape keys will be scaled correctly as well!'
                       '\nWARNING: This can have unwanted effects on shape keys, so be careful when modifying the head with this',
    'PoseToRest.success': 'Pose successfully applied as rest pose.',

    'JoinMeshes.label': 'Join Meshes',
    'JoinMeshes.desc': 'Joins all meshes of this model together.'
                       '\nIt also:'
                       '\n  - Reorders all shape keys correctly'
                       '\n  - Applies all transforms'
                       '\n  - Repairs broken armature modifiers'
                       '\n  - Applies all decimation and mirror modifiers'
                       '\n  - Merges UV maps correctly',
    'JoinMeshes.failure': 'Meshes could not be joined!',
    'JoinMeshes.success': 'Meshes joined.',

    'JoinMeshesSelected.label': 'Join Selected Meshes',
    'JoinMeshesSelected.desc': 'Joins all selected meshes of this model together.'
                               '\nIt also:'
                               '\n  - Reorders all shape keys correctly'
                               '\n  - Applies all transforms'
                               '\n  - Repairs broken armature modifiers'
                               '\n  - Applies all decimation and mirror modifiers'
                               '\n  - Merges UV maps correctly',
    'JoinMeshesSelected.error.noSelect': 'No meshes selected! Please select the meshes you want to join in the hierarchy!',
    'JoinMeshesSelected.error.cantJoin': 'Selected meshes could not be joined!',
    'JoinMeshesSelected.success': 'Selected meshes joined.',

    'SeparateByMaterials.label': 'Separate by Materials',
    'SeparateByMaterials.desc': 'Separates selected mesh by materials.\n'
                                '\n'
                                'Warning: Never decimate something where you might need the shape keys later (face, mouth, eyes..)',
    'SeparateByMaterials.success': 'Successfully separated by materials.',

    'SeparateByLooseParts.label': 'Separate by Loose Parts',
    'SeparateByLooseParts.desc': 'Separates selected mesh by loose parts.\n'
                                 'This acts like separating by materials but creates more meshes for more precision',
    'SeparateByLooseParts.success': 'Successfully separated by loose parts.',

    'SeparateByShapekeys.label': 'Separate by Shape Keys',
    'SeparateByShapekeys.desc': 'Separates selected mesh into two parts,'
                                '\ndepending on whether it is effected by a shape key or not.'
                                '\n'
                                '\nVery useful for manual decimation',
    'SeparateByShapekeys.success': 'Successfully separated by shape keys.',

    'SeparateByCopyProtection.label': 'Separate by Copy Protection',
    'SeparateByCopyProtection.desc': 'Separates selected mesh into two parts,'
                                     '\ndepending on whether it is effected by the Cats Copy Protection or not.'
                                     '\n'
                                     '\nUseful if you have the Copy Protection enabled on multiple selected parts of your model',
    'SeparateByCopyProtection.success': 'Successfully separated by shape keys.',

    'SeparateByX.error.noMesh': 'No meshes found!',
    'SeparateByX.error.multipleMesh': 'Multiple meshes found!'
                                      '\nPlease select the mesh you want to separate!',
    'SeparateByX.warn.noSeparation': 'No meshes had to be separated!',

    'MergeWeights.label': 'Merge Weights to Parent',
    'MergeWeights.desc': 'Deletes the selected bones and adds their weight to their respective parents.'
                         '\n'
                         '\nOnly available in Edit or Pose Mode with bones selected',
    'MergeWeights.success': 'Deleted {number} bones and added their weights to their parents.',

    'MergeWeightsToActive.label': 'Merge Weights to Active',
    'MergeWeightsToActive.desc': 'Deletes the selected bones except the active one and adds their weights to the active bone.'
                                 '\nThe active bone is the one you selected last.'
                                 '\n'
                                 '\nOnly available in Edit or Pose Mode with bones selected',
    'MergeWeightsToActive.success': 'Deleted {number} bones and added their weights to the active bone.',

    'ApplyTransformations.label': 'Apply Transformations',
    'ApplyTransformations.desc': 'Applies the position, rotation and scale to the armature and it\'s meshes',
    'ApplyTransformations.success': 'Transformations applied.',

    'ApplyAllTransformations.label': 'Apply All Transformations',
    'ApplyAllTransformations.desc': 'Applies the position, rotation and scale of all objects',
    'ApplyAllTransformations.success': 'Transformations applied.',

    'RemoveZeroWeightBones.label': 'Remove Zero Weight Bones',
    'RemoveZeroWeightBones.desc': 'Cleans up the bones hierarchy, deleting all bones that don\'t directly affect any vertices\n'
                                  'Don\'t use this if you plan to use \'Fix Model\'',
    'RemoveZeroWeightBones.success': 'Deleted {number} zero weight bones.',

    'RemoveZeroWeightGroups.label': 'Remove Zero Weight Vertex Groups',
    'RemoveZeroWeightGroups.desc': 'Cleans up the vertex groups of all meshes, deleting all groups that don\'t directly affect any vertices',
    'RemoveZeroWeightGroups.success': 'Removed {number} zero weight vertex groups.',

    'RemoveConstraints.label': 'Remove Bone Constraints',
    'RemoveConstraints.desc': 'Removes constrains between bones causing specific bone movement as these are not used by VRChat',
    'RemoveConstraints.success': 'Removed all bone constraints.',

    'RecalculateNormals.label': 'Recalculate Normals',
    'RecalculateNormals.desc': 'Makes normals point inside of the selected mesh.\n\n'
                               'Don\'t use this on good looking meshes as this can screw them up.\n'
                               'Use this if there are random inverted or darker faces on the mesh',
    'RecalculateNormals.success': 'Recalculated all normals.',

    'FlipNormals.label': 'Flip Normals',
    'FlipNormals.desc': 'Flips the direction of the faces\' normals of the selected mesh.\n'
                        'Use this if all normals are inverted',
    'FlipNormals.success': 'Flipped all normals.',

    'RemoveDoubles.label': 'Remove Doubles',
    'RemoveDoubles.desc': 'Merges duplicated faces and vertices of the selected meshes.'
                          '\nThis is more safe than doing it manually:'
                          '\n  - leaves shape keys completely untouched'
                          '\n  - but removes less doubles overall',
    'RemoveDoubles.success': 'Removed {number} vertices.',

    'RemoveDoublesNormal.label': 'Remove Doubles Normally',
    'RemoveDoublesNormal.desc': 'Merges duplicated faces and vertices of the selected meshes.'
                                '\nThis is exactly like doing it manually',
    'RemoveDoublesNormal.success': 'Removed {number} vertices.',

    'FixVRMShapesButton.label': 'Fix Koikatsu Shapekeys',
    'FixVRMShapesButton.desc': 'Fixes the shapekeys of Koikatsu models',
    'FixVRMShapesButton.warn.notDetected': 'No shapekeys detected!',
    'FixVRMShapesButton.success': 'Fixed VRM shapekeys.',

    'FixFBTButton.label': 'Fix Full Body Tracking',
    'FixFBTButton.desc': 'WARNING: This fix is no longer needed for VRChat, you should not use it!'
                         '\n'
                         '\nApplies a general fix for Full Body Tracking.'
                         '\nIgnore the \"Spine length zero\" warning in Unity',
    'FixFBTButton.error.bonesNotFound': 'Required bones could not be found!'
                                        '\nPlease make sure that your armature contains the following bones:'
                                        '\n - Hips, Spine, Left leg, Right leg'
                                        '\nExact names are required!',
    'FixFBTButton.error.alreadyApplied': 'Full Body Tracking Fix already applied!',
    'FixFBTButton.success': 'Successfully applied the Full Body Tracking fix.',

    'RemoveFBTButton.label': 'Remove Full Body Tracking Fix',
    'RemoveFBTButton.desc': 'Removes the fix for Full Body Tracking, since it is no longer advised to use it.'
                            '\n'
                            '\nRequires bones:'
                            '\n - Hips, Spine, Left leg, Right leg, Left leg 2, Right leg 2',
    'RemoveFBTButton.error.bonesNotFound': 'Required bones could not be found!'
                                           '\nPlease make sure that your armature contains the following bones:'
                                           '\n - Hips, Spine, Left leg, Right leg, Left leg 2, Right leg 2'
                                           '\nExact names are required!',
    'RemoveFBTButton.error.notApplied': 'The Full Body Tracking Fix is not applied!',
    'RemoveFBTButton.success': 'Successfully removed the Full Body Tracking fix.',

    'DuplicateBonesButton.label': 'Duplicate Bones',
    'DuplicateBonesButton.desc': 'Duplicates the selected bones including their weight and renames them to _L and _R',
    'DuplicateBonesButton.success': 'Successfully duplicated {number} bones.',

    # Tools Armature Custom
    'MergeArmature.label': 'Merge Armatures',
    'MergeArmature.desc': 'Merges the selected merge armature into the base armature.'
                          '\nYou should fix both armatures with Cats first.'
                          '\nOnly move the mesh of the merge armature to the desired position, the bones will be moved automatically',
    'MergeArmature.error.notFound': 'The armature "{name}" could not be found.',
    'MergeArmature.error.checkTransforms': ['Please make sure that the parent of the merge armature has the following transforms:',
                                            ' - Location at 0',
                                            ' - Rotation at 0',
                                            ' - Scale at 1'],
    'MergeArmature.error.pleaseFix': ['Please use the "Fix Model" feature on the selected armatures first!',
                                      'Make sure to select the armature you want to fix above the "Fix Model" button!',
                                      'After that please only move the mesh (not the armature!) to the desired position.'],
    'MergeArmature.success': 'Armatures successfully joined.',

    'AttachMesh.label': 'Attach Mesh',
    'AttachMesh.desc': 'Attaches the selected mesh to the selected bone of the selected armature.'
                       '\n'
                       '\nINFO: The mesh will only be assigned to the selected bone.'
                       '\nE.g.: A jacket won\'t work, because it requires multiple bones',
    'AttachMesh.success': 'Mesh successfully attached to armature.',

    'CustomModelTutorialButton.label': 'Go to Documentation',
    'CustomModelTutorialButton.URL': 'https://github.com/michaeldegroot/cats-blender-plugin#custom-model-creation',  # BOOM, now we can point at the Japanese link now ;)
    'CustomModelTutorialButton.success': 'Documentation',

    'merge_armatures.error.transformReset': ['If you want to rotate the new part, only modify the mesh instead of the armature,',
                                             'or select "Apply Transforms"!',
                                             '',
                                             'The transforms of the merge armature got reset and the mesh you have to modify got selected.',
                                             'Now place this selected mesh where and how you want it to be and then merge the armatures again.',
                                             'If you don\'t want that, undo this operation.'],
    'merge_armatures.error.pleaseUndo': ['Something went wrong! Please undo, check your selections and try again.'],

    # Tools Atlas
    'EnableSMC.label': 'Enable Material Combiner',
    'EnableSMC.desc': 'Enables Material Combiner',
    'EnableSMC.success': 'Enabled Material Combiner!',

    'AtlasHelpButton.label': 'Generate Material List',
    'AtlasHelpButton.desc': 'Open useful Atlas Tips',
    'AtlasHelpButton.URL': 'https://github.com/michaeldegroot/cats-blender-plugin/#texture-atlas',
    'AtlasHelpButton.success': 'Atlas Help opened.',

    'InstallShotariya.label': 'Error while loading Material Combiner:',
    'InstallShotariya.error.install1': 'Material Combiner is not installed!',
    'InstallShotariya.error.install2': 'The plugin \'Material Combiner\' by Shotariya is required for this function.',
    'InstallShotariya.error.install3': 'Please download and install it manually:',
    'InstallShotariya.error.enable1': 'Material Combiner is not enabled!',
    'InstallShotariya.error.enable2': 'The plugin \'Material Combiner\' by Shotariya is required for this function.',
    'InstallShotariya.error.enable3': 'Please enable it in your User Preferences.',
    'InstallShotariya.error.version1': 'Material Combiner is outdated!',
    'InstallShotariya.error.version2': 'The latest version is required for this function.',
    'InstallShotariya.error.version3': 'Please download and install it manually:',

    'ShotariyaButton.label': 'Download Material Combiner',
    'ShotariyaButton.URL': 'https://vrcat.club/threads/material-combiner-blender-addon-1-1-3.2255/',
    'ShotariyaButton.success': 'Material Combiner link opened',

    # Tools Bonemerge
    'BoneMergeButton.label': 'Merge Bones',
    'BoneMergeButton.desc': 'Merges the given percentage of bones together.\n'
                            'This is useful to reduce the amount of bones used by Dynamic Bones.',
    'BoneMergeButton.success': 'Merged bones.',

    # Tools Common
    'ShowError.label': 'Report: Error',

    # Tools Copy protection
    'CopyProtectionEnable.label': 'Enable Protection',
    'CopyProtectionEnable.desc': 'Protects your model from piracy. NOT a 100% safe protection!'
                                 '\nRead the documentation before use',
    'CopyProtectionEnable.success': 'Model secured!',

    'CopyProtectionDisable.label': 'Disable Protection',
    'CopyProtectionDisable.desc': 'Removes the copy protections from this model.',
    'CopyProtectionDisable.success': 'Model un-secured!',

    'ProtectionTutorialButton.label': 'Go to Documentation',
    'ProtectionTutorialButton.URL': 'https://github.com/michaeldegroot/cats-blender-plugin#copy-protection',
    'ProtectionTutorialButton.success': 'Documentation',

    # Tools Credits
    'ForumButton.label': 'Go to the Forums',
    'ForumButton.URL': 'https://vrcat.club/threads/cats-blender-plugin.6/',
    'ForumButton.success': 'Forum opened.',

    'DiscordButton.label': 'Join our Discord',
    'DiscordButton.URL': 'https://discord.gg/f8yZGnv',
    'DiscordButton.success': 'Discord opened.',

    'PatchnotesButton.label': 'Latest Patchnotes',
    'PatchnotesButton.URL': 'https://github.com/michaeldegroot/cats-blender-plugin/releases',
    'PatchnotesButton.success': 'Patchnotes opened.',

    # Tools Decimation
    'ScanButton.label': 'Scan for decimation models',
    'ScanButton.desc': 'Separates the mesh.',

    'AddShapeButton.label': 'Add',
    'AddShapeButton.desc': 'Adds the selected shape key to the whitelist.\n'
                           'This means that every mesh containing that shape key will be not decimated.',

    'AddMeshButton.label': 'Add',
    'AddMeshButton.desc': 'Adds the selected mesh to the whitelist.\n'
                          'This means that this mesh will be not decimated.',

    'RemoveShapeButton.label': '',
    'RemoveShapeButton.desc': 'Removes the selected shape key from the whitelist.\n'
                              'This means that this shape key is no longer decimation safe!',

    'RemoveMeshButton.label': '',
    'RemoveMeshButton.desc': 'Removes the selected mesh from the whitelist.\n'
                             'This means that this mesh will be decimated.',

    'AutoDecimateButton.label': 'Quick Decimation',
    'AutoDecimateButton.desc': 'This will automatically decimate your model while preserving the shape keys.\n'
                               'You should manually remove unimportant meshes first.',
    'AutoDecimateButton.error.noMesh': 'No meshes found!',

    'decimate.cantDecimateWithSettings': 'This model can not be decimated to {number} tris with the specified settings.',
    'decimate.safeTryOptions': 'Try to use Custom, Half or Full Decimation.',
    'decimate.halfTryOptions': 'Try to use Custom or Full Decimation.',
    'decimate.customTryOptions': 'Select fewer shape keys and/or meshes or use Full Decimation.',
    'decimate.disableFingersOrIncrease': 'Disable \'Save Fingers\' or increase the Tris Count.',
    'decimate.disableFingers': 'or disable \'Save Fingers\'.',  # This comes after one of the previous xTryOptions
    'decimate.noDecimationNeeded': 'The model already has less than {number} tris. Nothing had to be decimated.',
    'decimate.cantDecimate1': 'The model could not be decimated to {number} tris.',
    'decimate.cantDecimate2': 'It got decimated as much as possible within the limits.',

    # Tools Eyetracking
    'CreateEyesButton.label': 'Create Eye Tracking',
    'CreateEyesButton.desc': 'This will let you track someone when they come close to you and it enables blinking.\n'
                             'You should do decimation before this operation.\n'
                             'Test the resulting eye movement in the \'Testing\' tab.',
    'CreateEyesButton.error.noShapeSelected': 'You have no shape keys selected.'
                                              '\nPlease choose a mesh containing shape keys or check "Disable Eye Blinking".',
    'CreateEyesButton.error.missingBone': 'The bone "{bone}" does not exist.',
    'CreateEyesButton.error.noVertex': 'The bone "{bone}" has no existing vertex group or no vertices assigned to it.'
                                       '\nThis might be because you selected the wrong mesh or the wrong bone.'
                                       '\nAlso make sure that the selected eye bones actually move the eyes in pose mode.',
    'CreateEyesButton.error.dontUse': 'Please do not use "{eyeName}" as the input bone.'
                                      '\nIf you are sure that you want to use that bone please rename it to "{eyeNameShort}".',
    'CreateEyesButton.error.hierarchy': 'Eye tracking will not work unless the bone hierarchy is exactly as following: Hips > Spine > Chest > Neck > Head'
                                        '\nFurthermore the mesh containing the eyes has to be called "Body" and the armature "Armature".',
    'CreateEyesButton.success': 'Created eye tracking!',

    'StartTestingButton.label': 'Start Eye Testing',
    'StartTestingButton.desc': 'This will let you test how the eye movement will look ingame.\n'
                               'Don\'t forget to stop the Testing process afterwards.\n'
                               'Bones "LeftEye" and "RightEye" are required.',

    'StopTestingButton.label': 'Stop Eye Testing',
    'StopTestingButton.desc': 'Stops the testing process.',
    'StopTestingButton.error.tryAgain': 'Something went wrong. Please try eye testing again.',

    'ResetRotationButton.label': 'Reset Rotation',
    'ResetRotationButton.desc': 'This resets the eye positions.',

    'AdjustEyesButton.label': 'Set Range',
    'AdjustEyesButton.desc': 'Lets you re-adjust the movement range of the eyes.\n'
                             'This gets saved',
    'AdjustEyesButton.error.noVertex': 'The bone "{bone}" has no existing vertex group or no vertices assigned to it.'
                                       '\nThis might be because you selected the wrong mesh or the wrong bone.'
                                       '\nAlso make sure to join your meshes before creating eye tracking and make sure that the eye bones actually move the eyes in pose mode.',

    'StartIrisHeightButton.label': 'Start Iris Height Adjustment',
    'StartIrisHeightButton.desc': 'Lets you readjust the distance of the iris from the eye ball.\n'
                                  'Use this to fix clipping of the iris into the eye ball.\n'
                                  'This gets saved.',

    'TestBlinking.label': 'Test',
    'TestBlinking.desc': 'This lets you see how eye blinking will look in-game.',

    'TestLowerlid.label': 'Test',
    'TestLowerlid.desc': 'This lets you see how lowerlids will look in-game.',

    'ResetBlinkTest.label': 'Reset Shapes',
    'ResetBlinkTest.desc': 'This resets the blink testing.',

    # Tools Importer
    'ImportAnyModel.label': 'Import Any Model',
    'ImportAnyModel.desc2.79': 'Import a model of any supported type.'
                               '\n'
                               '\nSupported types:'
                               '\n- MMD: .pmx/.pmd'
                               '\n- XNALara: .xps/.mesh/.ascii'
                               '\n- Source: .smd/.qc'
                               '\n- VRM: .vrm'
                               '\n- FBX .fbx '
                               '\n- DAE: .dae '
                               '\n- ZIP: .zip',
    'ImportAnyModel.desc2.8': 'Import a model of any supported type.'
                              '\n'
                              '\nSupported types:'
                              '\n- MMD: .pmx/.pmd'
                              '\n- XNALara: .xps/.mesh/.ascii'
                              '\n- Source: .smd/.qc/.vta/.dmx'
                              '\n- VRM: .vrm'
                              '\n- FBX: .fbx'
                              '\n- DAE: .dae '
                              '\n- ZIP: .zip',
    'ImportAnyModel.importantInfo.label': 'IMPORTANT INFO (hover here)',
    'ImportAnyModel.importantInfo.desc': 'If you want to modify the import settings, use the button next to the Import button.\n\n',
    'ImportAnyModel.error.emptyZip': 'The selected zip file contains no importable models.',
    'ImportAnyModel.error.unsupportedFBX': 'The FBX file version is unsupported!'
                                           '\nPlease use a tool such as the "Autodesk FBX Converter" to make it compatible.',

    'ZipPopup.label': 'Zip Model Selection:',
    'ZipPopup.desc': 'Shows the models contained in the zip files',
    'ZipPopup.selectModel1': 'Select which model you want to import',
    'ZipPopup.selectModel2': 'Then confirm with OK',

    'get_zip_content.choose': 'Import model "{model}" from the zip "{zipName}?"',

    'ModelsPopup.label': 'Select which you want to import:',
    'ModelsPopup.desc': 'Show individual import options',

    'ImportMMD.label': 'MMD',
    'ImportMMD.desc': 'Import a MMD model (.pmx/pmd)',

    'ImportXPS.label': 'XNALara',
    'ImportXPS.desc': 'Import a XNALara model (.xps/.mesh/.ascii)',

    'ImportSource.label': 'Source',
    'ImportSource.desc': 'Import a Source model (.smd/.qc/.vta/.dmx)',

    'ImportFBX.label': 'FBX',
    'ImportFBX.desc': 'Import a FBX model (.fbx)',

    'ImportVRM.label': 'VRM',
    'ImportVRM.desc': 'Import a VRM model (.vrm)',

    'InstallXPS.label': 'XPS Tools is not installed or enabled!',

    'InstallSource.label': 'Source Tools is not installed or enabled!',

    'InstallVRM.label': 'VRM Importer is not installed or enabled!',

    'InstallX.pleaseInstall1': 'If it is not enabled please enable it in your User Preferences.',
    'InstallX.pleaseInstall2': 'If it is not installed please download and install it manually.',
    'InstallX.pleaseInstall3': 'Make sure to install the version for Blender {blenderVersion}',
    'InstallX.pleaseInstallTesting': 'Currently you have to select \'Testing\' in the addons settings.',

    'EnableMMD.label': 'Mmd_tools is not enabled!',
    'EnableMMD.required1': 'The plugin "mmd_tools" is required for this function.',
    'EnableMMD.required2': 'Please restart Blender.',

    'XpsToolsButton.label': 'Download XPS Tools',
    'XpsToolsButton.URL': 'https://github.com/johnzero7/XNALaraMesh',
    'XpsToolsButton.success': 'XPS Tools link opened',

    'SourceToolsButton.label': 'Download Source Tools',
    'SourceToolsButton.URL': 'https://github.com/Artfunkel/BlenderSourceTools',
    'SourceToolsButton.success': 'Source Tools link opened',

    'VrmToolsButton.label': 'Download VRM Importer',
    'VrmToolsButton.URL_2.79': 'https://github.com/iCyP/VRM_IMPORTER_for_Blender2_79',
    'VrmToolsButton.URL_2.8': 'https://github.com/saturday06/VRM_IMPORTER_for_Blender2_8',
    'VrmToolsButton.success': 'VRM Importer link opened',

    'ExportModel.label': 'Export Model',
    'ExportModel.desc': 'Export this model as .fbx for Unity.\n'
                        '\n'
                        'Automatically sets the optimal export settings',
    'ExportModel.error.notEnabled': 'FBX Exporter not enabled! Please enable it in your User Preferences.',

    'ErrorDisplay.label': 'Warning:',
    'ErrorDisplay.polygons1': 'Too many polygons!',
    'ErrorDisplay.polygons2': 'You have {number} tris in this model, but you shouldn\'t have more than 70,000!',
    'ErrorDisplay.polygons3': 'You should decimate before you export this model.',
    'ErrorDisplay.materials1': 'Model not optimized!',
    'ErrorDisplay.materials2': 'This model has {number} materials!',
    'ErrorDisplay.materials3': 'You should try to have a maximum of 4 materials on your model.',
    'ErrorDisplay.materials4': 'Creating a texture atlas in CATS is very easy, so please make use of it.',
    'ErrorDisplay.meshes1': 'Meshes not joined!',
    'ErrorDisplay.meshes2': 'This model has {number} meshes!',
    'ErrorDisplay.meshes3': 'It is not very optimized and might cause lag for you and others!',
    'ErrorDisplay.meshes3_alt': "It is extremely unoptimized and will cause laugh for you and others!",
    'ErrorDisplay.meshes4': 'You should always join your meshes, it\'s very easy:',
    'ErrorDisplay.JoinMeshes.label': 'Join Meshes',
    'ErrorDisplay.brokenShapekeys1': 'Broken shapekeys!',
    'ErrorDisplay.brokenShapekeys2': 'This model has {number} broken shapekey(s):',
    'ErrorDisplay.brokenShapekeys3': 'You will not be able to upload this model until you fix these shapekeys.',
    'ErrorDisplay.brokenShapekeys4': 'Either delete or repair them before export.',
    'ErrorDisplay.textures1': 'No textures found!',
    'ErrorDisplay.textures2': 'This model has no textures assigned but you have \'Embed Textures\' enabled.',
    'ErrorDisplay.textures3': 'Therefore, no textures will be embedded into the FBX.',
    'ErrorDisplay.textures4': 'This is not an issue, but you will have to import the textures manually into Unity.',
    'ErrorDisplay.eyes1': 'Eyes not named \'Body\'!',
    'ErrorDisplay.eyes2': 'The mesh \'{name}\' has Eye Tracking shapekeys but is not named \'Body\'.',
    'ErrorDisplay.eyes2_alt': 'Multiple meshes have Eye Tracking shapekeys but are not named \'Body\'.',
    'ErrorDisplay.eyes3': 'If you want Eye Tracking to work, rename this mesh to \'Body\'.',
    'ErrorDisplay.eyes3_alt': 'Make sure that the mesh containing the eyes is named \'Body\' in order',
    'ErrorDisplay.eyes4_alt': 'to get Eye Tracking to work.',
    'ErrorDisplay.continue': 'Continue to Export',

    # Tools Material
    'OneTexPerMatButton.label': 'One Material Texture',
    'OneTexPerMatButton.desc': 'Have all material slots ignore extra texture slots as these are not used by VRChat.',

    'OneTexPerMatOnlyButton.label': 'One Material Texture',
    'OneTexPerMatOnlyButton.desc': 'Have all material slots ignore extra texture slots as these are not used by VRChat.'
                                   '\nAlso removes the textures from the material instead of disabling it.'
                                   '\nThis makes no difference, but cleans the list for the perfectionists',

    'ToolsMaterial.error.notCompatible': 'This function is not yet compatible with Blender 2.8!',
    'OneTexPerXButton.success': 'All materials have one texture now.',

    'StandardizeTextures.label': 'Standardize Textures',
    'StandardizeTextures.desc': 'Enables Color and Alpha on every texture, sets the blend method to Multiply'
                                '\nand changes the materials transparency to Z-Transparency',
    'StandardizeTextures.success': 'All textures are now standardized.',

    'CombineMaterialsButton.label': 'Combine Same Materials',
    'CombineMaterialsButton.desc': 'Combines similar materials into one, reducing draw calls.\n'
                                   'Your avatar should visibly look the same after this operation.\n'
                                   'This is a very important step for optimizing your avatar.\n'
                                   'If you have problems with this, please tell us!\n',
    'CombineMaterialsButton.error.noChanges': 'No materials combined.',
    'CombineMaterialsButton.success': 'Combined {number} materials!',

    'ConvertAllToPngButton.label': 'Convert Textures to PNG',
    'ConvertAllToPngButton.desc': 'Converts all texture files into PNG files.'
                                  '\nThis helps with transparency and compatibility issues.'
                                  '\n\nThe converted image files will be saved next to the old ones',
    'ConvertAllToPngButton.success': 'Converted {number} to PNG files.',

    # Tools Root bone
    'RootButton.label': 'Parent Bones',
    'RootButton.desc': 'This will duplicate the parent of the bones and reparent them to the duplicate.\n'
                       'Very useful for Dynamic Bones.',
    'RootButton.success': 'Bones parented!',

    'RefreshRootButton.label': 'Refresh List',
    'RefreshRootButton.desc': 'This will clear the group bones list cache and rebuild it, useful if bones have changed or your model.',
    'RefreshRootButton.success': 'Root bones refreshed, check the root bones list again.',

    # Tools Settings
    'RevertChangesButton.label': 'Revert Settings',
    'RevertChangesButton.desc': 'Revert the changes back to how they were on Blender start-up.',
    'RevertChangesButton.success': 'Settings reverted.',

    'ResetGoogleDictButton.label': 'Clear Local Google Translations',
    'ResetGoogleDictButton.desc': 'Deletes all currently saved Google Translations. You can\'t undo this',
    'ResetGoogleDictButton.resetInfo': 'Local Google Dictionary cleared!',

    'DebugTranslations.label': 'Debug Google Translations',  # DEV ONLY
    'DebugTranslations.desc': 'Tests Google translations and prints the response into a file called \'google-response.txt\' located in the cats addon folder > resources'
                              '\nThis button is only visible in the cats development version',  # DEV ONLY
    'DebugTranslations.error': 'Errors found, response printed!!',  # DEV ONLY
    'DebugTranslations.success': 'No issues with Google Translations found, response printed!',  # DEV ONLY

    # Tools Shapekey
    'ShapeKeyApplier.label': 'Apply Selected Shapekey to Basis',
    'ShapeKeyApplier.desc': 'Applies the selected shape key to the new Basis at it\'s current strength and creates a reverted shape key from the selected one',
    'ShapeKeyApplier.error.revertCustomBasis': ['To revert the shape keys, please apply the "Reverted" shape keys in reverse order.',
                                                'Start with the shape key called "{name}".',
                                                '',
                                                'If you didn\'t change the shape key order, you can revert the shape keys from top to bottom.'],
    'ShapeKeyApplier.error.revertCustomBasis.scale': 7.3,
    'ShapeKeyApplier.error.revert': ['To revert the shape keys, please apply the "Reverted" shape keys in reverse order.',
                                     'Start with the reverted shape key that uses the relative key called "Basis".',
                                     '',
                                     "If you didn't change the shape key order, you can revert the shape keys from top to bottom."],
    'ShapeKeyApplier.error.revert.scale': 7.3,
    'ShapeKeyApplier.successRemoved': 'Successfully removed shapekey "{name}" from the Basis.',
    'ShapeKeyApplier.successSet': 'Successfully set shapekey "{name}" as the new Basis.',

    'addToShapekeyMenu.ShapeKeyApplier.label': 'Apply Selected Shapekey to Basis',

    # Tools Supporter
    'PatreonButton.label': 'Become a Patron',
    'PatreonButton.URL': 'https://www.patreon.com/catsblenderplugin',
    'PatreonButton.success': 'Patreon page opened.',

    'ReloadButton.label': 'Reload List',
    'ReloadButton.desc': 'Reloads the supporter list',

    'DynamicPatronButton.label': 'Supporter Name',
    'DynamicPatronButton.desc': 'This is an awesome supporter',

    'register_dynamic_buttons.desc': '{name} is an awesome supporter',

    # Tools Translate
    'TranslateShapekeyButton.label': 'Translate Shape Keys',
    'TranslateShapekeyButton.desc': 'Translates all shape keys using the internal dictionary and Google Translate',
    'TranslateShapekeyButton.success': 'Translated {number} shape keys.',

    'TranslateBonesButton.label': 'Translate Bones',
    'TranslateBonesButton.desc': 'Translates all bones using the internal dictionary and Google Translate',
    'TranslateBonesButton.success': 'Translated {number} bones.',

    'TranslateObjectsButton.label': 'Translate Meshes & Objects',
    'TranslateObjectsButton.desc': 'Translates all meshes and objects using the internal dictionary and Google Translate',
    'TranslateObjectsButton.success': 'Translated {number} meshes and objects.',

    'TranslateMaterialsButton.label': 'Translate Materials',
    'TranslateMaterialsButton.desc': 'Translates all materials using the internal dictionary and Google Translate',
    'TranslateMaterialsButton.success': 'Translated {number} materials.',

    'TranslateTexturesButton.label': 'Translate Textures',
    'TranslateTexturesButton.desc': 'Translates all textures using the internal dictionary and Google Translate',
    'TranslateTexturesButton.success_alt': 'Translated all textures',
    'TranslateTexturesButton.error.noInternet': 'Could not connect to Google. Please check your internet connection.',
    'TranslateTexturesButton.success': 'Translated {number} textures',

    'TranslateAllButton.label': 'Translate Everything',
    'TranslateAllButton.desc': 'Translates everything using the internal dictionary and Google Translate',
    'TranslateAllButton.success': 'Translated everything.',

    'TranslateX.error.wrongVersion': 'You need Blender 2.79 or higher for this function.',

    'update_dictionary.error.cantConnect': 'Could not connect to Google. Some parts could not be translated.',
    'update_dictionary.error.temporaryBan': 'It looks like you got banned from Google Translate temporarily!',
    'update_dictionary.error.catsTranslated': '\nCats translated what it could with the local dictionary, but you will have to try again later for the Google translations.',
    'update_dictionary.error.cantAccess': 'Cats was not able to access Google Translate!',
    'update_dictionary.error.errorMsg': 'You got an error message from Google Translate!',
    'update_dictionary.error.apiChanged': 'Could not get translations from Google Translate!'
                                          '\nThis means that Google changed their API and translations will no longer work until this is fixed.'
                                          '\nPlease translate manually or wait for an CATS update.'
                                          '\nFor updates and dicussions please join our Discord. The link can be found in the Credits panel down below.',

    # Tools Viseme
    'AutoVisemeButton.label': 'Create Visemes',
    'AutoVisemeButton.desc': 'This will give your avatar the ability to mimic each sound that comes from your mouth by blending between various shapes to mimic your actual voice.\n'
                             'It will generate 15 shape keys from the 3 shape keys you specify',
    'AutoVisemeButton.error.noShapekeys': 'This mesh has no shapekeys!',
    'AutoVisemeButton.error.selectShapekeys': 'Please select the correct mouth shapekeys instead of "Basis"!',
    'AutoVisemeButton.success': 'Created mouth visemes!',

    # Extensions
    'Scene.armature.label': 'Armature',
    'Scene.armature.desc': 'Select the armature which will be used by Cats',

    'Scene.zip_content.label': 'Zip Content',
    'Scene.zip_content.desc': 'Select the model you want to import',

    'Scene.keep_upper_chest.label': 'Keep Upper Chest',
    'Scene.keep_upper_chest.desc': 'VRChat now partially supports the Upper Chest bone, so deleting it is no longer necessary.'
                                   '\n\nWARNING: Currently this breaks Eye Tracking, so don\'t check this if you want Eye Tracking',

    'Scene.combine_mats.label': 'Combine Same Materials',
    'Scene.combine_mats.desc': 'Combines similar materials into one, reducing draw calls.\n\n'
                               'Your avatar should visibly look the same after this operation.\n'
                               'This is a very important step for optimizing your avatar.\n'
                               'If you have problems with this, uncheck this option and tell us!\n',

    'Scene.remove_zero_weight.label': 'Remove Zero Weight Bones',
    'Scene.remove_zero_weight.desc': 'Cleans up the bones hierarchy, deleting all bones that don\'t directly affect any vertices.'
                                     '\nUncheck this if bones or vertex groups that you want to keep got deleted',

    'Scene.keep_end_bones.label': 'Keep End Bones',
    'Scene.keep_end_bones.desc': 'Saves end bones from deletion.'
                                 '\n\nThis can improve skirt movement for dynamic bones, but increases the bone count.'
                                 '\nThis can also fix issues with crumbled finger bones in Unity.'
                                 '\nMake sure to always uncheck "Add Leaf Bones" when exporting or use the CATS export button',

    'Scene.keep_twist_bones.label': 'Keep Twist Bones',
    'Scene.keep_twist_bones.desc': 'This will keep any bone with "Twist" in the name.'
                                   '\nSo if there are certain bones that you want to keep, you can add "Twist" to them and they won\'t get deleted.'
                                   '\n\nVRChat can now make use of twist bones, so you can use this option to keep them',

    'Scene.fix_twist_bones.label': 'Fix MMD Twist Bones',
    'Scene.fix_twist_bones.desc': 'This will make MMD arm twist bones usable in VRChat.'
                                  '\nWIll only work if the twist bones are properly named.'
                                  '\nRequired names:'
                                  '\n  - ArmTwist[1-3]_[L/R]'
                                  '\n  - HandTwist[1-3]_[L/R]'
                                  '\n\nYou don\'t need to enable "Keep Twist Bones" for this to work',

    'Scene.join_meshes.label': 'Join Meshes',
    'Scene.join_meshes.desc': 'Joins all meshes of this model together.'
                              '\nIt also:'
                              '\n  - Applies all transformations'
                              '\n  - Repairs broken armature modifiers'
                              '\n  - Applies all decimation and mirror modifiers'
                              '\n  - Merges UV maps correctly'
                              '\n'
                              '\nINFO: You should always join your meshes',

    'Scene.connect_bones.label': 'Connect Bones',
    'Scene.connect_bones.desc': 'This connects all bones to their child bone if they have exactly one child bone.\n'
                                'This will not change how the bones function in any way, it just improves the aesthetic of the armature',

    'Scene.fix_materials.label': 'Fix Materials',
    'Scene.fix_materials.desc': 'This will apply some VRChat related fixes to materials',

    'Scene.remove_rigidbodies_joints.label': 'Remove Rigidbodies and Joints',
    'Scene.remove_rigidbodies_joints.desc': 'Rigidbodies and joints are used by MMD software to simulate physics.'
                                            '\nThey are completely useless for VRChat, so removing them is recommended for VRChat users!',

    'Scene.use_google_only.label': 'Use Old Translations (not recommended)',
    'Scene.use_google_only.desc': 'Ignores the internal dictionary and only uses the Google Translator for shape key translations.'
                                  '\n'
                                  '\nThis will result in slower translation speed and worse translations, but the translations will be like in CATS version 0.9.0 and older.'
                                  '\nOnly use this if you have animations which rely on the old translations and you don\'t want to convert them to the new ones',

    'Scene.show_more_options.label': 'Show More Options',
    'Scene.show_more_options.desc': 'Shows more model options',

    'Scene.merge_mode.label': 'Merge Mode',
    'Scene.merge_mode.desc': 'Mode',
    'Scene.merge_mode.armature.label': 'Merge Armatures',
    'Scene.merge_mode.armature.desc': 'Here you can merge two armatures together.',
    'Scene.merge_mode.mesh.label': 'Attach Mesh',
    'Scene.merge_mode.mesh.desc': 'Here you can attach a mesh to an armature.',

    'Scene.merge_armature_into.label': 'Base Armature',
    'Scene.merge_armature_into.desc': 'Select the armature into which the other armature will be merged\n',

    'Scene.merge_armature.label': 'Merge Armature',
    'Scene.merge_armature.desc': 'Select the armature which will be merged into the selected armature above\n',

    'Scene.attach_to_bone.label': 'Attach to Bone',
    'Scene.attach_to_bone.desc': 'Select the bone to which the armature will be attached to\n',

    'Scene.attach_mesh.label': 'Attach Mesh',
    'Scene.attach_mesh.desc': 'Select the mesh which will be attached to the selected bone in the selected armature\n',

    'Scene.merge_same_bones.label': 'Merge All Bones',
    'Scene.merge_same_bones.desc': 'Merges all bones together that have the same name instead of only the base bones (Hips, Spine, etc).'
                                   '\nYou will have to make sure that all the bones you want to merge have the same name.'
                                   '\n'
                                   '\nIf this is checked, you won\'t need to fix the model with CATS beforehand but it is still advised to do so.'
                                   '\nIf this is unchecked, CATS will only merge the base bones (Hips, Spine, etc).'
                                   '\n'
                                   '\nThis can have unintended side effects, so check your model afterwards!'
                                   '\n',

    'Scene.apply_transforms.label': 'Apply Transforms',
    'Scene.apply_transforms.desc': 'Check this if both armatures and meshes are already at their correct positions.'
                                   '\nThis will cause them to stay exactly where they are when merging',

    'Scene.merge_armatures_join_meshes.label': 'Join Meshes',
    'Scene.merge_armatures_join_meshes.desc': 'This will join all meshes.'
                                              '\nNot checking this will always apply transforms',

    'Scene.merge_armatures_remove_zero_weight_bones.label': 'Remove Zero Weight Bones',
    'Scene.merge_armatures_remove_zero_weight_bones.desc': 'Cleans up the bones hierarchy, deleting all bones that don\'t directly affect any vertices.'
                                                           '\nUncheck this if bones or vertex groups that you want to keep got deleted',

    # Decimation
    'Scene.decimation_mode.label': 'Decimation Mode',
    'Scene.decimation_mode.desc': 'Decimation Mode',
    'Scene.decimation_mode.smart.label': "Smart",
    'Scene.decimation_mode.smart.desc': 'Best results - repair shape keys after decimation\n'
                                        '\n'
                                        "This will decimate your whole model and attempt to undo the warping caused by Blender's decimation.\n"
                                        "This will give the best results and keep blinking and lip syncing, but may have issues on some models.",
    'Scene.decimation_mode.safe.label': 'Safe',
    'Scene.decimation_mode.safe.desc': 'Decent results - no shape key loss\n'
                                       '\n'
                                       'This will only decimate meshes with no shape keys.\n'
                                       'The results are decent and you won\'t lose any shape keys.\n'
                                       'Eye Tracking and Lip Syncing will be fully preserved.',
    'Scene.decimation_mode.half.label': 'Half',
    'Scene.decimation_mode.half.desc': 'Good results - minimal shape key loss\n'
                                       '\n'
                                       'This will only decimate meshes with less than 4 shape keys as those are often not used.\n'
                                       'The results are better but you will lose the shape keys in some meshes.\n'
                                       'Eye Tracking and Lip Syncing should still work.',
    'Scene.decimation_mode.full.label': 'Full',
    'Scene.decimation_mode.full.desc': 'Consistent results - full shape key loss\n'
                                       '\n'
                                       'This will decimate your whole model deleting all shape keys in the process.\n'
                                       'This will give consistent results but you will lose the ability to add blinking and Lip Syncing.\n'
                                       'Eye Tracking will still work if you disable Eye Blinking.',
    'Scene.decimation_mode.custom.label': 'Custom',
    'Scene.decimation_mode.custom.desc': 'Custom results - custom shape key loss\n'
                                         '\n'
                                         'This will let you choose which meshes and shape keys should not be decimated.\n',

    'Scene.selection_mode.label': 'Selection Mode',
    'Scene.selection_mode.desc': 'Selection Mode',
    'Scene.selection_mode.shapekeys.label': 'Shape Keys',
    'Scene.selection_mode.shapekeys.desc': 'Select all the shape keys you want to preserve here.',
    'Scene.selection_mode.meshes.label': 'Meshes',
    'Scene.selection_mode.meshes.desc': 'Select all the meshes you don\'t want to decimate here.',

    'Scene.add_shape_key.label': 'Shape',
    'Scene.add_shape_key.desc': 'The shape key you want to keep',

    'Scene.add_mesh.label': 'Mesh',
    'Scene.add_mesh.desc': 'The mesh you want to leave untouched by the decimation',

    'Scene.decimate_fingers.label': 'Save Fingers',
    'Scene.decimate_fingers.desc': 'Check this if you don\'t want to decimate your fingers!\n'
                                   'Results will be worse but there will be no issues with finger movement.\n'
                                   'This is probably only useful if you have a VR headset.\n'
                                   '\n'
                                   'This operation requires the finger bones to be named specifically:\n'
                                   'Thumb(0-2)_(L/R)\n'
                                   'IndexFinger(1-3)_(L/R)\n'
                                   'MiddleFinger(1-3)_(L/R)\n'
                                   'RingFinger(1-3)_(L/R)\n'
                                   'LittleFinger(1-3)_(L/R)',

    'Scene.decimate_hands.label': 'Save Hands',
    'Scene.decimate_hands.desc': 'Check this if you don\'t want to decimate your full hands!\n'
                                 'Results will be worse but there will be no issues with hand movement.\n'
                                 'This is probably only useful if you have a VR headset.\n'
                                 '\n'
                                 'This operation requires the finger and hand bones to be named specifically:\n'
                                 'Left/Right wrist\n'
                                 'Thumb(0-2)_(L/R)\n'
                                 'IndexFinger(1-3)_(L/R)\n'
                                 'MiddleFinger(1-3)_(L/R)\n'
                                 'RingFinger(1-3)_(L/R)\n'
                                 'LittleFinger(1-3)_(L/R)',

    'Scene.decimation_remove_doubles.label': 'Remove Doubles',
    'Scene.decimation_remove_doubles.desc': 'Uncheck this if you got issues with with this checked',

    'Scene.max_tris.label': 'Tris',
    'Scene.max_tris.desc': 'The target amount of tris after decimation',

    # Eye Tracking
    'Scene.eye_mode.label': 'Eye Mode',
    'Scene.eye_mode.desc': 'Mode',
    'Scene.eye_mode.creation.label': 'Creation',
    'Scene.eye_mode.creation.desc': 'Here you can create eye tracking.',
    'Scene.eye_mode.testing.label': 'Testing',
    'Scene.eye_mode.testing.desc': 'Here you can test how eye tracking will look in-game.',

    'Scene.mesh_name_eye.label': 'Mesh',
    'Scene.mesh_name_eye.desc': 'The mesh with the eyes vertex groups',

    'Scene.head.label': 'Head',
    'Scene.head.desc': 'The head bone containing the eye bones',

    'Scene.eye_left.label': 'Left Eye',
    'Scene.eye_left.desc': 'The models left eye bone',

    'Scene.eye_right.label': 'Right Eye',
    'Scene.eye_right.desc': 'The models right eye bone',

    'Scene.wink_left.label': 'Blink Left',
    'Scene.wink_left.desc': 'The shape key containing a blink with the left eye',

    'Scene.wink_right.label': 'Blink Right',
    'Scene.wink_right.desc': 'The shape key containing a blink with the right eye',

    'Scene.lowerlid_left.label': 'Lowerlid Left',
    'Scene.lowerlid_left.desc': 'The shape key containing a slightly raised left lower lid.\n'
                                'Can be set to "Basis" to disable lower lid movement',

    'Scene.lowerlid_right.label': 'Lowerlid Right',
    'Scene.lowerlid_right.desc': 'The shape key containing a slightly raised right lower lid.\n'
                                 'Can be set to "Basis" to disable lower lid movement',

    'Scene.disable_eye_movement.label': 'Disable Eye Movement',
    'Scene.disable_eye_movement.desc': 'IMPORTANT: Do your decimation first if you check this!\n'
                                       '\n'
                                       'Disables eye movement. Useful if you only want blinking.\n'
                                       'This creates eye bones with no movement bound to them.\n'
                                       'You still have to assign "LeftEye" and "RightEye" to the eyes in Unity',

    'Scene.disable_eye_blinking.label': 'Disable Eye Blinking',
    'Scene.disable_eye_blinking.desc': 'Disables eye blinking. Useful if you only want eye movement.\n'
                                       'This will create the necessary shape keys but leaves them empty',

    'Scene.eye_distance.label': 'Eye Movement Range',
    'Scene.eye_distance.desc': 'Higher = more eye movement\n'
                               'Lower = less eye movement\n'
                               'Warning: Too little or too much range can glitch the eyes.\n'
                               'Test your results in the "Eye Testing"-Tab!\n',

    'Scene.eye_rotation_x.label': 'Up - Down',
    'Scene.eye_rotation_x.desc': 'Rotate the eye bones on the vertical axis',

    'Scene.eye_rotation_y.label': 'Left - Right',
    'Scene.eye_rotation_y.desc': 'Rotate the eye bones on the horizontal axis.'
                                 '\nThis is from your own point of view',

    'Scene.iris_height.label': 'Iris Height',
    'Scene.iris_height.desc': 'Moves the iris away from the eye ball',

    'Scene.eye_blink_shape.label': 'Blink Strength',
    'Scene.eye_blink_shape.desc': 'Test the blinking of the eye',

    'Scene.eye_lowerlid_shape.label': 'Lowerlid Strength',
    'Scene.eye_lowerlid_shape.desc': 'Test the lowerlid blinking of the eye',

    'Scene.mesh_name_viseme.label': 'Mesh',
    'Scene.mesh_name_viseme.desc': 'The mesh with the mouth shape keys',

    # Visemes
    'Scene.mouth_a.label': 'Viseme AA',
    'Scene.mouth_a.desc': 'Shape key containing mouth movement that looks like someone is saying "aa".\nDo not put empty shape keys like "Basis" in here',

    'Scene.mouth_o.label': 'Viseme OH',
    'Scene.mouth_o.desc': 'Shape key containing mouth movement that looks like someone is saying "oh".\nDo not put empty shape keys like "Basis" in here',

    'Scene.mouth_ch.label': 'Viseme CH',
    'Scene.mouth_ch.desc': 'Shape key containing mouth movement that looks like someone is saying "ch". Opened lips and clenched teeth.\nDo not put empty shape keys like "Basis" in here',

    'Scene.shape_intensity.label': 'Shape Key Mix Intensity',
    'Scene.shape_intensity.desc': 'Controls the strength in the creation of the shape keys. Lower for less mouth movement strength',

    # Bone Parenting
    'Scene.root_bone.label': 'To Parent',
    'Scene.root_bone.desc': 'List of bones that look like they could be parented together to a root bone',

    # Optimize
    'Scene.optimize_mode.label': 'Optimize Mode',
    'Scene.optimize_mode.desc': 'Mode',
    'Scene.optimize_mode.atlas.label': 'Atlas',
    'Scene.optimize_mode.atlas.desc': 'Allows you to make a texture atlas.',
    'Scene.optimize_mode.material.label': 'Material',
    'Scene.optimize_mode.material.desc': 'Some various options on material manipulation.',
    'Scene.optimize_mode.bonemerging.label': 'Bone Merging',
    'Scene.optimize_mode.bonemerging.desc': 'Allows child bones to be merged into their parents.',

    # Bone Merging
    'Scene.merge_ratio.label': 'Merge Ratio',
    'Scene.merge_ratio.desc': 'Higher = more bones will be merged\n'
                              'Lower = less bones will be merged\n',

    'Scene.merge_mesh.label': 'Mesh',
    'Scene.merge_mesh.desc': 'The mesh with the bones vertex groups',

    'Scene.merge_bone.label': 'To Merge',
    'Scene.merge_bone.desc': 'List of bones that look like they could be merged together to reduce overall bones',

    # Settings
    'Scene.show_mmd_tabs.label': 'Show mmd_tools tabs',
    'Scene.show_mmd_tabs.desc': 'Allows you to hide/show the mmd_tools tabs "MMD" and "Misc"',

    'Scene.embed_textures.label': 'Embed Textures on Export',
    'Scene.embed_textures.desc': 'Enable this to embed the texture files into the FBX file upon export.'
                                 '\nUnity will automatically extract these textures and put them into a separate folder.'
                                 '\nThis might not work for everyone and it increases the file size of the exported FBX file',

    'Scene.use_custom_mmd_tools.label': 'Use Custom mmd_tools',
    'Scene.use_custom_mmd_tools.desc': 'Enable this to use your own version of mmd_tools. This will disable the internal cats mmd_tools',

    'Scene.debug_translations.label': 'Debug Google Translations',
    'Scene.debug_translations.desc': 'Tests the Google Translations and prints the Google response in case of error',

    # Updater
    'CheckForUpdateButton.label': 'Check now for Update',
    'CheckForUpdateButton.desc': 'Checks if a new update is available for CATS',

    'UpdateToLatestButton.label': 'Update Now',
    'UpdateToLatestButton.desc': 'Update CATS to the latest version',

    'UpdateToSelectedButton.label': 'Update to Selected version',
    'UpdateToSelectedButton.desc': 'Update CATS to the selected version',

    'UpdateToDevButton.label': 'Update to Development version',
    'UpdateToDevButton.desc': 'Update CATS to the Development version',

    'RemindMeLaterButton.label': 'Remind me later',
    'RemindMeLaterButton.desc': 'This hides the update notification \'til the next Blender restart',
    'RemindMeLaterButton.success': 'You will be reminded later',

    'IgnoreThisVersionButton.label': 'Ignore this version',
    'IgnoreThisVersionButton.desc': 'This ignores this version. You will be reminded again when the next version releases',
    'IgnoreThisVersionButton.success': 'Version {name} will be ignored.',

    'ShowPatchnotesPanel.label': 'Patchnotes',
    'ShowPatchnotesPanel.desc': 'Shows the patchnotes of the selected version',
    'ShowPatchnotesPanel.releaseDate': 'Released: {date}',

    'ConfirmUpdatePanel.label': 'Confirm Update',
    'ConfirmUpdatePanel.desc': 'This shows you a panel in which you have to confirm your update choice',
    'ConfirmUpdatePanel.warn.dev1': 'Warning:',
    'ConfirmUpdatePanel.warn.dev2': ' The development version of CATS if the place where',
    'ConfirmUpdatePanel.warn.dev3': ' we test new features and bug fixes.',
    'ConfirmUpdatePanel.warn.dev4': ' This version might be very unstable and some features',
    'ConfirmUpdatePanel.warn.dev5': ' might not work correctly.',
    'ConfirmUpdatePanel.ShowPatchnotesPanel.label': 'Show Patchnotes',
    'ConfirmUpdatePanel.updateNow': 'Update now:',

    'UpdateCompletePanel.label': 'Installation Report',
    'UpdateCompletePanel.desc': 'The update is now complete',
    'UpdateCompletePanel.success1': 'CATS was successfully updated.',
    'UpdateCompletePanel.success2': 'Restart Blender to complete the update.',
    'UpdateCompletePanel.failure1': 'Update failed.',
    'UpdateCompletePanel.failure2': 'See Updater Panel for more info.',

    'UpdateNotificationPopup.label': 'Update available',
    'UpdateNotificationPopup.desc': 'This shows you that an update is available',
    'UpdateNotificationPopup.newUpdate': 'CATS v{name} available!',
    'UpdateNotificationPopup.ShowPatchnotesPanel.label': 'Show Patchnotes',

    'check_for_update.cantCheck': 'Could not check for updates, try again later',

    'download_file.cantConnect': 'Could not connect to Github',
    'download_file.cantFindZip': 'Could not find the downloaded zip',
    'download_file.cantFindCATS': 'Could not find CATS in the downloaded zip',

    'draw_update_notification_panel.success': 'Restart Blender to complete update!',
    'draw_update_notification_panel.newUpdate': 'CATS v{name} available!',
    'draw_update_notification_panel.UpdateToLatestButton.label': 'Update Now',
    'draw_update_notification_panel.RemindMeLaterButton.label': 'Remind me later',
    'draw_update_notification_panel.IgnoreThisVersionButton.label': 'Ignore this version',

    'draw_updater_panel.updateLabel': 'Updates:',
    'draw_updater_panel.updateLabel_alt': 'CATS Updater:',
    'draw_updater_panel.success': 'Restart Blender to complete update!',
    'draw_updater_panel.CheckForUpdateButton.label': 'Checking..',
    'draw_updater_panel.UpdateToLatestButton.label': 'Update now to {name}',
    'draw_updater_panel.CheckForUpdateButton.label_alt': 'Check now for Update',
    'draw_updater_panel.UpdateToLatestButton.label_alt': 'Up to Date!',
    'draw_updater_panel.UpdateToSelectedButton.label': 'Install version:',
    'draw_updater_panel.UpdateToDevButton.label': 'Install Development Version',
    'draw_updater_panel.currentVersion': 'Current version: {name}',

    'bpy.types.Scene.cats_updater_version_list.label': 'Version',
    'bpy.types.Scene.cats_updater_version_list.desc': 'Select the version you want to install\n',

    'bpy.types.Scene.cats_update_action.label': 'Choose action',
    'bpy.types.Scene.cats_update_action.desc': 'Action',
    'bpy.types.Scene.cats_update_action.update.label': 'Update Now',
    'bpy.types.Scene.cats_update_action.update.desc': 'Updates now to the latest version',
    'bpy.types.Scene.cats_update_action.ignore.label': 'Ignore this version',
    'bpy.types.Scene.cats_update_action.ignore.desc': 'This ignores this version. You will be reminded again when the next version releases',
    'bpy.types.Scene.cats_update_action.defer.label': 'Remind me later',
    'bpy.types.Scene.cats_update_action.defer.desc': 'Hides the update notification til the next Blender restart',

}
