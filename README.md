# Image Classification with resnet Demo for MIT-Hackathon

Step 1. Start inference server on a machine which `nvidia-docker` is correctly configured.

```bash
bash start_server.sh
```

Step 2. Run `test_service.py` to detect objects of `cat.jpg`.

```bash
python test_service.py cat.jpg
```

Step 3. Check the result
The result will print out in the Terminal
