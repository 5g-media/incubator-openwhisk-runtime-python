# DeepSpeech action example

The function expects the following parameter as input

* `url` - the location of the audio file (wave format) 

The function returns the transcript and the time it took to perform the inference

```bash
{
    'transcript': <message transcript>,
    'inference_time': <inference in seconds>
}
```

## Running example of the function:

### Create the action

```
wsk action update myAction ds_action.py --docker openwhisk/python3dsaction
```

### Invoke the action

Use url to one of the sample wave files

```
wsk action invoke -r myAction -p url https://raw.githubusercontent.com/5g-media/incubator-openwhisk-runtime-python/deepspeech/core/python3DSAction/sample/audio/2830-3980-0043.wav
```

Expect a similar result
```bash
{
    "inference_time": "2.1945881301071495",
    "transcript": "experience proves this"
}
```

## Running the example on GPU enabled host

The same function can be invoked on a GPU node using the GPU runtime image (i.e. openwhisk/python3dscudaaction). Ensure the following prerequisites are met before attempting to invoke it: **TBD**

### Create the action

```
wsk action update myAction ds_action.py --docker openwhisk/python3dscudaaction
```

### Invoke the action

Invocation is same as described in above section


