from utils import *


def main():
    file_size = round(check_final_bytes(), 2)
    print(CmdColors.WARNING + f'\nThis procedure requires approximately {file_size} MB of memory\n' + CmdColors.ENDC)
    while True:
        user_input = input('Proceed Y/N?: ')
        if user_input in ['N', 'n']:
            print(CmdColors.FAIL + 'Procedure Aborted\n' + CmdColors.ENDC)
            raise SystemExit
        elif user_input in ['Y', 'y']:
            print(CmdColors.OKGREEN + 'Starting Procedure\n' + CmdColors.ENDC)
            powerset_blend(powerset(wav_files_in(os.getcwd()), list()))
            print(CmdColors.OKGREEN + 'Thank you for using Wavblend!\n' +CmdColors.ENDC)
            break
        else:
            print(CmdColors.WARNING + 'Invalid Entry\n' + CmdColors.ENDC)


if __name__ == '__main__':
    main()




