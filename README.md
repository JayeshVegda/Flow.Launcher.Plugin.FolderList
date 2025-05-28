# Folder List Plugin for Flow Launcher

A simple plugin that helps you quickly access your favorite folders using custom keywords.

## 🚀 Quick Start

1. Type `folder` in Flow Launcher
2. Add a new keyword: `folder mykeyword : C:/Your/Path/Here`
3. Access your folder: `folder mykeyword`

## 📥 Installation

1. Download the latest release from the [Releases page](https://github.com/JayeshVegda/Flow.Launcher.Plugin.FolderList/releases)
2. Extract the downloaded zip file
3. Copy the extracted folder to your Flow Launcher plugins directory:
   - `%APPDATA%\FlowLauncher\Plugins\`
4. Restart Flow Launcher
5. Type `folder` to start using the plugin

## ✨ Features

- 🔑 Create custom keywords for your folders
- 📂 Quick access to folder contents
- 🔍 Search through your keywords
- 📝 Easy to use command format

## 📝 How to Use

### Adding a New Keyword

```
folder mykeyword : C:/Your/Path/Here
```

### Accessing a Folder

```
folder mykeyword
```

### Viewing All Keywords

```
folder
```

## 💡 Examples

```
folder docs : C:/Documents
folder pics : D:/Pictures
folder work : E:/Projects
```

## ⚠️ Common Issues

- ❌ "Keyword already exists" - Choose a different keyword
- ❌ "Path already exists" - This folder is already linked to another keyword
- ❌ "Access Denied" - You don't have permission to access this folder

## 🔧 Requirements

- Flow Launcher
- Windows 10 or later

## 📝 Notes

- Keywords are case-insensitive
- Each folder can only have one keyword
- Each keyword can only point to one folder
- Paths must exist on your computer

## 🤝 Contributing

Feel free to submit issues and enhancement requests! 