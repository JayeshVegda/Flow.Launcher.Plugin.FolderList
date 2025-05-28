# Folder List Plugin for Flow Launcher

A simple plugin that lets you quickly access your favorite folders using custom keywords.

## Features

- List files and folders from any directory
- Set custom keywords for your frequently used folders
- Quick access to your folders using keywords
- Easy navigation through folder contents

## How to Use

### Basic Usage

1. Open Flow Launcher
2. Type `folder` followed by:
   - A folder path (e.g., `folder C:/Your/Dog/Videos/Path`)
   - A keyword you've set (e.g., `folder dogvids`)

### Setting Up Keywords

1. Type a folder path (e.g., `folder C:/Your/Dog/Videos/Path`)
2. When you see the folder list, press the right arrow key (→) on any folder
3. Select "Set as Keyword" from the context menu
4. The folder will now be accessible using that keyword

### Managing Keywords

- Type `folder` without any additional text to see all your current keywords
- Click on any keyword to open its associated folder
- Keywords are automatically saved in `settings.json`

## Examples

```
folder C:/Videos/Dogs           # Browse the Dogs folder
folder dogvids                  # Access the folder using keyword
folder                         # List all your keywords
```

## Troubleshooting

If you encounter any issues:
1. Check the `folder_list_plugin.log` file for error messages
2. Make sure the paths you're trying to access exist
3. Ensure you have the necessary permissions to access the folders

## Settings

The plugin uses a `settings.json` file to store your keywords. You can edit this file directly if needed:

```json
{
    "keywords": {
        "dogvids": "C:/Videos/Dogs",
        "catvids": "C:/Videos/Cats"
    }
}
```

## Requirements

- Flow Launcher
- Python 3.7 or higher
- Windows operating system 

folder catsvid : "C:/Your/Path/Here" 

folder catsvid 