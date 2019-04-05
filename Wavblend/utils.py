from config import *
from pydub import AudioSegment
from tqdm import tqdm


blended         = Config.BLENDED
temp            = Config.TEMP
filename        = Config.FILE_NAME
largest         = Config.LARGEST
smallest        = Config.SMALLEST
wav_files_in    = Config.WAV_FILES_IN
sample_rate     = Config.SAMPLE_RATE
bit_depth       = Config.BIT_DEPTH
channels        = Config.CHANNELS


def create_blended_dir():
    if not os.path.exists(blended):
        os.makedirs(blended)
    else:
        raise FileExistsError(f'{blended} folder already exists.')


def blend(audio1, audio2, filename, final=False):
    primary = largest(audio1, audio2) 
    secondary = smallest(audio1, audio2)
    A = AudioSegment.from_file(primary)
    B = AudioSegment.from_file(secondary)
    state = blended if final else temp
    A.overlay(B).export(state + filename + '.wav', format='wav')


def powerset(data, newset):
    if data == list():
        return [newset]
    else:
        pset = list()
        for s in powerset(data[1:], newset + [data[0]]):
            pset.append(s)
        for s in powerset(data[1:], newset):
            pset.append(s)
        return [item for item in pset if len(item) >= 2]


def powerset_blend(powerset):
    total = len(powerset)
    file_index = 0
    create_blended_dir()
    with tqdm(total=total) as pbar:
        for subset in powerset:
            if len(subset) == 2:
                blend(subset[0], subset[1], filename[1] + f'_{file_index}', final=True)
                file_index += 1
                pbar.update()
            elif len(subset) == 3:
                os.makedirs(temp)
                blend(subset[0], subset[1], filename[0] + f'_{file_index}', final=False)
                blend(subset[2], temp + wav_files_in(temp)[-1], filename[0] + f'_{file_index}', final=True)
                shutil.rmtree(temp)
                file_index += 1
                pbar.update()
            else:
                index = 2
                temp_index = 0
                os.makedirs(temp)
                blend(subset[0], subset[1], filename[0] + f'_{file_index}_{temp_index}', final=False)
                temp_index += 1
                while index <= len(subset) - 2:
                    blend(subset[index], temp + wav_files_in(temp)[-1], filename[0] + f'_{file_index}_{temp_index}', final=False)
                    index += 1
                    temp_index += 1
                blend(subset[index], temp + wav_files_in(temp)[-1], filename[1] + f'_{file_index}', final=True)
                shutil.rmtree(temp)
                file_index += 1
                pbar.update()
    print(CmdColors.OKGREEN + f'\nCompleted {file_index}/{total} files\n' + CmdColors.ENDC)

def check_final_bytes():
    MB = 1000000
    overhead = 1.3
    size = 0
    pset = powerset(wav_files_in(os.getcwd()), list())
    for subset in powerset(wav_files_in(os.getcwd()), list()):
        size += max([os.stat(i).st_size for i in subset]) * (bit_depth * sample_rate * channels) / MB
        return size 
