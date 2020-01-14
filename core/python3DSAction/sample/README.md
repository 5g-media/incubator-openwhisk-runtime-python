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
wsk -i action create myAction ds_action.py --docker docker5gmedia/python3dsaction
```

### Invoke the action

Use url to one of the sample wave files

```
wsk -i action invoke -r myAction -p url https://raw.githubusercontent.com/5g-media/incubator-openwhisk-runtime-python/gpu/core/python3DSAction/sample/audio/2830-3980-0043.wav
```

Expect a similar result
```bash
{
    "inference_time": "2.1945881301071495",
    "transcript": "experience proves this"
}
```

## Running the example on GPU enabled host

The same function can be invoked on a GPU node. Ensure the following [prerequisites](https://github.com/5g-media/incubator-openwhisk-deploy-kube/blob/gpu/docs/k8s-gpu-prerequisites.md) are met before attempting to invoke the action.

### Create the action

```
wsk -i action create myAction-gpu ds_action.py -m 2048 --kind python:3ds@gpu
```

**or for deepspeech 0.6.0 runtime:**

```
wsk -i action create myAction-gpu ds_action-0.6.0.py -m 2048 --kind python:3ds-0.6.0@gpu
```

### Invoke the action

```
wsk -i action invoke -r myAction-gpu -p url https://raw.githubusercontent.com/5g-media/incubator-openwhisk-runtime-python/gpu/core/python3DSAction/sample/audio/2830-3980-0043.wav
```
