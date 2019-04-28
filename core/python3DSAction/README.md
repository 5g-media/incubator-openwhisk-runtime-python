# DS Action

## DeepSpeech runtime image

This image contains libraries and frameworks useful for running DeepSpeech Service: A [TensorFlow implementation](https://github.com/mozilla/DeepSpeech) of Baidu's DeepSpeech architecture.

The pre-trained English model is installed for use (see Notes). Currently, only 16-bit, 16 kHz, mono-channel WAVE audio files are supported in this Python runtime.

Bellow are the versions for the included libraries:

| Image Version | Package | Notes |
| ------------- | ------- | ----- |
| python3dsaction | DeepSpeech 0.4.1, DeepSpeech Models 0.4.1 | Based on Ubuntu 16.04, Python 3.5.2. The pre-trained model is installed under /models |
| GPU: python3dscudaaction | DeepSpeech-gpu 0.4.1, DeepSpeech Models 0.4.1 | Based on Ubuntu 16.04, Cuda 9.0, cuDNN 7.0, Python 3.5 


#### DS Action Sample

To view an example with this DS Action check the [sample/speech recognition](./sample/).

### Image Details
#### Available Python packages

For a complete list execute:

```bash
$ docker run --rm --entrypoint pip3 openwhisk/python3dsaction list
```

#### Available Ubuntu packages

For a complete list execute:

```bash
$ docker run --rm --entrypoint apt openwhisk/python3dsaction list --installed
```

#### Available Python packages for GPU version

For a complete list execute:

```bash
$ docker run --rm --entrypoint pip3 openwhisk/python3dscudaaction list
```

#### Available Ubuntu packages for GPU version

For a complete list execute:

```bash
$ docker run --rm --entrypoint apt openwhisk/python3dscudaaction list --installed
```

