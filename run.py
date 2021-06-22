import two_sided_document_reorderer
import sys
import cmd

class CommandProcessor(cmd.Cmd):
    """Command processor"""
    
    def do_reorder(self, line):
        pdf1 = input('What\'s the path of the first PDF file?')
        pdf2 = input('What\'s the path of the second PDF file?')
        output = input('Where should it be outputted?')
        two_sided_document_reorderer.reorder.run(pdf1, pdf2, output)

    def do_exit(self, line):
        return(True)

if __name__ == '__main__':
    try:
        two_sided_document_reorderer.reorder.run(sys.argv[1], sys.argv[2], sys.argv[3])
    except IndexError:
        CommandProcessor().cmdloop()