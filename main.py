# -*- coding: utf-8 -*-

import sys
from pathlib import Path
import os
import json
import logging
from typing import List, Dict, Any
from flowlauncher import FlowLauncher

# Set up logging
plugindir = Path.absolute(Path(__file__).parent)
log_file = os.path.join(plugindir, 'folder_list_plugin.log')
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class FolderListPlugin(FlowLauncher):
    def __init__(self):
        try:
            logging.debug("Initializing FolderListPlugin")
            self.settings_file = os.path.join(plugindir, 'settings.json')
            self.load_settings()
            super().__init__()
            logging.debug("FolderListPlugin initialized successfully")
        except Exception as e:
            logging.error(f"Error initializing plugin: {str(e)}")
            raise

    def load_settings(self):
        try:
            if os.path.exists(self.settings_file):
                with open(self.settings_file, 'r') as f:
                    self.settings = json.load(f)
            else:
                self.settings = {"keywords": {}}
                self.save_settings()
            logging.debug(f"Loaded settings: {self.settings}")
        except Exception as e:
            logging.error(f"Error loading settings: {str(e)}")
            self.settings = {"keywords": {}}

    def save_settings(self):
        try:
            with open(self.settings_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
            logging.debug("Settings saved successfully")
        except Exception as e:
            logging.error(f"Error saving settings: {str(e)}")

    def query(self, query: str) -> List[Dict[str, Any]]:
        try:
            logging.debug(f"Received query: {query}")
            
            # If query is empty, show all current keywords
            if not query.strip():
                return self.list_keywords()
            
            # Check if this is a keyword setting command (keyword : path)
            if ':' in query:
                parts = query.split(':', 1)
                if len(parts) == 2:
                    keyword = parts[0].strip()
                    path = parts[1].strip().strip('"\'')  # Remove quotes if present
                    
                    if os.path.exists(path):
                        self.set_keyword(keyword, path)
                        return [{
                            "Title": "✅ Keyword saved successfully!",
                            "SubTitle": f"Keyword: {keyword} → Path: {path}",
                            "IcoPath": "images/app.png",
                            "JsonRPCAction": {
                                "method": "open_path",
                                "parameters": [path],
                                "dontHideAfterAction": False
                            }
                        }]
                    else:
                        return [{
                            "Title": "❌ Invalid path",
                            "SubTitle": f"Path does not exist: {path}",
                            "IcoPath": "images/app.png"
                        }]
            
            # Check if this is a path
            if os.path.exists(query):
                logging.debug(f"Query is a valid path: {query}")
                return self.list_path_contents(query)
            
            # Check for keywords that start with the query
            matching_keywords = [k for k in self.settings["keywords"].keys() if k.startswith(query.lower())]
            
            if matching_keywords:
                results = []
                for keyword in matching_keywords:
                    path = self.settings["keywords"][keyword]
                    # Get the last folder name from the path
                    folder_name = os.path.basename(path)
                    results.append({
                        "Title": f"! Open folder: {folder_name}",
                        "SubTitle": f"Keyword: {keyword} → Full path: {path}",
                        "IcoPath": "images/folder.png",
                        "JsonRPCAction": {
                            "method": "open_path",
                            "parameters": [path],
                            "dontHideAfterAction": False
                        }
                    })
                return results
            
            # If we get here, it's neither a path nor a matching keyword
            return [{
                "Title": "Path or keyword not found",
                "SubTitle": f"'{query}' is not a valid path or keyword",
                "IcoPath": "images/app.png"
            }]
            
        except Exception as e:
            logging.error(f"Error in query: {str(e)}")
            return [{
                "Title": "Error",
                "SubTitle": str(e),
                "IcoPath": "images/app.png"
            }]

    def list_keywords(self) -> List[Dict[str, Any]]:
        results = []
        for keyword, path in self.settings["keywords"].items():
            results.append({
                "Title": f"Keyword: {keyword}",
                "SubTitle": f"Path: {path}",
                "IcoPath": "images/app.png",
                "JsonRPCAction": {
                    "method": "open_path",
                    "parameters": [path],
                    "dontHideAfterAction": False
                }
            })
        
        if not results:
            results.append({
                "Title": "No keywords set",
                "SubTitle": "Type 'keyword : path' to set up a new keyword",
                "IcoPath": "images/app.png"
            })
        
        return results

    def list_path_contents(self, path: str) -> List[Dict[str, Any]]:
        logging.debug(f"Listing contents of path: {path}")
        
        if not os.path.exists(path):
            return [{
                "Title": "Path not found",
                "SubTitle": f"Path does not exist: {path}",
                "IcoPath": "images/app.png"
            }]
        
        folders = []
        files = []
        try:
            for item in os.listdir(path):
                full_path = os.path.join(path, item)
                is_dir = os.path.isdir(full_path)
                
                result = {
                    "Title": item,
                    "SubTitle": f"{'Folder' if is_dir else 'File'}: {full_path}",
                    "IcoPath": "images/folder.png" if is_dir else "images/file.png",
                    "JsonRPCAction": {
                        "method": "open_path",
                        "parameters": [full_path],
                        "dontHideAfterAction": False
                    }
                }
                
                if is_dir:
                    folders.append(result)
                else:
                    files.append(result)
                
                logging.debug(f"Added result for: {item}")
            
            # Sort folders and files alphabetically
            folders.sort(key=lambda x: x["Title"].lower())
            files.sort(key=lambda x: x["Title"].lower())
            
            # Combine results with folders first, then files
            results = folders + files
            
            logging.debug(f"Total results: {len(results)}")
            return results
            
        except Exception as e:
            logging.error(f"Error listing directory: {str(e)}")
            return [{
                "Title": "Error",
                "SubTitle": f"Failed to list directory: {str(e)}",
                "IcoPath": "images/app.png"
            }]

    def run(self, query: str) -> None:
        try:
            logging.debug(f"Run method called with query: {query}")
        except Exception as e:
            logging.error(f"Error in run method: {str(e)}")
            raise

    def open_path(self, path: str) -> None:
        try:
            logging.debug(f"Opening path: {path}")
            os.startfile(path)
        except Exception as e:
            logging.error(f"Error opening path: {str(e)}")
            raise

    def set_keyword(self, keyword: str, path: str) -> None:
        try:
            logging.debug(f"Setting keyword '{keyword}' for path: {path}")
            self.settings["keywords"][keyword.lower()] = path
            self.save_settings()
        except Exception as e:
            logging.error(f"Error setting keyword: {str(e)}")
            raise

if __name__ == "__main__":
    try:
        logging.debug("Starting FolderListPlugin")
        plugin = FolderListPlugin()
    except Exception as e:
        logging.critical(f"Critical error in plugin: {str(e)}")
        print(json.dumps({
            "result": [{
                "Title": "Critical Error",
                "SubTitle": "The plugin encountered a critical error. Check the log file for details.",
                "IcoPath": "images/app.png"
            }]
        })) 