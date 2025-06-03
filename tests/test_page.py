from config.conftest import *
from pages.donat import donats
from pages.VK import vk_page
from pages.android import androids
from pages.display_fon import display
from pages.page_find1 import finds
from pages.commons import com_page
from pages.button_sharp import btn_sharp
from pages.button_java import btn_java
from pages.WB import btn_wb
from pages.button_python import btn_python
from pages.button_CPP import btn_cpp
from pages.SQL import btn_sql
from pages.Linux import btn_linux

def test_wb(page, btn_wb):
    btn_wb()

def test_donats(page, donats):
    donats()

def test_vk(page, vk_page):
    vk_page()

def test_display(page, display):
    display()

def test_comm(page, com_page):
    com_page()

def test_finds(page, finds):
    finds()


def test_python(page, btn_python):
    btn_python()

def test_full_flow2(page, btn_java):
    btn_java()

def test_sharp(page, btn_sharp):
    btn_sharp()

def test_android(page, androids):
    androids()

def test_C_2plus(page, btn_cpp):
    btn_cpp()

def test_sql(page, btn_sql):
    btn_sql()

def test_linux(page, btn_linux):
    btn_linux()

