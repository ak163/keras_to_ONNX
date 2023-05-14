Remember to import onnx and keras2onnx packages.
keras2onnx.convert_keras() function converts the keras model to ONNX object.
onnx.save_model() function is to save the ONNX object into .onnx file.


#Do inferecing fololwoing way
import onnxruntime
sess = onnxruntime.InferenceSession(onnx_model)
let us say x is your input then do following

x = x if isinstance(x, list) else [x]
feed = dict([(input.name, x[n]) for n, input in enumerate(sess.get_inputs())])
pred_onnx = sess.run(None, feed)[0]
