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

## Running the example on GPU enabled host

Ensure the following [prerequisites](https://github.com/5g-media/incubator-openwhisk-deploy-kube/blob/gpu-rhel/docs/k8s-gpu-prerequisites.md) are met before attempting to invoke the action.

### Create the action

```
wsk -i action create myAction-gpu ds_action.py -m 2048 --kind python:3ds@gpu
```

### Invoke the action

Use url to one of the sample wave files

```
wsk -i action invoke -r myAction-gpu -p url https://raw.githubusercontent.com/5g-media/incubator-openwhisk-runtime-python/gpu-rhel/core/python3DSAction/sample/audio/2830-3980-0043.wav
```

Expect a similar result
```bash
{
    "inference_time": "2.1945881301071495",
    "transcript": "experience proves this"
}
```
