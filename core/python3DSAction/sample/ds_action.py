"""Sample DeepSpeech action.

/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
 
 This example is inspired from https://github.com/mozilla/DeepSpeech/blob/master/native_client/python/client.py
"""

from deepspeech import Model
import numpy as np
import shlex
import subprocess
from timeit import default_timer as timer
import urllib.request
import wave


BEAM_WIDTH = 1024
N_FEATURES = 26
N_CONTEXT = 9
modelPath = '/models/output_graph.pbmm'
alphabetPath = '/models/alphabet.txt'

LM_ALPHA = 0.75
LM_BETA = 1.85
lmPath = '/models/lm.binary'
triePath = '/models/trie'


try:
    from shhlex import quote
except ImportError:
    from pipes import quote


def main(parm):

    try:    
        if not parm.get('url'):
            return {
                'error': "Missing 'url' parameter"
            }
        def convert_samplerate(audio_path):
            sox_cmd = 'sox {} --type raw --bits 16 --channels 1 --rate 16000 --encoding signed-integer --endian little --compression 0.0 --no-dither - '.format(quote(audio_path))
            try:
                output = subprocess.check_output(shlex.split(sox_cmd), stderr=subprocess.PIPE)
            except subprocess.CalledProcessError as e:
                raise RuntimeError('SoX returned non-zero status: {}'.format(e.stderr))
            except OSError as e:
                raise OSError(e.errno, 'SoX not found, use 16kHz files or install it: {}'.format(e.strerror))

            return 16000, np.frombuffer(output, np.int16)

        print('Loading model from file {}'.format(modelPath))
        model_load_start = timer()

        ds = Model(modelPath, N_FEATURES, N_CONTEXT, alphabetPath, BEAM_WIDTH)
        model_load_end = timer() - model_load_start
        print('Loaded model in {:.3}s.'.format(model_load_end))

        lm_load_start = timer()
        ds.enableDecoderWithLM(alphabetPath, lmPath, triePath, LM_ALPHA, LM_BETA)
        lm_load_end = timer() - lm_load_start
        print('Loaded language model in {:.3}s.'.format(lm_load_end))

        urllib.request.urlretrieve(parm['url'], '/audio-temp.wav')
        fin = wave.open('/audio-temp.wav', 'rb')
        fs = fin.getframerate()
        if fs != 16000:
            print('Warning: original sample rate ({}) is different than 16kHz. Resampling might produce erratic speech recognition.'.format(fs))
            fs, audio = convert_samplerate('/audio-temp.wav')
        else:
            audio = np.frombuffer(fin.readframes(fin.getnframes()), np.int16)

        audio_length = fin.getnframes() * (1/16000)
        fin.close()

        print('Running inference.')
        inference_start = timer()
        transcript = ds.stt(audio, fs)
        print(transcript)
        inference_end = timer() - inference_start
        print('Inference took %0.3fs for %0.3fs audio file.' % (inference_end, audio_length))

        return {
            'transcript': transcript,
            'inference_time': str(inference_end)
        }
    except Exception as e:
        return {
            'error': 'Error occurred: %s' % str(e)
        }