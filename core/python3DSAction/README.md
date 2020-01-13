# DS Action

## DeepSpeech runtime image

This GPU based image contains libraries and frameworks useful for running DeepSpeech Service: A [TensorFlow implementation](https://github.com/mozilla/DeepSpeech) of Baidu's DeepSpeech architecture.

The pre-trained English model is installed for use (see the Notes column in the table below). Currently, only 16-bit, 16 kHz, mono-channel WAVE audio files are supported in this Python runtime.

**Note:** this image has a tensorflow built against Cuda Compute Capabilities 5.0 (for Quadro M1000M) to prevent it hitting a lengthy JIT compile step. It is based on this image https://github.com/mozilla/DeepSpeech/blob/v0.6.0/Dockerfile#L79 with the modified `TF_CUDA_COMPUTE_CAPABILITIES` being set

Bellow is the version for the included libraries:

| Image Version | Package | Notes |
| ------------- | ------- | ----- |
| python3dscudaaction:compute-5.0 | DeepSpeech-gpu 0.6.0, DeepSpeech Models 0.6.0, Tensorflow 1.14 | Based on Ubuntu 18.04, Cuda 10.0, cuDNN 7.0, Python 3.6 


#### DS Action Sample

To view an example with this DS Action check the [sample/speech recognition](./sample/).

### Image Details
#### Available Python packages

For a complete list execute:

```bash
$ docker run --rm --entrypoint pip3 docker5gmedia/python3dscudaaction:compute-5.0 list
```

#### Available Ubuntu packages

For a complete list execute:

```bash
$ docker run --rm --entrypoint apt docker5gmedia/python3dscudaaction:compute-5.0 list --installed
```
