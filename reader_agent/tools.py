"""Tools for reading and parsing API specification files."""

import json
import os
from pathlib import Path
from typing import Union, Dict, Any

try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False


def read_api_spec(file_path: str) -> Dict[str, Any]:
    """
    Read an API specification file and return its contents.
    
    Supports JSON and YAML formats (.json, .yaml, .yml).
    
    Args:
        file_path: Path to the API specification file.
        
    Returns:
        Dictionary containing the parsed API specification.
        
    Raises:
        FileNotFoundError: If the file doesn't exist.
        ValueError: If the file format is not supported or parsing fails.
    """
    file_path = Path(file_path).resolve()
    
    if not file_path.exists():
        raise FileNotFoundError(f"API spec file not found: {file_path}")
    
    suffix = file_path.suffix.lower()
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            if suffix == '.json':
                return json.load(f)
            elif suffix in ['.yaml', '.yml']:
                if not YAML_AVAILABLE:
                    raise ValueError("YAML support requires PyYAML. Install it with: pip install pyyaml")
                return yaml.safe_load(f)
            else:
                raise ValueError(f"Unsupported file format: {suffix}. Supported formats: .json, .yaml, .yml")
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON file: {e}")
    except yaml.YAMLError as e:
        raise ValueError(f"Failed to parse YAML file: {e}")


def read_api_spec_as_string(file_path: str) -> str:
    """
    Read an API specification file and return its raw contents as a string.
    
    Supports JSON and YAML formats (.json, .yaml, .yml).
    
    Args:
        file_path: Path to the API specification file.
        
    Returns:
        String containing the raw file contents.
        
    Raises:
        FileNotFoundError: If the file doesn't exist.
    """
    file_path = Path(file_path).resolve()
    
    if not file_path.exists():
        raise FileNotFoundError(f"API spec file not found: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def list_api_specs(directory: str = ".") -> list[str]:
    """
    List all API specification files in a directory.
    
    Args:
        directory: Directory to search for API specs. Defaults to current directory.
        
    Returns:
        List of paths to API specification files found.
    """
    dir_path = Path(directory).resolve()
    
    if not dir_path.is_dir():
        raise ValueError(f"Not a valid directory: {directory}")
    
    spec_files = []
    for ext in ['*.json', '*.yaml', '*.yml']:
        spec_files.extend([str(p) for p in dir_path.glob(f"**/{ext}")])
    
    return sorted(spec_files)
