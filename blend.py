import os
import shutil
from pydub import AudioSegment


blended = './blended/'
temp = './tempfiles/'
filename = ['temp', 'blend']    

largest  = lambda a, b: a if os.stat(a).st_size > os.stat(b).st_size else b
smallest = lambda a, b: a if os.stat(a).st_size < os.stat(b).st_size else b

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


wav_files_in = lambda dirname: [i for i in os.listdir(dirname) if i.endswith('.wav')]

def powerset_blend(powerset):
    file_index = 0
    if not os.path.exists(blended):
        os.makedirs(blended)
        
    for subset in powerset:
        if len(subset) == 2:
            blend(subset[0], subset[1], filename[1] + f'_{file_index}', final=True)
            file_index += 1
        elif len(subset) == 3:
            os.makedirs(temp)
            blend(subset[0], subset[1], filename[0] + f'_{file_index}', final=False)
            blend(subset[2], temp + wav_files_in(temp)[-1], filename[0] + f'_{file_index}', final=True)
            shutil.rmtree(temp)
            file_index += 1
        else:
            index = 2
            os.makedirs(temp)
            blend(subset[0], subset[1], filename[0] + f'_{file_index}', final=False)
            while index <= len(subset) - 2:
                blend(subset[index], temp + wav_files_in(temp)[-1], filename[0] + f'_{file_index}', final=False)
                index += 1
            blend(subset[index], temp + wav_files_in(temp)[-1], filename[1] + f'_{file_index}', final=True)
            shutil.rmtree(temp)
            file_index += 1
