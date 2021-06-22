from two_sided_document_reorderer.reorder import Mode, run
import sys
import cmd

class CommandProcessor(cmd.Cmd):
    """Command processor"""

    prompt = '(reorderer) '
    intro = 'This is an interactive mode. You may also use command-line execution:\n{0} [PDF1] [PDF2] [output] {{-r, to treat the second PDF in reverse order}}'.format(sys.argv[0])
    
    def do_reorder(self, line):
        pdf1 = input('What\'s the path of the first PDF file?')
        pdf2 = input('What\'s the path of the second PDF file?')
        output = input('Where should it be outputted?')
        reverse = input('Is the second document in reverse order? (y/N)')
        if reverse == 'y' or reverse == 'Y':
            run(pdf1, pdf2, output, mode=Mode.REVERSE_SECOND)
        else:
            run(pdf1, pdf2, output)

    def do_exit(self, line):
        return(True)

if __name__ == '__main__':
    try:
        if len(sys.argv) > 4 and sys.argv[4] == '-r':
            mode = Mode.REVERSE_SECOND
        else:
            mode = Mode.STANDARD
        run(sys.argv[1], sys.argv[2], sys.argv[3], mode=mode)
    except IndexError:
        CommandProcessor().cmdloop()