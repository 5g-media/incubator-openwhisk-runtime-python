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

### Run the development container

This command runs a playbox container that that contains the tools (e.g. pre-configured `wsk` OpenWhisk CLI) needed to run the example. We pass it the ip:port of OpenWhisk controller (Ingress).

If you are running Minikube per [prerequisites](https://github.com/5g-media/incubator-openwhisk-deploy-kube/blob/gpu/docs/k8s-gpu-prerequisites.md#minikube) requirements then simply invoke the below command as is. Otherwise, substitute `sudo minikube ip`:31001 with ip:port of your OpenWhisk controller IP address and port.

```bash
docker run -it -e OPENWHISK_APIHOST=`sudo minikube ip`:31001 --rm docker5gmedia/5gmedia-playbox-minikube-ow-gpu:1.0 /bin/bash
```

Run all the following commands from inside the container.

### Create the action

```
wsk -i action create myAction-gpu ds_action.py -m 2048 --kind python:3ds@gpu
```

### Invoke the action

```
wsk -i action invoke -r myAction-gpu -p url https://raw.githubusercontent.com/5g-media/incubator-openwhisk-runtime-python/gpu/core/python3DSAction/sample/audio/2830-3980-0043.wav
```

### Action log inspection

You should be able to see TensorFlow logs in action's logs identifying the GPU to run the inference on it.

This time, invoke the action with `b` switch to print its activation result:

```
wsk -i action invoke -b myAction-gpu -p url https://raw.githubusercontent.com/5g-media/incubator-openwhisk-runtime-python/gpu/core/python3DSAction/sample/audio/2830-3980-0043.wav
```

And inspect the `Logs` entry. You should similar trace to this
```
"2019-07-11T07:25:13.896790957Z stdout: 2019-07-11 07:25:13.845130: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1115] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 10374 MB memory) -> physical GPU (device: 0, name: GeForce GTX 1080 Ti, pci bus id: 0000:01:00.0, compute capability: 6.1)",
```
