import onnxruntime
class WrapInferenceSession:

    def __init__(self, onnx_bytes):
        self.sess = onnxruntime.InferenceSession(onnx_bytes.SerializeToString())
        self.onnx_bytes = onnx_bytes

    def run(self, *args):
        return self.sess.run(*args)

    def __getstate__(self):
        return {'onnx_bytes': self.onnx_bytes}

    def __setstate__(self, values):
        self.onnx_bytes = values['onnx_bytes']
        self.sess = onnxruntime.InferenceSession(onnx_bytes.SerializeToString()) 