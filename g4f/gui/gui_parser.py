from argparse import ArgumentParser

def gui_parser():
    parser = ArgumentParser(description="Run the GUI")
    parser.add_argument("-host", type=str, default="0.0.0.0", help="hostname")
    parser.add_argument("-port", type=int, default=80, help="port")
    parser.add_argument("-debug", action="store_true", help="debug mode")
    return parser
