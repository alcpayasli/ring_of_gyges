# -*- coding: utf-8 -*- 
import subprocess
from my_modules.my_print_colored import print_style
import re
class My_Mac_Changer():
    def __init__(self, interface):
        #taken users interface
        self.interface = interface
    def random_mac(self):
        """this function change mac address random"""
        subprocess.check_output(args=["ifconfig", self.interface, "down"])
        subprocess.check_output(args = ["macchanger", "-r", self.interface])
        subprocess.check_output(args=["ifconfig", self.interface, "up"])
        ifconfig = subprocess.check_output(args = ["ifconfig", self.interface])
        new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
        self.final_write = print(print_style.CGREEN + "\nNew Mac: ", new_mac.group(0).upper())
        return self.final_write
    def private_mac(self, prvmac):
        """this function change mac address user input mac"""
        subprocess.check_output(["ifconfig", self.interface, "down"])
        subprocess.check_output(["ifconfig", self.interface, "hw", "ether", prvmac])
        subprocess.check_output(["ifconfig", self.interface, "up"])
        ifconfig = subprocess.check_output(["ifconfig",self.interface])
        new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
        self.final_write_1 = print(print_style.CGREEN + "\nNew Mac: ", new_mac.group(0).upper())
        return self.final_write_1
    def orginal_mac(self):
        """this function current mac return permanent mac"""
        subprocess.check_output(["ifconfig", self.interface, "down"])
        subprocess.check_output(["macchanger", "-p", self.interface])
        subprocess.check_output(["ifconfig", self.interface, "up"])
        ifconfig = subprocess.check_output(["ifconfig",self.interface])
        org_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
        self.final_write_2 = print(print_style.CGREEN + "\nOrginal Mac:", org_mac.group(0).upper())
        return self.final_write_2
    def show_mac_address(self):
        """this function return current mac"""
        ifconfig = subprocess.check_output(["ifconfig",self.interface])
        find_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
        self.current_mac  = print(print_style.CGREEN + "\nCurrent Mac:", find_mac.group(0).upper())
        return self.current_mac