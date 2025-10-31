#!/usr/bin/env python3
"""
Environment validation script for SlugLime backend.
Run this before starting the server to check if everything is set up correctly.
"""
import sys
import os
from pathlib import Path

# Color codes for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def print_success(msg):
    print(f"{GREEN}✓{RESET} {msg}")

def print_error(msg):
    print(f"{RED}✗{RESET} {msg}")

def print_warning(msg):
    print(f"{YELLOW}⚠{RESET} {msg}")

def check_python_version():
    """Check if Python version is 3.10 or higher"""
    print("\n1. Checking Python version...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 10:
        print_success(f"Python {version.major}.{version.minor}.{version.micro} ✓")
        return True
    else:
        print_error(f"Python {version.major}.{version.minor}.{version.micro} - Need Python 3.10+")
        return False

def check_dependencies():
    """Check if all required packages are installed"""
    print("\n2. Checking dependencies...")
    required = [
        'flask', 'flask_cors', 'flask_sqlalchemy', 'marshmallow',
        'dotenv', 'werkzeug', 'passlib', 'argon2', 'itsdangerous'
    ]
    
    missing = []
    for package in required:
        try:
            if package == 'dotenv':
                __import__('dotenv')
            elif package == 'argon2':
                __import__('argon2')
            else:
                __import__(package)
            print_success(f"{package}")
        except ImportError:
            print_error(f"{package} - NOT INSTALLED")
            missing.append(package)
    
    if missing:
        print_error(f"\nMissing packages: {', '.join(missing)}")
        print(f"\nInstall them with: pip install -r requirements.txt")
        return False
    return True

def check_env_file():
    """Check if .env file exists and has required variables"""
    print("\n3. Checking environment configuration...")
    env_path = Path('.env')
    
    if not env_path.exists():
        print_warning(".env file not found")
        print("  Creating from .env.example...")
        
        example_path = Path('.env.example')
        if example_path.exists():
            import shutil
            shutil.copy(example_path, env_path)
            print_success(".env created from .env.example")
            print_warning("IMPORTANT: Edit .env and set a secure SECRET_KEY!")
            return False
        else:
            print_error(".env.example not found")
            return False
    
    # Check if SECRET_KEY is set
    with open(env_path, 'r') as f:
        content = f.read()
        if 'SECRET_KEY=' in content:
            # Check if it's still the default
            if 'change-this' in content.lower():
                print_warning("SECRET_KEY is still the default value")
                print("  Please set a secure SECRET_KEY in .env")
                return False
            print_success(".env file exists with SECRET_KEY set")
            return True
        else:
            print_error("SECRET_KEY not found in .env")
            return False

def check_directories():
    """Check if required directories exist"""
    print("\n4. Checking directories...")
    dirs = ['instance', 'uploads']
    
    for dir_name in dirs:
        dir_path = Path(dir_name)
        if dir_path.exists():
            print_success(f"{dir_name}/ exists")
        else:
            print_warning(f"{dir_name}/ not found - will be created on startup")
    return True

def check_imports():
    """Test if local modules can be imported"""
    print("\n5. Checking local modules...")
    modules = ['config', 'database', 'models', 'schemas', 'security']
    
    for module in modules:
        try:
            __import__(module)
            print_success(f"{module}.py")
        except Exception as e:
            print_error(f"{module}.py - {str(e)}")
            return False
    return True

def main():
    print("="*60)
    print("SlugLime Backend Environment Validation")
    print("="*60)
    
    checks = [
        check_python_version(),
        check_dependencies(),
        check_env_file(),
        check_directories(),
        check_imports(),
    ]
    
    print("\n" + "="*60)
    if all(checks):
        print_success("All checks passed! ✓")
        print("\nYou can now start the server:")
        print("  python app.py")
    else:
        print_error("Some checks failed ✗")
        print("\nPlease fix the issues above before starting the server.")
        sys.exit(1)
    print("="*60)

if __name__ == "__main__":
    main()
