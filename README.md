# BLENDS2GLTFS

## a .blend to .gltf mass exporter

_Author: Belery Olivier
Version: 1.0
License: MIT_

## Description:

Script to exports all blend files (even nested in subdirectories) to GLTF 2 format. Exported files are saved in a user specified location.

This python script uses Blender's embeded python interpreter. No other Python required.

Use case: Export multiple blender files content to single Unity/Godot/A-frame assets folder.

## Usage:

**WINDOWS:**

```bash
 "C:/program files (x86)/blender foundation/blender/blender.exe" --background --python blends2gltfs.py -- PATH_WHERE TO EXPORT YOUR_GLTF
```

**NIX (osx/linux/unix...):\***

```bash
 blender --background --python blends2gltfs.py -- PATH_WHERE TO EXPORT YOUR_GLTF
```
