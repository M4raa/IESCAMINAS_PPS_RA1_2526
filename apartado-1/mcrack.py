#!/usr/bin/env python
# mcrack.py
# Autor: David Maratrat Pons
# Fecha: 25/11/2025
# Versión: 1.0
# Description: This program is a password cracker for
# Office and PDF files based on a dictionary attack.

import argparse
import time
import sys
import os
import io
import msoffcrypto
import pikepdf
from colorama import Fore, Style, init

# Import the render_text function from the ascii_letters module
# This module is expected to be in a subdirectory named 'lib'
# If the module is not found, the program will exit with an error message
try:
    from lib.ascii_letters import render_text
except ImportError:
    print("Error: Couldn't find 'ascii_letters.py'.")
    sys.exit(1)

init(autoreset=True)

# ==========================================
# AUXILIAR FUNCTIONS
# ==========================================

# Function to count the number of lines in a file
def get_total_lines(filepath):
    try:
        with open(filepath, 'rb') as f:
            return sum(1 for _ in f)
    except Exception:
        return 0

# Function to format time
def time_format(seconds):
    if seconds < 0: seconds = 0
    return time.strftime("%H:%M:%S", time.gmtime(seconds))

# ==========================================
# CRACKING FUNCTIONS
# ==========================================

# Function to try to crack an Office file
def try_office(target_file, password, extension):
    try:
        file = msoffcrypto.OfficeFile(target_file)
        file.load_key(password=password)

        # Sometimes load_key says True with incorrect passwords (False Positive).
        # To avoid it, we decrypt in memory and check the header of the resulting file.
        output = io.BytesIO()
        file.decrypt(output) # Try to decrypt in memory
        
        # If it's a modern file (docx, xlsx, pptx), the result MUST be a ZIP.
        # ZIP files always start with the "Magic Bytes": PK (0x50 0x4B)
        if extension in ['.docx', '.xlsx', '.pptx']:
            output.seek(0)
            magic = output.read(2)
            # If it doesn't start with PK, the password '1' was a false positive.
            if magic != b'PK':
                return False
        return True 
        
    except Exception:
        return False

# Function to try to crack a PDF file
def try_pdf(target_file, password):
    try:
        pikepdf.open(target_file, password=password)
        return True
    except pikepdf.PasswordError:
        return False
    except Exception:
        return False

# Function to perform the attack
def perform_attack(wordlist, target_file, file_type):
    total_passwords = get_total_lines(wordlist)
    start_time = time.time()
    
    # Get file extension
    ext = os.path.splitext(target_file)[1].lower()

    # Banner
    print(Fore.CYAN + Style.BRIGHT + render_text("MCRACK"))
    print(Fore.WHITE + "="*60)
    print(Fore.GREEN + f"[*] File: {Fore.WHITE}{target_file}")
    print(Fore.GREEN + f"[*] Type: {Fore.WHITE}{file_type.upper()}")
    print(Fore.GREEN + f"[*] Dictionary: {Fore.WHITE}{wordlist} ({total_passwords} words)")
    print(Fore.WHITE + "="*60 + "\n")

    effective_file = None
    if file_type == 'office':
        try:
            effective_file = open(target_file, 'rb')
        except IOError:
            print(Fore.RED + "Error: Can't open the target file.")
            return

    try:
        with open(wordlist, 'r', encoding='latin-1', errors='ignore') as f:
            count = 0
            for line in f:
                password = line.strip()
                count += 1
                
                # Time
                now = time.time()
                elapsed = now - start_time
                rate = count / elapsed if elapsed > 0 else 0
                time_left = (total_passwords - count) / rate if rate > 0 else 0
                str_elapsed = time_format(elapsed)
                str_time_left = time_format(time_left)

                # Dynamic output
                message = (
                    f"{Fore.BLUE}[Tiempo: {str_elapsed}] "
                    f"{Fore.MAGENTA}[Restante: {str_time_left}] "
                    f"{Fore.WHITE}Probando: {Fore.YELLOW}{password:<20}"
                )
                sys.stdout.write(f"\r{message}")
                sys.stdout.flush()

                # Verification
                found = False
                if file_type == 'office':
                    effective_file.seek(0)
                    # Pass the extension to activate the anti-false-positive verification
                    if try_office(effective_file, password, ext):
                        found = True
                elif file_type == 'pdf':
                    if try_pdf(target_file, password):
                        found = True

                if found:
                    sys.stdout.write("\r" + " "*100 + "\r") # Clear line
                    
                    # --- SUCCESS MESSAGE ---
                    print(Fore.GREEN + Style.BRIGHT + "\n" + "╔" + "═"*50 + "╗")
                    print(Fore.GREEN + Style.BRIGHT + "║                 ¡PASSWORD FOUND!                 ║")
                    print(Fore.GREEN + Style.BRIGHT + "╠" + "═"*50 + "╣")
                    print(Fore.GREEN + Style.BRIGHT + "║ Password: " + Fore.WHITE + Style.BRIGHT + f"{password:^34}" + Fore.GREEN + "     ║")
                    print(Fore.GREEN + Style.BRIGHT + "╚" + "═"*50 + "╝\n")
                    
                    print(Fore.WHITE + f"[*] Total time: {str_elapsed}")
                    return

    except KeyboardInterrupt:
        sys.stdout.write("\r" + " "*100 + "\r")
        print(Fore.RED + "\n[!] Stopped by the user.")
        sys.exit()
    finally:
        if effective_file:
            effective_file.close()

    sys.stdout.write("\r" + " "*100 + "\r")
    print(Fore.RED + Style.BRIGHT + "[-] Password not found in the dictionary.")

# Main function
def main():
    parser = argparse.ArgumentParser(description="M-CRACK")
    parser.add_argument("-w", "--wordlist", required=True, help="Wordlist")
    parser.add_argument("-f", "--file", dest="target_file", required=True, help="File")
    
    args = parser.parse_args()

    if not os.path.exists(args.wordlist):
        sys.exit(Fore.RED + "Wordlist not found: %s" % args.wordlist)
    if not os.path.exists(args.target_file):
        sys.exit(Fore.RED + "File not found: %s" % args.target_file)

    ext = os.path.splitext(args.target_file)[1].lower()
    if ext in ['.docx', '.xlsx', '.pptx', '.accdb', '.mdb']:
        file_type = 'office'
    elif ext == '.pdf':
        file_type = 'pdf'
    else:
        file_type = 'office'

    perform_attack(args.wordlist, args.target_file, file_type)

if __name__ == "__main__":
    main()