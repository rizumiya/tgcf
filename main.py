import os
from importlib import resources
import logging
import tgcf.web_ui as wu
import streamlit as st

def main():
    package_dir = resources.path(package=wu, resource="").__enter__()
    print(package_dir)
    path = os.path.join(package_dir, "0_👋_Hello.py")
    os.system(f"streamlit run {path}")

current_dir = os.getcwd()
print("test", current_dir)
main()
