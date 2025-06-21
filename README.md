# STL Batch Screenshot Renderer

This project contains two Python scripts designed to automate rendering screenshots of STL 3D models using Blender and to clean up rendered screenshots based on size criteria.

---

## Scripts

1. **main.py**

- Recursively loads all .stl files from the folder named STLFiles (including all subfolders).
- Renders a screenshot of each STL file from a 45 degree angle to the right and 60 degree vertical angle.
- Saves screenshots as .png files inside a folder named screenshots inside STLFiles, preserving the original STL folder structure.

2. **clean_screenshots.py**

- Takes the root screenshots folder as input.
- Deletes any PNG images whose filenames contain dimension patterns (NxM) where either N or M is greater than 5.
- The height dimension is ignored; only the two horizontal dimensions are considered.

---

## Usage

### Render all STL files to screenshots

Make sure your Blender executable is installed and accessible.

Run Blender from the command line with the main.py script:

```
"BLENDER_EXECUTABLE_PATH" --background --python main.py
```

Replace BLENDER_EXECUTABLE_PATH with your Blender executable path, for example:

"C:Program Files (x86)SteamsteamappscommonBlenderblender.exe" --background --python main.py

This command will recursively scan the STLFiles folder, import each STL, set up camera and lighting, render a screenshot, and save it in the STLFilesscreenshots folder preserving the folder structure.

---

### Clean screenshots by dimensions

Run the cleaning script with the screenshots folder path as argument:

```
python clean_screenshots.py STLFilesscreenshots
```

This will delete all PNG images whose filenames contain dimension patterns where either horizontal dimension is greater than 5.

---

## Notes

- Ensure the STLFiles folder exists in the same directory as main.py.
- The scripts preserve folder hierarchy when saving screenshots.
- The dimension format recognized in filenames is NxM (e.g., 3x5), without spaces.
- The cleaning script only looks at filenames, it does not inspect actual image content or metadata.

---

## Troubleshooting

- If Blender commands fail, check your Blender installation path.
- The STL import operator requires Blender’s STL import addon enabled by default.
- Run scripts in an environment where Python and Blender are accessible.

---

_Date: 2025-06-21_
