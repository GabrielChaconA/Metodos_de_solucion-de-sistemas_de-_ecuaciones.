import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Sistema.Menu import Menu
def main():
    instanciaMenu = Menu()
    instanciaMenu.menu()

if __name__ == "__main__":
    main()
