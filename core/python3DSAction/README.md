# DS Action

This image contains libraries and frameworks useful for running DeepSpeech Service: A [TensorFlow implementation](https://github.com/mozilla/DeepSpeech) of Baidu's DeepSpeech architecture.

The pre-trained English model is installed for use (see Notes). Currently, only 16-bit, 16 kHz, mono-channel WAVE audio files are supported in this Python runtime.

Bellow are the versions for the included libraries:

| Image Version | Package | Notes |
| ------------- | ------- | ----- |
| 0.1      | Tensorflow 1.12.0, DeepSpeech 0.4.1, DeepSpeech Models 0.4.1 | Based on Ubuntu Xenail, Python 3.5.2. The pre-trained model is installed under /models


#### DS Action Sample

To view an example with this DS Action check the [sample/speech recognition](./sample/).

### 0.1 Details
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
